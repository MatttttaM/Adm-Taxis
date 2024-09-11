"""The table page."""
import reflex as rx


from taxi.templates.template import template
from ..backend.table_state import TableState
from ..views.tabla_nueva import main_table


@template(route="/table",title="Table",description="tablessss askfjañglka",on_load=TableState.load_entries)
def table_page() -> rx.Component:
    """The table page.

    Returns:
        The UI for the table page.
    """
    return rx.vstack(
        rx.heading("Table", size="5"),
        main_table(),
        spacing="8",
        width="100%",
    )
