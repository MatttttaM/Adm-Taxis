import reflex as rx
from typing import List
from sqlmodel import Field, select, asc, desc, or_, cast, String
from datetime import datetime
import csv
from taxi.constants import APORTE, SALARIO, TZ
from .notificaciones import send_email


# class Item(rx.Base):
#     """Item para la tabla."""
#     name: str
#     payment: float
#     date: str
#     status: str


class Liquidaciones(rx.Model, table=True):
    """Modelo de Liquidación."""

    __table_args__ = {'extend_existing': True}
    
    cod_id: str = Field(primary_key=True)
    chofer: int
    movil: int
    recaudacion: int
    gastos: float
    salario: float
    combustible: int
    extras: int
    liquido: float
    aportes: float
    sub_total: float
    h13: float
    credito: float
    entrega: float
    fecha: str
    estado: str


class TableState(rx.State):
    """Estado principal para la tabla y gestión de liquidaciones."""
    liquidaciones: List[Liquidaciones] = []
    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False
    total_liquidacioness: int = 0
    offset: int = 0
    limit: int = 12  # Límite de filas por página
    current_liquidacion: Liquidaciones = Liquidaciones()

    @rx.var(cache=True)
    def filtered_sorted_liquidacioness(self) -> List[Liquidaciones]:
        """Ordena y filtra las liquidaciones según el valor de búsqueda y orden."""
        liquidaciones = self.liquidaciones

        # Ordenar por el valor de la columna seleccionada
        if self.sort_value:
            sort_column = getattr(Liquidaciones, self.sort_value)
            order = desc(sort_column) if self.sort_reverse else asc(sort_column)
            liquidaciones = sorted(
                liquidaciones,
                key=lambda liquidaciones: getattr(liquidaciones, self.sort_value),
                reverse=self.sort_reverse,
            )

        # Filtrar por valor de búsqueda
        if self.search_value:
            search_value = self.search_value.lower()
            liquidaciones = [
                liquidacion for liquidacion in liquidaciones
                if any(search_value in str(getattr(liquidacion, attr)).lower()
                for attr in ["chofer", "movil", "recaudacion", "estado"])
            ]

        return liquidaciones

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return (self.total_liquidacioness // self.limit) + (1 if self.total_liquidacioness % self.limit else 0)

    @rx.var(cache=True)
    def get_current_page(self) -> List[Liquidaciones]:
        """Obtiene los elementos de la página actual."""
        start_index = self.offset
        end_index = start_index + self.limit
        return self.filtered_sorted_liquidacioness[start_index:end_index]

    def prev_page(self):
        if self.offset > 0:
            self.offset -= self.limit

    def next_page(self):
        if self.offset + self.limit < self.total_liquidacioness:
            self.offset += self.limit

    def load_entries(self):
        """Carga las liquidaciones desde la base de datos."""
        with rx.session(url="mysql+pymysql://<user>:<password>@<host>/defaultdb") as session:
            query = select(Liquidaciones)
            if self.search_value:
                search_value = f"%{self.search_value.lower()}%"
                query = query.where(
                    or_(
                        *[getattr(Liquidaciones, field).ilike(search_value)
                        for field in Liquidaciones.__fields__]
                    )
                )
            if self.sort_value:
                sort_column = getattr(Liquidaciones, self.sort_value)
                query = query.order_by(desc(sort_column) if self.sort_reverse else asc(sort_column))
            self.liquidaciones = session.exec(query).all()
            self.total_liquidacioness = len(self.liquidaciones)

    def add_liquidacion(self, form_data: dict):
        """Agrega una nueva liquidación a la base de datos."""
        self.current_liquidacion = form_data
        self.current_liquidacion["fecha"] = datetime.now(TZ).strftime("%Y/%m/%d %H:%M:%S")
        self.current_liquidacion["cod_id"] = f"C{self.current_liquidacion['chofer']}_M{self.current_liquidacion['movil']}_{self.current_liquidacion['fecha'][2:10]}"

        # Verificar recaudación para notificar
        recaudacion = self.current_liquidacion["recaudacion"]
        if recaudacion > 15000:
            send_email("Recaudación Alta", f"El chofer {self.current_liquidacion['chofer']} ha recaudado {recaudacion}.")
        elif recaudacion < 2000:
            send_email("Recaudación Baja", f"El chofer {self.current_liquidacion['chofer']} ha recaudado {recaudacion}.")

        # Guardar en la base de datos
        with rx.session(url="mysql+pymysql://<user>:<password>@<host>/defaultdb") as session:
            if session.exec(select(Liquidaciones).where(Liquidaciones.cod_id == self.current_liquidacion["cod_id"])).first():
                return rx.toast.info("Liquidación ya existente.", variant="outline", position="bottom-right")
            session.add(Liquidaciones(**self.current_liquidacion))
            session.commit()

        self.load_entries()


    def verifica_recaudacion(self, current_liquidacion):
        recaudacion = float(current_liquidacion["recaudacion"])
        if recaudacion > 15000:
            subject = "Recaudación Alta"
            body = f"El chofer {current_liquidacion['chofer']} ha realizado una recaudación de {recaudacion}."
            send_email(subject, body, to_email="mattbarbr@hotmail.com")
        elif recaudacion < 2000:
            subject = "Recaudación Baja"
            body = f"El chofer {current_liquidacion['chofer']} ha realizado una recaudación de {recaudacion}."
            send_email(subject, body, to_email="mattbarbr@hotmail.com")


    def calculos_to_db(self, current_liquidacion: dict):
        """Calcula los valores de las columnas a partir de los valores ingresados"""
        self.current_liquidacion["salario"] = float(self.current_liquidacion["recaudacion"]) * SALARIO
        self.current_liquidacion["gastos"] = float(self.current_liquidacion["salario"])+float(self.current_liquidacion["combustible"])+float(self.current_liquidacion["extras"])
        self.current_liquidacion["liquido"] = float(self.current_liquidacion["recaudacion"])-float(self.current_liquidacion["gastos"])
        self.current_liquidacion["aportes"] = float(self.current_liquidacion["salario"]) * APORTE
        self.current_liquidacion["sub_total"] = float(self.current_liquidacion["liquido"])+float(self.current_liquidacion["aportes"])
        self.current_liquidacion["entrega"] = float(self.current_liquidacion["sub_total"])-float(self.current_liquidacion["h13"])-float(self.current_liquidacion["credito"])
        return current_liquidacion


    def update_liquidacion_to_db(self, form_data: dict):
        """Actualizar una liquidacioón"""
        # Actualiza la información de la liquidación actual con los datos del formulario
        self.current_liquidacion.update(form_data)       
        # Realiza los cálculos adicionales necesarios para actualizar la liquidación
        self.current_liquidacion = self.calculos_to_db(self.current_liquidacion)

        # Establece una conexión con la base de datos usando Reflex
        with rx.session(url="mysql+pymysql://avnadmin:AVNS_0wDZLak0nK19kamQus8@dbliqudiaciones-admtaxi.b.aivencloud.com:16928/defaultdb?") as session:
            
            # Busca en la base de datos la liquidación existente que corresponde al código único `cod_id`
            liquidacion = session.exec(
                select(Liquidaciones).where(Liquidaciones.cod_id == self.current_liquidacion["cod_id"])
            ).first()
            # Actualiza los campos de la liquidación encontrada con los nuevos datos, excepto `cod_id`
            for field in Liquidaciones.get_fields():
                if field != "cod_id":
                    # Actualiza el campo `field` en el objeto `liquidacion` con el valor correspondiente de `self.current_liquidacion`
                    setattr(liquidacion, field, self.current_liquidacion[field])
            
            # Añade la liquidación actualizada de nuevo a la sesión para guardarla en la base de datos
            session.add(liquidacion)
            session.commit()  # Confirma los cambios en la base de datos
        # Recarga los registros de liquidaciones
        self.load_entries()
        
        # Muestra una notificación indicando que la liquidación fue modificada
        return rx.toast.info(f"Liquidacion {self.current_liquidacion['cod_id']} fue modificada.", variant="outline", position="bottom-right")


    def delete_liquidacion(self, cod_id: int):
        """Borrar una liquidación de la base de datos."""
        # Establece una conexión con la base de datos usando Reflex
        with rx.session(url="mysql+pymysql://avnadmin:AVNS_0wDZLak0nK19kamQus8@dbliqudiaciones-admtaxi.b.aivencloud.com:16928/defaultdb?") as session:
            
            # Busca la liquidación en la base de datos por su `cod_id`
            liquidacion = session.exec(select(Liquidaciones).where(Liquidaciones.cod_id == cod_id)).first()
            # Elimina la liquidación encontrada
            session.delete(liquidacion)
            # Confirma los cambios en la base de datos
            session.commit()  
        # Recarga los registros de liquidaciones
        self.load_entries()
        
        # Muestra una notificación indicando que la liquidación fue eliminada
        return rx.toast.info(f"Liquidación {liquidacion.cod_id} fue eliminada.", variant="outline", position="bottom-right")

