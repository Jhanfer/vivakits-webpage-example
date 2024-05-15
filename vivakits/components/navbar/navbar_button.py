import reflex as rx
import vivakits.styles.styles as st

def navbar_button(title:str) -> rx.Component:
    return rx.button(
        title,
        variant="ghost",
        color=st.TextColor.ALT_BODY.value
    )