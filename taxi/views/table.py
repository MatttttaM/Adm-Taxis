import reflex as rx

from taxi.constants import Encabezado
from ..backend.backend import Liquidacion, State, Liquidacion
from ..components.form_field import form_field
from ..components.estado_badges import estado_badge


def show_customer(liquidacion: Liquidacion):
    """Show a customer in a table row."""

    return rx.table.row(
        rx.table.cell(liquidacion.id),
        rx.table.cell(liquidacion.movil),
        rx.table.cell(liquidacion.recaudacion),
        rx.table.cell(liquidacion.salario),
        rx.table.cell(liquidacion.combustible),
        rx.table.cell(liquidacion.extras),
        rx.table.cell(liquidacion.gastos),
        rx.table.cell(liquidacion.liquido),
        rx.table.cell(liquidacion.h13),
        rx.table.cell(liquidacion.credito),
        rx.table.cell(liquidacion.entrega),
        rx.table.cell(liquidacion.fecha),
        rx.table.cell(
            rx.match(
                liquidacion.estado,
                ("Delivered", estado_badge("Delivered")),
                ("Pending", estado_badge("Pending")),
                ("Cancelled", estado_badge("Cancelled")),
                estado_badge("Pending"),
            )
        ),
        rx.table.cell(
            rx.hstack(
                update_customer_dialog(liquidacion),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_customer(getattr(liquidacion, "id")),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )


### Botón "+ Add Liquidacion"
def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add Liquidacion", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="users", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Add New Customer",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Fill the form with the customer's info",
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
                    ### Ventana que se abré en el boton "+ Add Liquidacion"
                    rx.flex(
                        # ID
                        form_field(
                            "id",
                            "Customer Name",
                            "number",
                            "id",
                            "user",
                        ),
                        # Email
                        form_field(
                            "Email",
                            "user@reflex.dev",
                            "number",
                            "movil",
                            "mail",
                        ),
                        # Phone
                        form_field(
                            "Phone",
                            "Customer Phone",
                            "number",
                            "recaudacion",
                            "phone",
                        ),
                        # otro
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "combustible",
                            "dollar-sign",
                        ),
                        # otro
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "extras",
                            "dollar-sign",
                        ),
                        # otro
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "h13",
                            "dollar-sign",
                        ),
                        # otro
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "credito",
                            "dollar-sign",
                        ),


                    # rx.flex(
                    #     # Name
                    #     form_field(
                    #         "Nombre",
                    #         "Customer Name",
                    #         "text",
                    #         "name",
                    #         "user",
                    #     ),
                    #     # Email
                    #     form_field(
                    #         "Email", "user@reflex.dev", "email", "email", "mail"
                    #     ),
                    #     # Phone
                    #     form_field("Phone", "Customer Phone", "tel", "phone", "phone"),
                    #     # Address
                    #     form_field(
                    #         "Address",
                    #         "Customer Address",
                    #         "text",
                    #         "address",
                    #         "home"
                    #     ),
                    #     # Payments
                    #     form_field(
                    #         "Payment ($)",
                    #         "Customer Payment",
                    #         "number",
                    #         "Total",
                    #         "dollar-sign",
                    #     ),

                        # Estado
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("estado"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Delivered", "Pending", "Cancelled"],
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
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Cargar liquidaciónr"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    ### LLama a la función add_customer_to_db para cargar la liquidación
                    on_submit=State.add_customer_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


### Botón de "Editar" una liquidación
def update_customer_dialog(liquidacion):
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
                    color_scheme="grass",
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
                    ### Ventana que se abre para "Editar" una liquidación
                    rx.flex(
                        form_field(
                            Encabezado.CHOFER.value["titulo"],
                            Encabezado.CHOFER.value["desc"],
                            Encabezado.CHOFER.value["type"],
                            Encabezado.CHOFER.value["var"],
                            Encabezado.CHOFER.value["icono"],
                            # str(liquidacion.id),
                        ),
                        form_field(
                            Encabezado.MOVIL.value["titulo"],
                            Encabezado.MOVIL.value["desc"],
                            Encabezado.MOVIL.value["type"],
                            Encabezado.MOVIL.value["var"],
                            Encabezado.MOVIL.value["icono"],
                            # str(liquidacion.movil),
                            # user.email,
                        ),
                        form_field(
                            Encabezado.RECAUDACION.value["titulo"],
                            Encabezado.RECAUDACION.value["desc"],
                            Encabezado.RECAUDACION.value["type"],
                            Encabezado.RECAUDACION.value["var"],
                            Encabezado.RECAUDACION.value["icono"],
                            # str(liquidacion.recaudacion),
                            # user.phone,
                        ),
                        form_field(
                            Encabezado.COMBUSTIBLE.value["titulo"],
                            Encabezado.COMBUSTIBLE.value["desc"],
                            Encabezado.COMBUSTIBLE.value["type"],
                            Encabezado.COMBUSTIBLE.value["var"],
                            Encabezado.COMBUSTIBLE.value["icono"],
                            #str(liquidacion.combustible),
                            # str(liquidacion.gastos),
                            # user.address,
                        ),
                        form_field(
                            Encabezado.EXTRAS.value["titulo"],
                            Encabezado.EXTRAS.value["desc"],
                            Encabezado.EXTRAS.value["type"],
                            Encabezado.EXTRAS.value["var"],
                            Encabezado.EXTRAS.value["icono"],
                            # # user.payments.to(str),        
                        ),                
                        form_field(
                            Encabezado.H13.value["titulo"],
                            Encabezado.H13.value["desc"],
                            Encabezado.H13.value["type"],
                            Encabezado.H13.value["var"],
                            Encabezado.H13.value["icono"],
                            # str(liquidacion.combustible),
                        ),
                        form_field(
                            Encabezado.CREDITO.value["titulo"],
                            Encabezado.CREDITO.value["desc"],
                            Encabezado.CREDITO.value["type"],
                            Encabezado.CREDITO.value["var"],
                            Encabezado.CREDITO.value["icono"],
                            # str(liquidacion.extras),
                        ),
                        form_field(
                            Encabezado.FECHA.value["titulo"],
                            Encabezado.FECHA.value["desc"],
                            Encabezado.FECHA.value["type"],
                            Encabezado.FECHA.value["var"],
                            Encabezado.FECHA.value["icono"],
                            # str(liquidacion.liquido),
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
                                ["Entregada", "Pendiente", "Movil parado"],
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
                                color_scheme="gray",
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
                    ### LLama a la función update_customer_to_db para actualizar la liquidación
                    on_submit=State.update_customer_to_db,
                    reset_on_submit=False,
                ),
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        max_width="450px",
        padding="1.5em",
        border=f"2px solid {rx.color('accent', 7)}",
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
        ### Primera línea de objetos
        rx.flex(
            ### Botón de añadir liquidación
            add_customer_button(),
            rx.spacer(),
            ### Botón para ordenar
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
            ### Botón para ordenar según las opciones
            rx.select(
                ["id", "movil", "recaudacion", "salario", "gastos", "date", "estado"],    # opciones
                placeholder="Sort By: Name",
                size="3",
                on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            ### Botón para buscar
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
        ### Tabla principal
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell(Encabezado.CHOFER.value["titulo"], Encabezado.CHOFER.value["icono"]),
                    _header_cell(Encabezado.MOVIL.value["titulo"], Encabezado.MOVIL.value["icono"]),
                    _header_cell(Encabezado.RECAUDACION.value["titulo"], Encabezado.RECAUDACION.value["icono"]),
                    _header_cell(Encabezado.SALARIO.value["titulo"], Encabezado.SALARIO.value["icono"]),
                    _header_cell(Encabezado.COMBUSTIBLE.value["titulo"], Encabezado.COMBUSTIBLE.value["icono"]),
                    _header_cell(Encabezado.EXTRAS.value["titulo"], Encabezado.EXTRAS.value["icono"]),
                    _header_cell(Encabezado.GASTOS.value["titulo"], Encabezado.GASTOS.value["icono"]),
                    _header_cell(Encabezado.LIQUIDO.value["titulo"], Encabezado.LIQUIDO.value["icono"]),
                    _header_cell(Encabezado.H13.value["titulo"], Encabezado.H13.value["icono"]),
                    _header_cell(Encabezado.CREDITO.value["titulo"], Encabezado.CREDITO.value["icono"]),
                    _header_cell(Encabezado.ENTREGA.value["titulo"], Encabezado.ENTREGA.value["icono"]),
                    _header_cell(Encabezado.FECHA.value["titulo"], Encabezado.FECHA.value["icono"]),
                    _header_cell(Encabezado.ESTADO.value["titulo"], Encabezado.CHOFER.value["icono"]),
                    _header_cell(Encabezado.ACCION.value["titulo"], Encabezado.ACCION.value["icono"]),
                ),
            ),
            ### Muestra los datos de la tabla
            rx.table.body(rx.foreach(State.liquidaciones, show_customer)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
    )
