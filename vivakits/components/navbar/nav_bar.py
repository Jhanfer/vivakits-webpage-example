import reflex as rx
import vivakits.styles.styles as st
from vivakits.components.navbar.navbar_button import navbar_button
from reflex_motion import motion

def navbar() -> rx.Component:
    return rx.hstack(
                rx.flex(
                        rx.link(
                            rx.heading(
                                "VivaKits",
                                color=st.TextColor.ALT_BODY.value,
                                style={"font_family":st.Fonts.LOGO.value})),
                        rx.hstack(
                            navbar_button("Marcas"),
                            navbar_button("Hombre"),
                            navbar_button("Mujer"),
                            navbar_button("Niños"),
                            navbar_button("Zapatos"),
                            spacing="9",
                            align="center",
                            width="100%",
                            justify="center",
                            padding_top=st.Size.SMALL.value),
                        rx.input(
                            placeholder="buscar...",
                            max_length=20,
                            radius="full"),
                        rx.link(
                            rx.icon(
                                "user",
                                height="auto",
                                weight="auto",
                                color="white",
                                padding_top="0.3em")),
                        rx.link(
                            rx.icon(
                                "shopping-cart",
                                height="auto",
                                weight="auto",
                                color="white",
                                padding_top="0.3em")),
                    direction="row",
                    align="start",
                    justify="center",
                    spacing="3",
                    width="100%",
                    padding_right=st.Size.INTERMEDIATE.value),
                align="start",
                justify="center",
                height=st.Size.VERY_BIG.value,
                bg=st.Colors.BARS.value,
                width="100%",
                padding_top=st.Size.SMALL.value,
                padding_left=st.Size.SMALL.value,
                position="fixed",
                z_index="5000")


