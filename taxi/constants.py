from enum import Enum


class Encabezado(Enum):
    COD_ID = {"var": "cod_id", "titulo": "Código", "icono": "scan-barcode", "desc": "Código de Liquidación", "type": "string"}
    CHOFER = {"var": "chofer", "titulo": "Chófer", "icono": "user", "desc": "Número de Chofer", "type": "number"}
    MOVIL = {"var": "movil", "titulo": "Móvil", "icono": "car-taxi-front", "desc": "STX0000", "type": "number"}
    RECAUDACION = {"var": "recaudacion", "titulo": "Recaudación", "icono": "dollar-sign", "desc": "Monto de la Recaudación", "type": "number"}
    SALARIO = {"var": "salario", "titulo": "Salario", "icono": "dollar-sign", "desc": "", "type": "number"}
    COMBUSTIBLE = {"var": "combustible", "titulo": "Combustible", "icono": "fuel", "desc": "Combustible ingresado", "type": "number"}
    EXTRAS = {"var": "extras", "titulo": "Extras", "icono": "dollar-sign", "desc": "Lavado, gomería, etc", "type": "number"}
    GASTOS = {"var": "gastos", "titulo": "Gastos", "icono": "dollar-sign", "desc": "", "type": "number"}
    LIQUIDO = {"var": "liquido", "titulo": "Líquido", "icono": "dollar-sign", "desc": "", "type": "number"}
    H13 = {"var": "h13", "titulo": "H13", "icono": "qr-code", "desc": "Total de H13", "type": "number"}
    CREDITO = {"var": "credito", "titulo": "Crédito", "icono": "credit-card", "desc": "Total tarjetas de Credito", "type": "number"}
    ENTREGA = {"var": "entrega", "titulo": "Entrega", "icono": "hand-coins", "desc": "", "type": "number"}
    FECHA = {"var": "fecha", "titulo": "Fecha", "icono": "calendar", "desc": "día/mes/año", "type": ""}
    ESTADO = {"var": "estado", "titulo": "Estado", "icono": "truck", "desc": "", "type": "text", }
    ACCION = {"var": "", "titulo": "Acción", "icono": "cog", "desc": "", "type": ""}


["Entregada", "Pendiente", "Movil parado"]

APORTE = 0.19


DB_URL = "mysql+pymysql://avnadmin:AVNS_0wDZLak0nK19kamQus8@dbliqudiaciones-admtaxi.b.aivencloud.com:16928/defaultdb?"


# print(Encabezado.CHOFER.value["titulo"], Encabezado.CHOFER.value["icono"])

# form_field(
#     Encabezado.CHOFER.value["titulo"],
#     Encabezado.CHOFER.value["desc"],
#     Encabezado.CHOFER.value["type"],
#     Encabezado.CHOFER.value["var"],
#     Encabezado.CHOFER.value["icono"],
# ),
# form_field(
#     Encabezado.MOVIL.value["titulo"],
#     Encabezado.MOVIL.value["desc"],
#     Encabezado.MOVIL.value["type"],
#     Encabezado.MOVIL.value["var"],
#     Encabezado.MOVIL.value["icono"],
# ),
# form_field(
#     Encabezado.RECAUDACION.value["titulo"],
#     Encabezado.RECAUDACION.value["desc"],
#     Encabezado.RECAUDACION.value["type"],
#     Encabezado.RECAUDACION.value["var"],
#     Encabezado.RECAUDACION.value["icono"],
# ),
# form_field(
#     Encabezado.COMBUSTIBLE.value["titulo"],
#     Encabezado.COMBUSTIBLE.value["desc"],
#     Encabezado.COMBUSTIBLE.value["type"],
#     Encabezado.COMBUSTIBLE.value["var"],
#     Encabezado.COMBUSTIBLE.value["icono"],
# ),
# form_field(
#     Encabezado.EXTRAS.value["titulo"],
#     Encabezado.EXTRAS.value["desc"],
#     Encabezado.EXTRAS.value["type"],
#     Encabezado.EXTRAS.value["var"],
#     Encabezado.EXTRAS.value["icono"],
# ),                
# form_field(
#     Encabezado.H13.value["titulo"],
#     Encabezado.H13.value["desc"],
#     Encabezado.H13.value["type"],
#     Encabezado.H13.value["var"],
#     Encabezado.H13.value["icono"],
# ),
# form_field(
#     Encabezado.CREDITO.value["titulo"],
#     Encabezado.CREDITO.value["desc"],
#     Encabezado.CREDITO.value["type"],
#     Encabezado.CREDITO.value["var"],
#     Encabezado.CREDITO.value["icono"],
# ),
# form_field(
#     Encabezado.FECHA.value["titulo"],
#     Encabezado.FECHA.value["desc"],
#     Encabezado.FECHA.value["type"],
#     Encabezado.FECHA.value["var"],
#     Encabezado.FECHA.value["icono"],
# )


# _header_cell(Encabezado.CHOFER.value["titulo"], Encabezado.CHOFER.value["icono"]),
# _header_cell(Encabezado.MOVIL.value["titulo"], Encabezado.MOVIL.value["icono"]),
# _header_cell(Encabezado.RECAUDACION.value["titulo"], Encabezado.RECAUDACION.value["icono"]),
# _header_cell(Encabezado.SALARIO.value["titulo"], Encabezado.SALARIO.value["icono"]),
# _header_cell(Encabezado.COMBUSTIBLE.value["titulo"], Encabezado.COMBUSTIBLE.value["icono"]),
# _header_cell(Encabezado.EXTRAS.value["titulo"], Encabezado.EXTRAS.value["icono"]),
# _header_cell(Encabezado.GASTOS.value["titulo"], Encabezado.GASTOS.value["icono"]),
# _header_cell(Encabezado.LIQUIDO.value["titulo"], Encabezado.LIQUIDO.value["icono"]),
# _header_cell(Encabezado.H13.value["titulo"], Encabezado.H13.value["icono"]),
# _header_cell(Encabezado.CREDITO.value["titulo"], Encabezado.CREDITO.value["icono"]),
# _header_cell(Encabezado.ENTREGA.value["titulo"], Encabezado.ENTREGA.value["icono"]),
# _header_cell(Encabezado.FECHA.value["titulo"], Encabezado.FECHA.value["icono"]),
# _header_cell(Encabezado.ESTADO.value["titulo"], Encabezado.CHOFER.value["icono"]),
# _header_cell(Encabezado.ACCION.value["titulo"], Encabezado.ACCION.value["icono"]),
