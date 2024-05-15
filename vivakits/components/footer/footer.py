import reflex as rx
import vivakits.styles.styles as st 
from datetime import datetime

def    footer(*, sp:str,sp_1:str,size:str) -> rx.Component:
    return rx.hstack(
                rx.vstack(
                    rx.flex(
                        footer_vstack("Productos","Mujer","Hombre","Niños","Outlet",size),
                        footer_vstack("Deporte","Futból","Baloncesto","Golf","Rugby",size),
                        footer_vstack("Asistencia","Ayuda y atención al cliente","Devoluciones y reembolsos","Guía de tallas","Tarjetas de regalo",size),
                        footer_vstack("Sobre nosotros","Acerca de Vivakits","Empleo","Programa de afiliados","Ubicación",size),
                        direction="row",
                        align="center",
                        justify="center",
                        spacing=sp,
                        width="100%",
                        ),
                    rx.text("© ",
                            rx.text.strong("Vivakits ",_hover={"color":"gold"}),
                            f"2023-{datetime.now().year}",
                            as_="label",
                            size="2",
                            color=st.TextColor.ALT_BODY.value,
                            padding_top=st.Size.DEFAULT.value),
                    align="center",
                    spacing=sp_1,
                    padding_top=st.Size.DEFAULT.value,
                    width="100%"),
                
                position="relative",
                align="center",
                justify="center",
                height="17.5em",
                bg=st.Colors.BARS.value,
                width="100%",
                padding_top=st.Size.SMALL.value,
                padding_left=st.Size.SMALL.value,
                z_index="1000000")
                

def footer_buttons(text:str) -> rx.Component:
    return rx.link(
        text,
        variant="ghost",
        size="1"
    )

def footer_vstack(title:str,bt_1:str,bt_2:str,bt_3:str,bt_4:str,size:str) -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.heading(
                title,
                size=size)),
        footer_buttons(bt_1),
        footer_buttons(bt_2),
        footer_buttons(bt_3),
        footer_buttons(bt_4),
        align="center",
        spacing="5")


