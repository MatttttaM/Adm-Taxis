import reflex as rx

from ..backend.backend_nuevo import Liquidaciones, TableState
from ..components.new.status_badge import status_badge
from ..components.form_field import form_field
from ..constants import COLOR_PRINCIPAL, Columna#, OPCIONES_FILTRO


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

def _pagination_view() -> rx.Component:
    """Pie de paginas"""
    return (
        rx.hstack(
            rx.text(
                "Page ",
                rx.code(TableState.page_number),
                f" of {TableState.total_pages}",
                justify="end",
            ),
            rx.hstack(
                rx.icon_button(
                    rx.icon("chevrons-left", size=18),
                    on_click=TableState.first_page,
                    opacity=rx.cond(TableState.page_number == 1, 0.6, 1),
                    color_scheme=rx.cond(TableState.page_number == 1, "gray", "accent"),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-left", size=18),
                    on_click=TableState.prev_page,
                    opacity=rx.cond(TableState.page_number == 1, 0.6, 1),
                    color_scheme=rx.cond(TableState.page_number == 1, "gray", "accent"),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-right", size=18),
                    on_click=TableState.next_page,
                    opacity=rx.cond(
                        TableState.page_number == TableState.total_pages, 0.6, 1
                    ),
                    color_scheme=rx.cond(
                        TableState.page_number == TableState.total_pages,
                        "gray",
                        "accent",
                    ),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevrons-right", size=18),
                    on_click=TableState.last_page,
                    opacity=rx.cond(
                        TableState.page_number == TableState.total_pages, 0.6, 1
                    ),
                    color_scheme=rx.cond(
                        TableState.page_number == TableState.total_pages,
                        "gray",
                        "accent",
                    ),
                    variant="soft",
                ),
                align="center",
                spacing="2",
                justify="end",
            ),
            spacing="5",
            margin_top="1em",
            align="center",
            width="100%",
            justify="end",
        ),
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
                on_click=lambda: TableState.get_liquidacion(liquidacion),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Editar Liquidación",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Editar o actualizar la liquidación",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    # Ventana que se abre para "Editar" una liquidación
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
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(rx.button("Cancelar",variant="soft")),
                        rx.form.submit(rx.dialog.close(rx.button("Actualizar liquidación")),as_child=True),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    # LLama a la función update_liquidacion_to_db para actualizar la liquidación
                    on_submit=TableState.update_liquidacion_to_db,
                    reset_on_submit=False,
                ),
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        max_width="450px",
        padding="1.5em",
    ),
    #                     # Botones de acción
    #                     rx.hstack(
    #                         rx.dialog.close(rx.button("Cancelar", variant="soft", color_scheme=COLOR_PRINCIPAL)),
    #                         rx.form.submit(rx.dialog.close(rx.button("Actualizar")), as_child=True),
    #                         spacing="3",
    #                     ),
    #                 ),
    #             on_submit=TableState.update_liquidacion_to_db,
    #             ),
    #         padding="1.5em",
    #         border=f"2px solid {rx.color(COLOR_PRINCIPAL, 7)}",
    #         border_radius="25px",
    #         ),
    #     max_width="450px",
    #     )
    # )

def main_table() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.flex(
                rx.cond(
                    TableState.sort_reverse,
                    rx.icon(
                        "arrow-down-z-a",
                        size=28,
                        stroke_width=1.5,
                        cursor="pointer",
                        flex_shrink="0",
                        on_click=TableState.toggle_sort,
                    ),
                    rx.icon(
                        "arrow-down-a-z",
                        size=28,
                        stroke_width=1.5,
                        cursor="pointer",
                        flex_shrink="0",
                        on_click=TableState.toggle_sort,
                    ),
                ),
                rx.select(
                    ["cod_id", "chofer", "movil", "recaudacion", "salario", "gastos", "fecha", "estado"],    # opciones
                    placeholder="Sort By: Name",
                    size="3",
                    on_change=TableState.set_sort_value,
                ),
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    rx.input.slot(
                        rx.icon("x"),
                        justify="end",
                        cursor="pointer",
                        on_click=TableState.setvar("search_value", ""),
                        display=rx.cond(TableState.search_value, "flex", "none"),
                    ),
                    value=TableState.search_value,
                    placeholder="Search here...",
                    size="3",
                    max_width=["150px", "150px", "200px", "250px"],
                    width="100%",
                    variant="surface",
                    color_scheme="gray",
                    on_change=TableState.set_search_value,
                ),
                align="center",
                justify="end",
                spacing="3",
            ),
            rx.button(
                rx.icon("arrow-down-to-line", size=20),
                "Export",
                size="3",
                variant="surface",
                display=["none", "none", "none", "flex"],
                on_click=rx.download(url="/items.csv"),
            ),
            spacing="3",
            justify="between",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        #     ### Agregar boton de ordenar de mayor a menor
        #     rx.flex(
        #         TableState.sort_reverse,
        #         rx.input(
        #             value=TableState.search_value,
        #             placeholder="Buscar...",
        #             size="3",
        #             variant="surface",
        #             on_change=TableState.toggle_sort,
        #         ),
        #         rx.select(OPCIONES_FILTRO),
        #         justify="end",
        #         align="center",
        #         spacing="3",
        #         wrap="wrap",
        #         width="100%",
        #         padding_bottom="1em",
        #     ),
        #     rx.flex(
        #         rx.cond(
        #             TableState.sort_reverse,
        #             rx.icon(
        #                 "arrow-down-z-a",
        #                 size=28,
        #                 stroke_width=1.5,
        #                 cursor="pointer",
        #                 flex_shrink="0",
        #                 on_click=TableState.toggle_sort,
        #             ),
        #             rx.icon(
        #                 "arrow-down-a-z",
        #                 size=28,
        #                 stroke_width=1.5,
        #                 cursor="pointer",
        #                 flex_shrink="0",
        #                 on_click=TableState.toggle_sort,
        #             ),
        #         ),
        #         rx.select(
        #             [
        #                 "name",
        #                 "payment",
        #                 "date",
        #                 "status",
        #             ],
        #             placeholder="Sort By: Name",
        #             size="3",
        #             on_change=TableState.set_sort_value,
        #         ),
        #         rx.input(
        #             rx.input.slot(rx.icon("search")),
        #             rx.input.slot(
        #                 rx.icon("x"),
        #                 justify="end",
        #                 cursor="pointer",
        #                 on_click=TableState.setvar("search_value", ""),
        #                 display=rx.cond(TableState.search_value, "flex", "none"),
        #             ),
        #             value=TableState.search_value,
        #             placeholder="Search here...",
        #             size="3",
        #             max_width=["150px", "150px", "200px", "250px"],
        #             width="100%",
        #             variant="surface",
        #             color_scheme="gray",
        #             on_change=TableState.set_search_value,
        #         ),
        #         align="center",
        #         justify="end",
        #         spacing="3",
        #     ),
        #     rx.button(
        #         rx.icon("arrow-down-to-line", size=20),
        #         "Export",
        #         size="3",
        #         variant="surface",
        #         display=["none", "none", "none", "flex"],
        #         on_click=rx.download(url="/items.csv"),
        #     ),
        #     spacing="3",
        #     justify="between",
        #     wrap="wrap",
        #     width="100%",
        #     padding_bottom="1em",
        # ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell(Columna.COD_ID.value["titulo"], Columna.COD_ID.value["icono"]),
                    _header_cell(Columna.CHOFER.value["titulo"], Columna.CHOFER.value["icono"]),
                    _header_cell(Columna.MOVIL.value["titulo"], Columna.MOVIL.value["icono"]),
                    _header_cell(Columna.RECAUDACION.value["titulo"], Columna.RECAUDACION.value["icono"]),
                    _header_cell(Columna.SALARIO.value["titulo"], Columna.SALARIO.value["icono"]),
                    _header_cell(Columna.COMBUSTIBLE.value["titulo"], Columna.COMBUSTIBLE.value["icono"]),
                    _header_cell(Columna.EXTRAS.value["titulo"], Columna.EXTRAS.value["icono"]),
                    _header_cell(Columna.GASTOS.value["titulo"], Columna.GASTOS.value["icono"]),
                    _header_cell(Columna.LIQUIDO.value["titulo"], Columna.LIQUIDO.value["icono"]),
                    _header_cell(Columna.APORTES.value["titulo"], Columna.APORTES.value["icono"]),
                    _header_cell(Columna.SUB_TOTAL.value["titulo"], Columna.SUB_TOTAL.value["icono"]),
                    _header_cell(Columna.H13.value["titulo"], Columna.H13.value["icono"]),
                    _header_cell(Columna.CREDITO.value["titulo"], Columna.CREDITO.value["icono"]),
                    _header_cell(Columna.ENTREGA.value["titulo"], Columna.ENTREGA.value["icono"]),
                    _header_cell(Columna.FECHA.value["titulo"], Columna.FECHA.value["icono"]),
                    _header_cell(Columna.ESTADO.value["titulo"], Columna.CHOFER.value["icono"]),
                    _header_cell(Columna.ACCION.value["titulo"], Columna.ACCION.value["icono"]),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    TableState.get_current_page,
                    lambda liquidacion, index: _show_liquidacion(liquidacion, index)
                ),
            ),
            variant="surface",
            size="3",
            width="100%",
            on_mount=TableState.load_entries
        ),
        _pagination_view(),
        width="100%",
    )