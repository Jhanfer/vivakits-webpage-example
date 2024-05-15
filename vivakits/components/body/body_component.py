import reflex as rx
import vivakits.styles.image_content as im
import vivakits.styles.styles as st
from reflex_motion import motion



##Image Badge##

def images_badges_left(*, title_1:str,src:str,wi:int,ini:str,padding:str,padding_heading:str) -> rx.Component:
    return rx.flex(
        motion(
            rx.heading(title_1,color=st.TextColor.ALT_BODY.value,size="7",padding_left=padding,width=padding_heading,style={"position":"absolute","top": "0em","left":"10px","font_family":st.Fonts.TITLES.value}),
            initial={"x":ini},
            while_in_view={"x":wi},
            transition={"type":"spring","stiffness": 260,"damping":150}),
        rx.image(
                src=src,
                height="100%",
                width="100%"),
        align="center",
        style={"overflow":"hidden"})


def images_badges_right(*, title_1:str,src:str,x_f:int,x_i:int,padding:str,padding_heading:str) -> rx.Component:
    return rx.flex(
        motion(
            rx.hstack(rx.spacer(),rx.heading(title_1,color=st.TextColor.ALT_BODY.value,size="7",padding_left=padding,width=padding_heading,style={"position":"absolute","top":"0em","left":"0em","font_family":st.Fonts.TITLES.value}),align="end"),
            initial={"x":x_i},
            while_in_view={"x":x_f},
            transition={"type":"spring","stiffness": 260,"damping":150}),
        rx.image(
                src=src,
                height="100%",
                width="100%"),
        align="center",
        direction="row",
        style={"overflow":"hidden"})


def windowns_component(title:str,src:str,width:str,height:str) -> rx.Component:
    return rx.vstack(
                rx.link(
                    rx.image(
                        src=src,
                        width=width,
                        height=height),
                    padding="0em"),
                rx.link(title,size="7",color="black",style={"font_family":st.Fonts.TITLES.value}),
                spacing="6",
                align="center")

def windowns_component_motion(letra:str,mval:int,pval:int,title:str,img:str,width:str,height:str) -> rx.Component:
    return motion(
                windowns_component(title,img,width,height),
                initial={letra:mval,"filter":"brightness(1)"},
                while_hover={"filter":"brightness(0.5)"},
                while_in_view={letra:pval},
                transition={"type":"spring","stiffness":360,"damping":20})