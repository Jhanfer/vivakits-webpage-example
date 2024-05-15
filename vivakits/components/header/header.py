import reflex as rx
import vivakits.styles.const as cs
import vivakits.styles.styles as st
import vivakits.styles.image_content as im
from vivakits.components.header.header_image import header_image
from vivakits.components.body.header_popup import navbar_popup,mobile_navbar_popup


def header() -> rx.Component:
    return rx.vstack(
        rx.mobile_only(
            rx.flex(
                rx.image(
                    src="images/mobile_png.jpg",
                    width="100%",
                    max_width="100%"),
                rx.heading("VIVA LA EXPERIENCIA KITS",position="absolute", color=st.TextColor.ALT_BODY.value, size="5", padding_left="3.5em",padding_top="6em",style={"font_family":st.Fonts.TITLES.value})),
            mobile_navbar_popup(-500)),

        rx.tablet_and_desktop(
            navbar_popup(-50),
            header_image()),

        rx.heading(
                "Dia especial",
                padding_top="0.5em",
                size="8",
                style={"font_family":st.Fonts.TITLES.value}),
    align="center",
    justify="center")

