

def liquidacion_schema(liquidacion) -> dict:
    return {
        "id": str(liquidacion["id"]),
        "movil": liquidacion["movil"],
        "recaudacion_total": liquidacion["recaudacion_total"],
        "salario": int(liquidacion["recaudacion_total"]) * 0.29,
        "combustible": liquidacion["combustible"],
        "extras": liquidacion["extras"],
        "gastos": int(liquidacion["salario"]) + int(liquidacion["combustible"]) + int(liquidacion["extras"]),
        "liquido": int(liquidacion["recaudacion_total"]) - int(liquidacion["gastos"]),
        "h13": liquidacion["h13"],
        "credito": liquidacion["credito"],
        "fecha": "fecha"
    }


def liquidaciones_schema(liquidaciones) -> list:
    return [liquidacion_schema(liquidacion) for liquidacion in liquidaciones]


# _header_cell("id", "user"),
# _header_cell("Móvil", "user"),
# _header_cell("Recaudación Total", "dollar-sign"),
# _header_cell("Salario", "dollar-sign"),
# _header_cell("Combustible", "dollar-sign"),
# _header_cell("Extras", "dollar-sign"),
# _header_cell("Gastos", "dollar-sign"),
# _header_cell("Líquido", "dollar-sign"),
# _header_cell("H13", "dollar-sign"),
# _header_cell("Crédito", "dollar-sign"),
# _header_cell("Date", "calendar"),
# _header_cell("Status", "truck"),
# _header_cell("Actions", "cog"),