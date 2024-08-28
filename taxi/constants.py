from enum import Enum
import pytz

class Encabezado(Enum):
    COD_ID = {"var": "cod_id", "titulo": "Código", "icono": "scan-barcode", "desc": "Código de Liquidación", "type": "string"}
    CHOFER = {"var": "chofer", "titulo": "Chofer", "icono": "user", "desc": "Número de Chofer", "type": "number"}
    MOVIL = {"var": "movil", "titulo": "Móvil", "icono": "car-taxi-front", "desc": "STX0000", "type": "number"}
    RECAUDACION = {"var": "recaudacion", "titulo": "Recaudación", "icono": "dollar-sign", "desc": "Monto de la Recaudación", "type": "number"}
    SALARIO = {"var": "salario", "titulo": "Salario", "icono": "dollar-sign", "desc": "", "type": "number"}
    COMBUSTIBLE = {"var": "combustible", "titulo": "Combustible", "icono": "fuel", "desc": "Combustible ingresado", "type": "number"}
    EXTRAS = {"var": "extras", "titulo": "Extras", "icono": "dollar-sign", "desc": "Lavado, gomería, etc", "type": "number"}
    GASTOS = {"var": "gastos", "titulo": "Gastos", "icono": "dollar-sign", "desc": "", "type": "number"}
    LIQUIDO = {"var": "liquido", "titulo": "Líquido", "icono": "dollar-sign", "desc": "", "type": "number"}
    APORTES = {"var": "aportes", "titulo": "Aportes", "icono": "circle-percent", "desc": "", "type": "number"}
    SUB_TOTAL = {"var": "sub_total", "titulo": "Sub Total", "icono": "circle-equal", "desc": "", "type": "number"}
    H13 = {"var": "h13", "titulo": "H13", "icono": "qr-code", "desc": "Total de H13", "type": "number"}
    CREDITO = {"var": "credito", "titulo": "Crédito", "icono": "credit-card", "desc": "Total tarjetas de Credito", "type": "number"}
    ENTREGA = {"var": "entrega", "titulo": "Entrega", "icono": "hand-coins", "desc": "", "type": "number"}
    FECHA = {"var": "fecha", "titulo": "Fecha", "icono": "calendar", "desc": "día/mes/año", "type": ""}
    ESTADO = {"var": "estado", "titulo": "Estado", "icono": "truck", "desc": "", "type": "text", }
    ACCION = {"var": "", "titulo": "Acción", "icono": "cog", "desc": "", "type": ""}


["Entregada", "Pendiente", "Movil parado"]

APORTE = 0.19
SALARIO = 0.29

DB_URL = "mysql+pymysql://avnadmin:AVNS_0wDZLak0nK19kamQus8@dbliqudiaciones-admtaxi.b.aivencloud.com:16928/defaultdb?"


# Obtener la zona horaria de Montevideo
TZ = pytz.timezone('America/Montevideo')