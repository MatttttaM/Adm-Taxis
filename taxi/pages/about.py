"""The about page."""
import reflex as rx

from taxi.templates.template import template
from .. import styles


@template(route="/about",title="About",description="sdajfjsl")
def about_page() -> rx.Component:

    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)