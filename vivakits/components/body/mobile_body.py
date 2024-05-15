import reflex as rx
import vivakits.styles.const as cs
import vivakits.styles.image_content as im
from vivakits.components.header.header_image import header_image,header_image_content
import vivakits.styles.styles as st
import vivakits.components.body.body_carousel as cr
from vivakits.components.body.body_component import images_badges_left,images_badges_right,windowns_component_motion
from reflex_motion import motion
from vivakits.components.header.header import header
from vivakits.components.body.body_anoucement import anoucement,text_area


def mobile_body() -> rx.Component:
    return rx.vstack(
                header(),
                cr.body_carousel("26em","11em","1"),
                images_badges_left(title_1="LOS MEJORES ESTILOS",src=im.MOBILE_BADGE_1,wi=40,ini=1,padding="0em",padding_heading="11.5em"),
                images_badges_right(title_1="SIENTE EL DEPORTE",src=im.MOBILE_BADGE_2,x_f=72,x_i=100,padding="0em",padding_heading="11em"),
                rx.flex(
                    windowns_component_motion("x",-15,0,"Training",im.WINDOWN_1,"18em","23em"),
                    windowns_component_motion("x",15,0,"Pool",im.WINDOWN_2,"18em","23em"),
                    windowns_component_motion("x",-15,0,"Sport",im.WINDOWN_3,"18em","23em"),
                    direction="column",
                    padding_bottom="5em",
                    padding_top="5em",
                    spacing="9"),
                images_badges_left(title_1="ZAPATOS DE CALIDAD",src=im.MOBILE_BADGE_3,wi=45,ini=1,padding="0em",padding_heading="11.5em"),
                rx.flex(
                    windowns_component_motion("x",-15,0,"Hombre",im.WINDOWN_4,"18em","18em"),
                    windowns_component_motion("y",15,0,"Mujer",im.WINDOWN_5,"18em","18em"),
                    windowns_component_motion("x",-15,0,"Niños",im.WINDOWN_6,"18em","18em"),
                    direction="column",
                    padding_bottom="5em",
                    padding_top="5em",
                    spacing="9"),
                anoucement("70%"),
                text_area("70%"),
                align="center")
