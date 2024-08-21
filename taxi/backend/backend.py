from dataclasses import field
import reflex as rx
from sqlmodel import Field, select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta

from taxi.constants import APORTE



# def _get_percentage_change(value: Union[int, float], prev_value: Union[int, float]) -> float:
#     percentage_change = (
#         round(((value - prev_value) / prev_value) * 100, 2)
#         if prev_value != 0
#         else 0
#         if value == 0
#         else
#         float("inf")
#     )
#     return percentage_change

# class Customer(rx.Model, table=True):
#     """The customer model."""

#     name: str
#     email: str
#     phone: str
#     address: str
#     date: str
#     payments: float
#     status: str


class MonthValues(rx.Base):
    """Values for a month."""

    num_customers: int = 0
    total_payments: float = 0.0
    num_delivers: int = 0


class Liquidaciones(rx.Model, table=True):
    """Modelo de Liquidacion"""
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


class State(rx.State):
    """The app state."""

    liquidaciones: list[Liquidaciones] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_liquidacion: Liquidaciones = Liquidaciones()
    # Values for current and previous month
    current_month_values: MonthValues = MonthValues()
    previous_month_values: MonthValues = MonthValues()


    def load_entries(self) -> list[Liquidaciones]:
            """Get all recaudaciones from the database."""
            with rx.session(url="mysql+pymysql://avnadmin:AVNS_0wDZLak0nK19kamQus8@dbliqudiaciones-admtaxi.b.aivencloud.com:16928/defaultdb?") as session:
                query = select(Liquidaciones)
                if self.search_value:
                    search_value = f"%{str(self.search_value).lower()}%"
                    query = query.where(
                        or_(
                            *[
                                getattr(Liquidaciones, field).ilike(search_value)
                                for field in Liquidaciones.__fields__
                                if field not in ["chofer"]
                            ],
                            # ensures that movil is cast to a string before applying the ilike operator
                            cast(Liquidaciones.movil, String).ilike(search_value)
                        )
                    )

                if self.sort_value:
                    sort_column = getattr(Liquidaciones, self.sort_value)
                    order = desc(sort_column) if self.sort_reverse else asc(sort_column)
                    query = query.order_by(order)

                self.liquidaciones = session.exec(query).all()

    #         self.get_current_month_values()
    #         self.get_previous_month_values()


    # def get_current_month_values(self):
    #     """Calculate current month's values."""
    #     now = datetime.now()
    #     start_of_month = datetime(now.year, now.month, 1)
        
    #     current_month_users = [
    #         user for user in self.users if datetime.strptime(user.date, '%Y-%m-%d %H:%M:%S') >= start_of_month
    #     ]
    #     num_customers = len(current_month_users)
    #     total_payments = sum(user.payments for user in current_month_users)
    #     num_delivers = len([user for user in current_month_users if user.status == "Delivered"])
    #     self.current_month_values = MonthValues(num_customers=num_customers, total_payments=total_payments, num_delivers=num_delivers)


    # def get_previous_month_values(self):
    #     """Calculate previous month's values."""
    #     now = datetime.now()
    #     first_day_of_current_month = datetime(now.year, now.month, 1)
    #     last_day_of_last_month = first_day_of_current_month - timedelta(days=1)
    #     start_of_last_month = datetime(last_day_of_last_month.year, last_day_of_last_month.month, 1)
        
    #     previous_month_users = [
    #         user for user in self.users
    #         if start_of_last_month <= datetime.strptime(user.date, '%Y-%m-%d %H:%M:%S') <= last_day_of_last_month
    #     ]
    #     # We add some dummy values to simulate growth/decline. Remove them in production.
    #     num_customers = len(previous_month_users) + 3
    #     total_payments = sum(user.payments for user in previous_month_users) + 240
    #     num_delivers = len([user for user in previous_month_users if user.status == "Delivered"]) + 5
        
    #     self.previous_month_values = MonthValues(num_customers=num_customers, total_payments=total_payments, num_delivers=num_delivers)


    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

    def get_liquidacion(self, liquidacion: Liquidaciones):
        self.current_liquidacion = liquidacion


    ### Calculos y creación de valores a partir de los ingresado
    def add_customer_to_db(self, form_data: dict):
        self.current_liquidacion = form_data
        self.current_liquidacion["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_liquidacion["cod_id"] = "C"+str(self.current_liquidacion['chofer'])+"_"+"M"+str(self.current_liquidacion['movil'])+"_"+str(self.current_liquidacion['fecha'][2:10])
        self.current_liquidacion["salario"] = float(self.current_liquidacion["recaudacion"]) * 0.29
        self.current_liquidacion["gastos"] = float(self.current_liquidacion["salario"])+float(self.current_liquidacion["combustible"])+float(self.current_liquidacion["extras"])
        self.current_liquidacion["liquido"] = float(self.current_liquidacion["recaudacion"])-float(self.current_liquidacion["gastos"])
        self.current_liquidacion["aportes"] = float(self.current_liquidacion["salario"]) * APORTE
        self.current_liquidacion["sub_total"] = float(self.current_liquidacion["liquido"])+float(self.current_liquidacion["aportes"])
        self.current_liquidacion["entrega"] = float(self.current_liquidacion["sub_total"])-float(self.current_liquidacion["h13"])-float(self.current_liquidacion["credito"])

        with rx.session(url="mysql+pymysql://avnadmin:AVNS_0wDZLak0nK19kamQus8@dbliqudiaciones-admtaxi.b.aivencloud.com:16928/defaultdb?") as session:
            if session.exec(
                select(Liquidaciones).where(Liquidaciones.movil == self.current_liquidacion["movil"])
            ).first():
                return rx.window_alert("Liquidacion con este movil already exists")
            session.add(Liquidaciones(**self.current_liquidacion))
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Liquidación {self.current_liquidacion['chofer']} has been added.", variant="outline", position="bottom-right")


    def update_customer_to_db(self, form_data: dict):
        self.current_liquidacion.update(form_data)
        with rx.session(url="mysql+pymysql://avnadmin:AVNS_0wDZLak0nK19kamQus8@dbliqudiaciones-admtaxi.b.aivencloud.com:16928/defaultdb?") as session:
            liquidacion = session.exec(
                select(Liquidaciones).where(Liquidaciones.chofer == self.current_liquidacion["chofer"])
            ).first()
            for field in Liquidaciones.get_fields():
                if field != "chofer":
                    setattr(liquidacion, field, self.current_liquidacion[field])
            session.add(liquidacion)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Liquidacion {self.current_liquidacion['chofer']} has been modified.", variant="outline", position="bottom-right")


    def delete_customer(self, chofer: int):
        """Borrar una liquidación de la base de datos."""
        with rx.session(url="mysql+pymysql://avnadmin:AVNS_0wDZLak0nK19kamQus8@dbliqudiaciones-admtaxi.b.aivencloud.com:16928/defaultdb?") as session:
            liquidacion = session.exec(select(Liquidaciones).where(Liquidaciones.chofer == chofer)).first()
            session.delete(liquidacion)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {liquidacion.chofer} has been deleted.", variant="outline", position="bottom-right")
    
    

    # @rx.var(cache=True)
    # def payments_change(self) -> float:
    #     return _get_percentage_change(self.current_month_values.total_payments, self.previous_month_values.total_payments)

    # @rx.var(cache=True)
    # def customers_change(self) -> float:
    #     return _get_percentage_change(self.current_month_values.num_customers, self.previous_month_values.num_customers)

    # @rx.var(cache=True)
    # def delivers_change(self) -> float:
    #     return _get_percentage_change(self.current_month_values.num_delivers, self.previous_month_values.num_delivers)
