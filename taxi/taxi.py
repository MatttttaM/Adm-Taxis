import reflex as rx

from taxi.pages.home import home_page
from taxi.pages.about import about_page
from taxi.pages.index import otro_page
from taxi.pages.profile import profile_page
from taxi.pages.settings import settings_page
from taxi.pages.table import table_page


from .pages import *
from . import styles


#Create the app.
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    title="Dashboard Template",
    description="A dashboard template for Reflex.",
    theme=rx.theme(appearance="dark", has_background=True, radius="large", accent_color="blue"),
)

app.add_page(otro_page)
app.add_page(home_page)
app.add_page(about_page)
app.add_page(profile_page)
app.add_page(settings_page)
app.add_page(table_page)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run()