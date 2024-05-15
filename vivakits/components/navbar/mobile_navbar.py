import reflex as rx
import vivakits.styles.styles as st
from reflex_motion.motion import motion

def mobile_navbar() -> rx.Component:
    return rx.hstack(
                rx.flex(
                        rx.link(
                            rx.heading(
                                "VivaKits",
                                color=st.TextColor.ALT_BODY.value)),
                        rx.spacer(),
                        drawer(),
                    direction="row",
                    align="start",
                    justify="center",
                    spacing="3",
                    width="100%",
                    padding_right=st.Size.SMALL.value),
                align="start",
                justify="start",
                height=st.Size.VERY_BIG.value,
                bg=st.Colors.BARS.value,
                width="100%",
                padding_top=st.Size.SMALL.value,
                padding_left=st.Size.SMALL.value,
                position="fixed",
                z_index="1000")


def drawer() -> rx.Component:
    return rx.drawer.root(
                    rx.drawer.trigger(
                        motion(        
                                rx.icon_button(
                                        "menu",
                                        height="auto",
                                        width="auto", 
                                        color=st.TextColor.ALT_BODY.value,
                                        _hover={"variant":"ghost"},
                                        variant="ghost"),
                                while_hover={"rotate":90},
                                while_tap={"rotare":90},
                                transition={"type":"spring","duration":100000,"ease":"back_in_out","stiffness": 260, "damping": 20}),
                    padding_top="0.3em"),
                    rx.drawer.overlay(z_index="6"),
                    rx.drawer.portal(
                        rx.drawer.content(
                            rx.vstack(
                                rx.flex(
                                    rx.drawer.close(rx.box(rx.button("Close"),align="end")),
                                    padding_left="13em",
                                    direction="column"),
                                menú_button("marcas"),
                                menú_button("hombre"),
                                menú_button("mujer"),
                                menú_button("niños"),
                                menú_button("zapatos"),
                                justify="start",
                                align="center"),
                            top="auto",
                            right="auto",
                            left="2.7em",
                            height="100%",
                            width="100%",
                            padding="2em",
                            background_color=st.Colors.BARS.value)),
            direction="right")

def menú_button(title:str) -> rx.Component:
    return rx.button(title,width="100%")