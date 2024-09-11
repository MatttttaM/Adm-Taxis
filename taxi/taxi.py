import reflex as rx

from taxi.pages.liquidacion import liquidacion_page
from taxi.pages.gastos import gastos_page
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
    title="Adm taxis",
    description="Prototipo de app para adm de taxis",
    theme=rx.theme(appearance="dark", has_background=True, radius="large", accent_color="blue"),
)

app.add_page(liquidacion_page)
app.add_page(table_page)
app.add_page(otro_page)
#app.add_page(home_page)
app.add_page(gastos_page)
app.add_page(about_page)
app.add_page(profile_page)
app.add_page(settings_page)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run()