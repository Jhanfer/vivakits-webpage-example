import reflex as rx
from reflex_motion import motion
import vivakits.styles.styles as st

class PopUpLocation(rx.State):
    value:int = 50
    pos: int 
    delay:int 

    def reset_pos(self):
        self.pos = self.value
        self.delay = 4
    def hidden_popup(self):
        if self.pos == self.value:
            self.delay = 0
            self.pos = -50
        else:
            self.pos = self.value

class MobilePopUpLocation(rx.State):
    value:int = -181
    pos: int 
    delay:int 

    def reset_pos(self):
        self.pos = self.value
        self.delay = 4
    def hidden_popup(self):
        if self.pos == self.value:
            self.delay = 0
            self.pos = -500
        else:
            self.pos = self.value


def navbar_popup(initial:int) -> rx.Component:
    return motion(
                rx.hstack(
                    rx.spacer(),
                    rx.text("ENVÍOS GRATUITOS PARA PEDIDOS SUPERIORES A 60 €. 60 DÍAS DE DEVOLUCIONES GRATUITAS.",size="1"),
                    rx.spacer(),
                    rx.link(
                        rx.icon(tag="x"),
                        color_scheme="gray",
                        on_click=PopUpLocation.hidden_popup(),
                        size="1",
                        _hover={"color":"#6A8FE9"}),
                bg="#E9C46A",
                padding=st.Size.SMALL.value,
                direction="row",
                width="100%",
                align="center",
                position="absolute",
                on_mount=PopUpLocation.reset_pos()),
            initial={"y":initial},
            animate={"y":PopUpLocation.pos},
            transition={"type":"spring","delay":PopUpLocation.delay,"damping":20,"swiftness":20})


def mobile_navbar_popup(initial:int) -> rx.Component:
    return motion(
                rx.hstack(
                    rx.spacer(),
                    rx.text("ENVÍOS GRATUITOS PARA PEDIDOS SUPERIORES A 60 €. 60 DÍAS DE DEVOLUCIONES GRATUITAS.",size="1"),
                    rx.spacer(),
                    rx.link(
                        rx.icon(tag="x"),
                        color_scheme="gray",
                        on_click=MobilePopUpLocation.hidden_popup(),
                        size="1",
                        _hover={"color":"#6A8FE9"}),
                bg="#E9C46A",
                padding=st.Size.SMALL.value,
                direction="row",
                width="100%",
                align="center",
                position="absolute",
                on_mount=MobilePopUpLocation.reset_pos()),
            initial={"y":initial},
            animate={"y":MobilePopUpLocation.pos},
            transition={"type":"spring","delay":MobilePopUpLocation.delay,"damping":20,"swiftness":20})