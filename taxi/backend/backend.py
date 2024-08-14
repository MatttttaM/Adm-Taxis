import reflex as rx
from sqlalchemy import DECIMAL, INTEGER, VARCHAR
from sqlmodel import Field, select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta


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


class Liquidacion(rx.Model, table=True):
    """Modelo de Liquidacion"""
    id: int = Field(default=None, primary_key=True)
    movil: int
    recaudacion_total: int
    gastos: float
    salario: float
    viatico: float
    combustible: float
    extras: float
    liquido: float
    aportes: float
    sub_total: float
    h13: float
    credito: float
    status: str


class State(rx.State):
    """The app state."""

    liquidaciones: list[Liquidacion] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_liquidacion: Liquidacion = Liquidacion()
    # Values for current and previous month
    current_month_values: MonthValues = MonthValues()
    previous_month_values: MonthValues = MonthValues()


    def load_entries(self) -> list[Liquidacion]:
            """Get all users from the database."""
            with rx.session(url="mysql+pymysql://root:Admin@localhost:3306/taxidb") as session:
                query = select(Liquidacion)
                if self.search_value:
                    search_value = f"%{str(self.search_value).lower()}%"
                    query = query.where(
                        or_(
                            *[
                                getattr(Liquidacion, field).ilike(search_value)
                                for field in Liquidacion.__fields__
                                if field not in ["id"]
                            ],
                            # ensures that payments is cast to a string before applying the ilike operator
                            cast(Liquidacion.movil, String).ilike(search_value)
                        )
                    )

                if self.sort_value:
                    sort_column = getattr(Liquidacion, self.sort_value)
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

    def get_liquidacion(self, liquidacion: Liquidacion):
        self.current_liquidacion = liquidacion


    def add_customer_to_db(self, form_data: dict):
        self.current_liquidacion = form_data
        self.current_liquidacion["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with rx.session(url="mysql+pymysql://root:Admin@localhost:3306/taxidb") as session:
            if session.exec(
                select(Liquidacion).where(Liquidacion.movil == self.current_liquidacion["movil"])
            ).first():
                return rx.window_alert("Liquidacion con este movil already exists")
            session.add(Liquidacion(**self.current_liquidacion))
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Liquidación {self.current_liquidacion['id']} has been added.", variant="outline", position="bottom-right")


    def update_customer_to_db(self, form_data: dict):
        self.current_liquidacion.update(form_data)
        with rx.session(url="mysql+pymysql://root:Admin@localhost:3306/taxidb") as session:
            liquidacion = session.exec(
                select(Liquidacion).where(Liquidacion.id == self.current_liquidacion["id"])
            ).first()
            for field in Liquidacion.get_fields():
                if field != "id":
                    setattr(liquidacion, field, self.current_liquidacion[field])
            session.add(liquidacion)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Liquidacion {self.current_liquidacion['id']} has been modified.", variant="outline", position="bottom-right")


    def delete_customer(self, id: int):
        """Delete a customer from the database."""
        with rx.session(url="mysql+pymysql://root:Admin@localhost:3306/taxidb") as session:
            liquidacion = session.exec(select(Liquidacion).where(Liquidacion.id == id)).first()
            session.delete(liquidacion)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {liquidacion.id} has been deleted.", variant="outline", position="bottom-right")
    
    
    # @rx.var(cache=True)
    # def payments_change(self) -> float:
    #     return _get_percentage_change(self.current_month_values.total_payments, self.previous_month_values.total_payments)

    # @rx.var(cache=True)
    # def customers_change(self) -> float:
    #     return _get_percentage_change(self.current_month_values.num_customers, self.previous_month_values.num_customers)

    # @rx.var(cache=True)
    # def delivers_change(self) -> float:
    #     return _get_percentage_change(self.current_month_values.num_delivers, self.previous_month_values.num_delivers)
