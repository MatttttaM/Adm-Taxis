import reflex as rx

from taxi.templates.template import template
from taxi.components.form_field import form_field
from taxi.backend.backend import State
from taxi.constants import COLOR_PRINCIPAL, Columna, Paginas


@template(route=Paginas.LIQUIDACION.value["url"],title=Paginas.LIQUIDACION.value["titulo"],description=Paginas.LIQUIDACION.value["desc"])
def liquidacion_page() -> rx.Component:
    """Botón '+ Add Liquidacion'"""
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
                    color_scheme=COLOR_PRINCIPAL,
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Agregar una nueva liquidacion",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Completa la información para crear una nueva liquidación",
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
                        form_field(
                            Columna.CHOFER.value["titulo"],
                            Columna.CHOFER.value["desc"],
                            Columna.CHOFER.value["type"],
                            Columna.CHOFER.value["var"],
                            Columna.CHOFER.value["icono"],
                        ),
                        form_field(
                            Columna.MOVIL.value["titulo"],
                            Columna.MOVIL.value["desc"],
                            Columna.MOVIL.value["type"],
                            Columna.MOVIL.value["var"],
                            Columna.MOVIL.value["icono"],
                        ),
                        form_field(
                            Columna.RECAUDACION.value["titulo"],
                            Columna.RECAUDACION.value["desc"],
                            Columna.RECAUDACION.value["type"],
                            Columna.RECAUDACION.value["var"],
                            Columna.RECAUDACION.value["icono"],
                        ),
                        form_field(
                            Columna.COMBUSTIBLE.value["titulo"],
                            Columna.COMBUSTIBLE.value["desc"],
                            Columna.COMBUSTIBLE.value["type"],
                            Columna.COMBUSTIBLE.value["var"],
                            Columna.COMBUSTIBLE.value["icono"],
                        ),
                        form_field(
                            Columna.EXTRAS.value["titulo"],
                            Columna.EXTRAS.value["desc"],
                            Columna.EXTRAS.value["type"],
                            Columna.EXTRAS.value["var"],
                            Columna.EXTRAS.value["icono"],
                        ),                
                        form_field(
                            Columna.H13.value["titulo"],
                            Columna.H13.value["desc"],
                            Columna.H13.value["type"],
                            Columna.H13.value["var"],
                            Columna.H13.value["icono"],
                        ),
                        form_field(
                            Columna.CREDITO.value["titulo"],
                            Columna.CREDITO.value["desc"],
                            Columna.CREDITO.value["type"],
                            Columna.CREDITO.value["var"],
                            Columna.CREDITO.value["icono"],
                        ),

                        # Estado
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("estado"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Entregada", "Pendiente", "Movil Parado"],
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
                                #color_scheme=COLOR_PRINCIPAL,
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
                        #justify="end",
                    ),
                    # LLama a la función add_liquidacion_to_db para cargar la liquidación
                    on_submit=State.add_liquidacion_to_db,
                    reset_on_submit=False,
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
    )
