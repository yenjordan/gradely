"""Common templates used between pages in the app."""

from __future__ import annotations

from gradely import styles
# from gradely.components.sidebar import sidebar
from typing import Callable

import reflex as rx

# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]

def logo() -> rx.Component:
    return rx.image(src="gradelyLogo.png", width="10em", height="2em", margin_left="12em"),

def navbar():
    return rx.hstack(
        rx.hstack(
            rx.text("Home", margin_left="3em", font_size="1.3em", font_weight=500, ),
            rx.text("Grades", margin_left="3em", font_size="1.3em", font_weight=500, ),
            rx.text("Account", margin_left="3em", font_size="1.3em", font_weight=500, ),
        ),
        rx.hstack(
            rx.image(src="gradelyLogo.png", width="10em", height="2em", margin_left="14em"),
        ),
        rx.spacer(),
        
        # rx.chakra.menu(
        #     rx.chakra.menu_button("Menu"),
        #     rx.chakra.menu_list(
        #         rx.chakra.menu_item("Item 1"),
        #         rx.chakra.menu_divider(),
        #         rx.chakra.menu_item("Item 2"),
        #         rx.chakra.menu_item("Item 3"),
        #     ),
        # ),
        position="fixed",
        top="0px",
        background_color="#F8F6F5",
        padding="1em",
        height="4em",
        width="100%",
        z_index="0",
        margin_top="0.9em",
    )


def menu_button() -> rx.Component:
    """The menu button on the top right of the page.

    Returns:
        The menu button component.
    """
    from reflex.page import get_decorated_pages

    return rx.chakra.box(
        rx.chakra.menu(
            rx.chakra.menu_button(
                rx.chakra.icon(
                    tag="hamburger",
                    size="4em",
                    color=styles.text_color,
                ),
            ),
            rx.chakra.menu_list(
                *[
                    rx.chakra.menu_item(
                        rx.chakra.link(
                            page["title"],
                            href=page["route"],
                            width="100%",
                        )
                    )
                    for page in get_decorated_pages()
                ],
                rx.chakra.menu_divider(),
                rx.chakra.menu_item(
                    rx.chakra.link(
                        "About", href="https://github.com/reflex-dev", width="100%"
                    )
                ),
                rx.chakra.menu_item(
                    rx.chakra.link(
                        "Contact", href="mailto:founders@=reflex.dev", width="100%"
                    )
                ),
            ),
        ),
        position="fixed",
        right="1.5em",
        top="1.5em",
        z_index="500",
    )


def template(
    route: str | None = None,
    title: str | None = None,
    image: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    """The template for each page of the app.

    Args:
        route: The route to reach the page.
        title: The title of the page.
        image: The favicon of the page.
        description: The description of the page.
        meta: Additionnal meta to add to the page.
        on_load: The event handler(s) called when the page load.
        script_tags: Scripts to attach to the page.

    Returns:
        The template with the page content.
    """

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        """The template for each page of the app.

        Args:
            page_content: The content of the page.

        Returns:
            The template with the page content.
        """
        # Get the meta tags for the page.
        all_meta = [*default_meta, *(meta or [])]

        @rx.page(
            route=route,
            title=title,
            image=image,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def templated_page():
            return rx.chakra.hstack(
                # sidebar(),
                navbar(),
                rx.chakra.box(
                    # logo(),
                    rx.chakra.box(
                        page_content(),
                        **styles.template_content_style,
                    ),
                    **styles.template_page_style,
                ),
                # menu_button(),
                align_items="flex-start",
                transition="left 0.5s, width 0.5s",
                position="relative",
            )

        return templated_page

    return decorator