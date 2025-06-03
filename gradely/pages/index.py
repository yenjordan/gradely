"""The home page of the app."""

from gradely import styles
from gradely.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.container(
        rx.grid(
            rx.foreach(
                rx.Var.range(12),
                lambda i: rx.card(f"Card {i}", height="33vh"),
            ),
            columns="3",
            spacing="4",
            width="100%",
        ),
    )