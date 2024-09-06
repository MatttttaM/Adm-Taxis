import reflex as rx
from taxi.templates.template import template, menu_item_link
#from ..templates.template import menu_item_link


# Creamos una página llamada "Home" usando la decoradora template.
@template(route="/", title="Homeasdasd", description="This is the homepage.")
def home_page() -> rx.Component:
    return rx.text("This is the home page")
    # """La página de inicio.

    # Returns:
    #     El UI para la página de inicio.
    # """
    # return rx.vstack(
    #     rx.heading("Welcome to the Home Page!", size="2xl"),
    #     rx.text("This is an example of a page using the template decorator."),
    #     #menu_item_link("1","http://localhost:3001")),
    #     spacing="20px",  # Espaciado entre los elementos.
    #     align_items="center",
    #     justify_content="center",
    # )