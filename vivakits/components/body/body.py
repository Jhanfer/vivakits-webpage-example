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
from reflex_responsive_carousel import responsive_carousel

def body() -> rx.Component:
    return rx.vstack(
                header(),
                cr.body_carousel("50em","20em","9"),
                responsive_carousel(
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
                    width="25em",
                    infinite_loop=True,
                    auto_play=True,
                    swipeable=True,
                    height="50"
                ),
                images_badges_left(title_1="LOS MEJORES ESTILOS",src=im.BADGE_1,wi=70,ini=0,padding="0em",padding_heading="15em"),
                images_badges_right(title_1="SIENTE EL DEPORTE",src=im.BADGE_2,x_f=720,x_i=800,padding="0em",padding_heading="10.2em"),
                rx.flex(
                    windowns_component_motion("x",-10,20,"Training",im.WINDOWN_1,"18em","23em"),
                    windowns_component_motion("y",-15,0,"Pool",im.WINDOWN_2,"18em","23em"),
                    windowns_component_motion("x",20,-10,"Sport",im.WINDOWN_3,"18em","23em"),
                    padding_bottom="5em",
                    padding_top="5em",
                    spacing="9",
                    padding_right=st.Size.SMALL.value,
                    style={"overflow":"hidden"}),
                images_badges_left(title_1="ZAPATOS DE CALIDAD",src=im.BADGE_3,wi=70,ini=1,padding="0em",padding_heading="15em"),
                rx.flex(
                    windowns_component_motion("x",-10,20,"Hombre",im.WINDOWN_4,"18em","18em"),
                    windowns_component_motion("y",-15,0,"Mujer",im.WINDOWN_5,"18em","18em"),
                    windowns_component_motion("x",20,-10,"Niños",im.WINDOWN_6,"18em","18em"),
                    padding_bottom="5em",
                    padding_top="5em",
                    spacing="9",
                    align="center",
                    padding_right=st.Size.SMALL.value,
                    style={"overflow":"hidden"}),
                anoucement("100%"),
                text_area("70%"),
                align="center")

