from enum import Enum


class Encabezado(Enum):
    CHOFER = {"var": "id", "titulo": "Chófer", "icono": "user", "desc": "Número de Chofer", "type": "number"}
    MOVIL = {"var": "movil", "titulo": "Móvil", "icono": "car-taxi-front", "desc": "Número de Móvil", "type": "number"}
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


# print(Encabezado.CHOFER.value["titulo"])


# print(Encabezado.CHOFER.value["titulo"], Encabezado.CHOFER.value["icono"])




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