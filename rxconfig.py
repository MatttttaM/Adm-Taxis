import reflex as rx

from taxi.db.client import DB_URL

config = rx.Config(
    app_name="taxi",
    DATABASE_URL=DB_URL
)