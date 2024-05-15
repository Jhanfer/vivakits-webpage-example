import reflex as rx
from enum import Enum

##Medidas##
class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    INTERMEDIATE="1.5em"
    BIG="2em"
    VERY_BIG="3em"

##Colores##
class Colors(Enum):
    PRIMARY="#D72638"
    SECONDARY="#3F88C5"
    BARS="#140F2D"
    ENFASIS="#F49D37"
    ERROR="#F22B29"
    BACKGROUND="#FFFFFF"

class TextColor(Enum):
    BASE_BODY="#161616"
    ALT_BODY="#FAFAFA"
    
class Fonts(Enum):
    DEFAULT="Nunito Sans"
    TITLES="Radio-Canada-Big"
    LOGO="Kanit"


STYLE_SHEET={
    "font_family":Fonts.DEFAULT.value,
    rx.link:{
        "text_decoration":"None",
        "_hover":{},
        "cursor":"pointer"
    },
    rx.button:{
        "cursor":"pointer",
        "_hover":{
        }
    }
}

FONTS_STYLESHEET=[
    "https://fonts.googleapis.com/css?family=Nunito-Sans:weight@500&display=swap",
    "https://fonts.googleapis.com/css?family=Radio-Canada-Big:wght@400&display=swap",
    "https://fonts.googleapis.com/css?family=Kanit:wght@500&display=swap"
]