"""Pagina de Gastos"""
import reflex as rx

from taxi.constants import Paginas
from taxi.templates.template import template


@template(route=Paginas.GASTOS.value["url"],title=Paginas.GASTOS.value["titulo"],description=Paginas.GASTOS.value["desc"])
def gastos_page() -> rx.Component:
    return rx.text("Pagina de Gastos")