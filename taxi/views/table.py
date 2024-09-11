import reflex as rx

from ..constants import COLOR_PRINCIPAL, Columna
from ..backend.backend import Liquidaciones, State
from ..components.form_field import form_field
from ..components.estado_badges import estado_badge


def show_liquidacion(liquidacion: Liquidaciones):
    """Ver las liquidaciones en una tabla."""

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
        rx.table.cell(
            rx.match(
                liquidacion.estado,
                ("Entregada", estado_badge("Entregada")),
                ("Pendiente", estado_badge("Pendiente")),
                ("Movil Parado", estado_badge("Movil Parado")),
                estado_badge("Pendingggggg"),
            )
        ),
        rx.table.cell(
            rx.hstack(
                update_liquidacion_dialog(liquidacion),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_liquidacion(getattr(liquidacion, "cod_id")),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )


# Botón de "Editar" una liquidación
def update_liquidacion_dialog(liquidacion):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Editar", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
                on_click=lambda: State.get_liquidacion(liquidacion),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme=COLOR_PRINCIPAL,
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
                        # ESTADO
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("estado"),
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
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme=COLOR_PRINCIPAL,
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Actualizar liquidación"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    # LLama a la función update_liquidacion_to_db para actualizar la liquidación
                    on_submit=State.update_liquidacion_to_db,
                    reset_on_submit=False,
                ),
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        max_width="450px",
        padding="1.5em",
        border=f"2px solid {rx.color(COLOR_PRINCIPAL, 7)}",
        border_radius="25px",
    ),


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def main_table():
    return rx.fragment(
        # Primera línea de objetos
        rx.flex(
            # Botón de añadir liquidación
            ### add_liquidacion_button(),   ### Boton extraido a una pagina independiente
            rx.spacer(),
            # Botón para ordenar
            rx.cond(
                State.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
            ),
            # Botón para ordenar según las opciones
            rx.select(
                ["cod_id", "chofer", "movil", "recaudacion", "salario", "gastos", "fecha", "estado"],    # opciones
                placeholder="Sort By: Name",
                size="3",
                on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            # Botón para buscar
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Buscar...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: State.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        # Tabla principal
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
            # Muestra los datos de la tabla
            rx.table.body(rx.foreach(State.liquidaciones, show_liquidacion)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
    )
