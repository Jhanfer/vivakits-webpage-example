import reflex as rx
import vivakits.styles.image_content as im
import vivakits.styles.styles as st

def header_image() -> rx.Component:
    return rx.flex(
                rx.heading("VIVA LA EXPERIENCIA KITS",position="absolute", color=st.TextColor.ALT_BODY.value, size="6", padding_left="6em",style={"font_family":st.Fonts.TITLES.value}),
                rx.image(
                    src=im.HEADER_IMAGE_BACKGROUND,
                    height="auto",
                    width="auto"),
                align="center"
            )

def header_image_content(title:str,body:str,image:str) -> rx.Component:
    return rx.image(
                    src=image,
                    height="14em",
                    width="14em")