import reflex as rx

from ..backend.backend_nuevo import Liquidaciones
from ..views.new.table import _pagination_view
from ..backend.backend_nuevo import TableState
from ..components.new.status_badge import status_badge
from ..components.form_field import form_field
from ..constants import COLOR_PRINCIPAL, Columna


def _header_cell(text: str, icon: str) -> rx.Component:
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def _show_liquidacion(liquidacion: Liquidaciones, index: int) -> rx.Component:
    bg_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 1),
        rx.color("accent", 2),
    )
    hover_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 3),
        rx.color("accent", 3),
    )
    return rx.table.row(
        rx.table.cell(liquidacion.cod_id),
        rx.table.cell(liquidacion.chofer),
        rx.table.cell(liquidacion.movil),
        rx.table.cell(liquidacion.recaudacion),
        rx.table.cell(liquidacion.salario),
        rx.table.cell(liquidacion.combustible),
        rx.table.cell(liquidacion.extras),
        rx.table.cell(liquidacion.gastos),
        rx.table.cell(liquidacion.liquido),
        rx.table.cell(liquidacion.aportes),
        rx.table.cell(liquidacion.sub_total),
        rx.table.cell(liquidacion.h13),
        rx.table.cell(liquidacion.credito),
        rx.table.cell(liquidacion.entrega),
        rx.table.cell(liquidacion.fecha),
        rx.table.cell(status_badge(liquidacion.estado)),
        # Acciones: Editar y Eliminar
        rx.table.cell(
            rx.hstack(
                update_liquidacion_dialog(liquidacion),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: TableState.delete_liquidacion(liquidacion.cod_id),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": hover_color}, "bg": bg_color},
        align="center",
    )


# Función para el diálogo de edición
def update_liquidacion_dialog(liquidacion: Liquidaciones):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Editar", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
            ),
        ),
        rx.dialog.content(
            rx.form.root(
                rx.flex(
                    form_field(
                        Columna.RECAUDACION.value["titulo"],
                        Columna.RECAUDACION.value["desc"],
                        Columna.RECAUDACION.value["type"],
                        Columna.RECAUDACION.value["var"],
                        Columna.RECAUDACION.value["icono"],
                        liquidacion.recaudacion.to(str),
                    ),
                    form_field(
                        Columna.COMBUSTIBLE.value["titulo"],
                        Columna.COMBUSTIBLE.value["desc"],
                        Columna.COMBUSTIBLE.value["type"],
                        Columna.COMBUSTIBLE.value["var"],
                        Columna.COMBUSTIBLE.value["icono"],
                        liquidacion.combustible.to(str),
                    ),
                    form_field(
                        Columna.EXTRAS.value["titulo"],
                        Columna.EXTRAS.value["desc"],
                        Columna.EXTRAS.value["type"],
                        Columna.EXTRAS.value["var"],
                        Columna.EXTRAS.value["icono"],
                        liquidacion.extras.to(str),
                    ),                
                    form_field(
                        Columna.H13.value["titulo"],
                        Columna.H13.value["desc"],
                        Columna.H13.value["type"],
                        Columna.H13.value["var"],
                        Columna.H13.value["icono"],
                        liquidacion.h13.to(str),
                    ),
                    form_field(
                        Columna.CREDITO.value["titulo"],
                        Columna.CREDITO.value["desc"],
                        Columna.CREDITO.value["type"],
                        Columna.CREDITO.value["var"],
                        Columna.CREDITO.value["icono"],
                        liquidacion.credito.to(str),
                    ),
                    form_field(
                        Columna.FECHA.value["titulo"],
                        Columna.FECHA.value["desc"],
                        Columna.FECHA.value["type"],
                        Columna.FECHA.value["var"],
                        Columna.FECHA.value["icono"],
                        liquidacion.fecha.to(str),
                    ),
                    # Estado
                    rx.vstack(
                        rx.hstack(
                            rx.icon("truck", size=16, stroke_width=1.5),
                            rx.text("Estado"),
                            align="center",
                            spacing="2",
                        ),
                        rx.radio(
                            ["Entregada", "Pendiente", "Movil Parado"],
                            default_value=liquidacion.estado,
                            name="estado",
                            direction="row",
                            as_child=True,
                            required=True,
                        ),
                    ),
                    # Botones de acción
                    rx.hstack(
                        rx.dialog.close(rx.button("Cancelar", variant="soft", color_scheme=COLOR_PRINCIPAL)),
                        rx.form.submit(rx.dialog.close(rx.button("Actualizar")), as_child=True),
                        spacing="3",
                    ),
                ),
                on_submit=TableState.update_liquidacion_to_db,
            ),
            padding="1.5em",
            border=f"2px solid {rx.color(COLOR_PRINCIPAL, 7)}",
            border_radius="25px",
        ),
        max_width="450px",
    )


def main_table() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.input(
                rx.input.slot(rx.icon("search")),
                value=TableState.search_value,
                placeholder="Buscar...",
                size="3",
                variant="surface",
                on_change=TableState.set_search_value,
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Código", "user"),
                    _header_cell("Chofer", "user"),
                    _header_cell("Movil", "user"),
                    _header_cell("Recaudación", "user"),
                    _header_cell("Fecha", "user"),
                    _header_cell("Estado", "user"),
                    _header_cell("Acciones", "user"),
                ),
            ),
            rx.table.body(
                rx.foreach(TableState.get_current_page, _show_liquidacion)
            ),
            variant="surface",
            size="3",
            width="100%",
        ),
        _pagination_view(),
        width="100%",
    )
