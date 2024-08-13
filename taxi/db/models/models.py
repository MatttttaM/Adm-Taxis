import datetime
from pydantic import BaseModel


# Entidad Chofer
class Chofer(BaseModel):
    id: str | None
    nombre: str
    email: str



# Entidad Liquidacion
class Liquidacion(BaseModel):
    id: str | None
    movil: int
    total: int
    gastos: int
    salario: int
    viatico: int
    combustible: int
    extras: int
    liquido: int
    aportes: int
    sub_total: int
    h13: int
    credito: int
