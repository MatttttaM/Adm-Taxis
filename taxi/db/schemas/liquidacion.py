

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