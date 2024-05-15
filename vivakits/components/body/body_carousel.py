import reflex as rx
import vivakits.styles.const as cs
import vivakits.styles.image_content as im
from vivakits.components.header.header_image import header_image,header_image_content
import vivakits.styles.styles as st
from reflex_motion import motion

class Example(rx.State):
    count:int = 1
    value:int = 0
    
    def increment(self):
        if self.count < 0:
            self.count += 500
        if self.count > 1:
            self.count = 1
    def decrement(self):
        if self.count > -1400:
            self.count -= 520
    def values(self):
        if abs(self.count) > 100:
            self.value = 100


def animate():
    return rx.hstack(
                motion(
                    rx.hstack(
                        header_image_content("Zapato","x talla",im.ART_1),
                        header_image_content("Zapato","x talla",im.ART_2),
                        header_image_content("Zapato","x talla",im.ART_3),
                        header_image_content("Zapato","x talla",im.ART_4),
                        header_image_content("Zapato","x talla",im.ART_5),
                        header_image_content("Zapato","x talla",im.ART_1),
                        header_image_content("Zapato","x talla",im.ART_2),
                        header_image_content("Zapato","x talla",im.ART_3),
                        header_image_content("Zapato","x talla",im.ART_4),
                        header_image_content("Zapato","x talla",im.ART_5),
                        spacing="7"),
                animate={"x":Example.count},
                transition={"type":"spring","stiffness":300,"damping":20},
                width="100%"),
            align="center",
            justify="center",
            spacing="9",
            width="100%")

def carousel_buttons(icon:str,state:rx.State) -> rx.Component:
    return rx.box(
                rx.icon_button(
                    icon,
                    color_scheme="grass",
                    on_click=state,
                    height="250px",
                    variant="ghost"))


def body_carousel(w:str,h:str,sp:str) -> rx.Component:
    return rx.flex(
            rx.box(carousel_buttons("move-left",Example.increment),z_index="1000"),
            animate(),
            rx.box(carousel_buttons("move-right",Example.decrement),z_index="1000"),
            style={
                "overflow":"hidden",
                "width":w,
                "height":h,
                "position":"static"},
            align="center",
            justify="start",
            spacing=sp,
            padding_bottom="0em"),live_progress()



def vstack_piece()->rx.Component:
    return rx.vstack(
        header_image_content("Zapato","x talla",im.ART_1),
        rx.text("hola"),
        width="100%",
        align="center"
    )

def live_progress():
    return rx.progress(value=abs(Example.count)/16,width="50%",height="0.2em",color_scheme="gray",margin_bottom=st.Size.INTERMEDIATE.value,margin_top="0em")




