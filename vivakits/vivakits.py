import reflex as rx
from vivakits.components.navbar.nav_bar import navbar
from vivakits.components.navbar.mobile_navbar import mobile_navbar
import vivakits.styles.styles as st 
from vivakits.components.body.body import body
from vivakits.components.body.mobile_body import mobile_body
from vivakits.components.footer.footer import footer



class State(rx.State):
        pass


def index() -> rx.Component:
        return rx.vstack(
                        rx.tablet_and_desktop(
                                navbar(),
                                body(),
                                footer(sp="9",sp_1="5",size="4")),

                        rx.mobile_only(
                                mobile_navbar(),
                                mobile_body(),
                                footer(sp="3",sp_1="3",size="1")),
                                
                        gap="1em",
                        justify="center")

app = rx.App(style=st.STYLE_SHEET,stylesheets=st.FONTS_STYLESHEET)
app.add_page(index)


