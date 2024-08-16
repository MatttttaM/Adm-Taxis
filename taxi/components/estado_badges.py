import reflex as rx


def _badge(icon: str, text: str, color_scheme: str):
    return rx.badge(
        rx.icon(icon, size=16),
        text,
        color_scheme=color_scheme,
        radius="full",
        variant="soft",
        size="3",
    )


def estado_badge(estado: str):
    badge_mapping = {
        "Delivered": ("check", "Entregada", "green"),
        "Pending": ("loader", "Pendiente", "yellow"),
        "Cancelled": ("ban", "Movil parado", "red"),
    }
    return _badge(*badge_mapping.get(estado, ("loader", "Pending", "yellow")))
