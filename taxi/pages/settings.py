"""The settings page."""
import reflex as rx


from taxi.templates.template import template
from ..views.new.color_picker import primary_color_picker, secondary_color_picker
from ..views.new.radius_picker import radius_picker
from ..views.new.scaling_picker import scaling_picker


@template(route="/settings",title="Settings",description="settings asofdauhjfa")
def settings_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Settings", size="5"),
        # Primary color picker
        rx.vstack(
            rx.hstack(
                rx.icon("palette", color=rx.color("accent", 10)),
                rx.heading("Primary color", size="6"),
                align="center",
            ),
            primary_color_picker(),
            spacing="4",
            width="100%",
        ),
        # Secondary color picker
        rx.vstack(
            rx.hstack(
                rx.icon("blend", color=rx.color("gray", 11)),
                rx.heading("Secondary color", size="6"),
                align="center",
            ),
            secondary_color_picker(),
            spacing="4",
            width="100%",
        ),
        # Radius picker
        radius_picker(),
        # Scaling picker
        scaling_picker(),
        spacing="7",
        width="100%",
    )
