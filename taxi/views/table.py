import reflex as rx
from ..backend.backend import Liquidacion, State, Liquidacion
from ..components.form_field import form_field
from ..components.status_badges import status_badge


def show_customer(liquidacion: Liquidacion):
    """Show a customer in a table row."""

    return rx.table.row(
        rx.table.cell(liquidacion.id),
        rx.table.cell(liquidacion.movil),
        rx.table.cell(liquidacion.recaudacion_total),
        rx.table.cell(liquidacion.gastos),
        rx.table.cell(liquidacion.salario),
        rx.table.cell(liquidacion.combustible),
        rx.table.cell(liquidacion.extras),
        rx.table.cell(liquidacion.liquido),
        rx.table.cell(liquidacion.h13),
        rx.table.cell(liquidacion.credito),
        rx.table.cell(
            rx.match(
                liquidacion.status,
                ("Delivered", status_badge("Delivered")),
                ("Pending", status_badge("Pending")),
                ("Cancelled", status_badge("Cancelled")),
                status_badge("Pending"),
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
                            "recaudacion_total",
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
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Delivered", "Pending", "Cancelled"],
                                name="status",
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
                    rx.flex(
                        # Número de chofer
                        form_field(
                            "id",
                            "Número de chofer",
                            "text",
                            "name",
                            "user",
                            str(liquidacion.id),
                        ),
                        # Email
                        form_field(
                            "Email",
                            "user@reflex.dev",
                            "email",
                            "email",
                            "mail",
                            str(liquidacion.movil),
                            # user.email,
                        ),
                        # Phone
                        form_field(
                            "Phone",
                            "Customer Phone",
                            "tel",
                            "phone",
                            "phone",
                            str(liquidacion.recaudacion_total),
                            # user.phone,
                        ),
                        # Address
                        form_field(
                            "Address",
                            "Customer Address",
                            "text",
                            "address",
                            "home",
                            str(liquidacion.gastos),
                            # user.address,
                        ),
                        # Payments
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "payments",
                            "dollar-sign",
                            # user.payments.to(str),        
                        ),                
                        # otro
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "payments",
                            "dollar-sign",
                            str(liquidacion.combustible),
                        ),
                        # otro
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "payments",
                            "dollar-sign",
                            str(liquidacion.extras),
                        ),
                        # otro
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "payments",
                            "dollar-sign",
                            str(liquidacion.liquido),
                        ),
                        # otro
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "payments",
                            "dollar-sign",
                            str(liquidacion.h13),
                        ),
                        # otro
                        form_field(
                            "Payment ($)",
                            "Customer Payment",
                            "number",
                            "payments",
                            "dollar-sign",
                            str(liquidacion.credito),
                        ),

                        # Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Delivered", "Pending", "Cancelled"],
                                default_value=liquidacion.status,
                                name="status",
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
                ["id", "movil", "recaudacion_total", "salario", "gastos", "date", "status"],    # opciones
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
                    _header_cell("id", "user"),
                    _header_cell("Móvil", "car-taxi-front"),
                    _header_cell("Recaudación Total", "dollar-sign"),
                    _header_cell("Salario", "dollar-sign"),
                    _header_cell("Combustible", "fuel"),
                    _header_cell("Extras", "dollar-sign"),
                    _header_cell("Gastos", "dollar-sign"),
                    _header_cell("Líquido", "dollar-sign"),
                    _header_cell("H13", "dollar-sign"),
                    _header_cell("Crédito", "dollar-sign"),
                    _header_cell("Date", "calendar"),
                    _header_cell("Status", "truck"),
                    _header_cell("Actions", "cog"),
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
