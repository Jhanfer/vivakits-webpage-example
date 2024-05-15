import reflex as rx
import vivakits.styles.styles as st

def anoucement(w:str) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text("20% De descuento de bienvenida por inscribirte en nuestro Newsletter",size="6"),
            rx.hstack(rx.input(placeholder="email",radius="full"),rx.button("registrarme",radius="full")),
            align="center",
            justify="center",
            spacing="4",
            width=w),
        bg="#E9C46A",
        width="100%",
        height="10em",
        align="center",
        justify="center"
    )

def text_area(w:str) -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading("¡Bienvenido a Vivakits, tu destino para ropa, calzado y accesorios de alta calidad!",style={"font_family":st.Fonts.TITLES.value}),
            rx.text("""En Vivakits, no solo nos destacamos por nuestra calidad y estilo, sino también por nuestra pasión, determinación y alegría. Estos valores nos impulsan a alcanzar la excelencia en todo lo que hacemos, ya sea en el gimnasio, en la pista o en el campo.
                        Cuando elijes Vivakits, te equipas con lo mejor para tus aventuras diarias y desafíos deportivos. Ya sea que seas un atleta de élite o simplemente quieras mantenerte activo y saludable, tenemos todo lo que necesitas para brillar y rendir al máximo.
                        Nuestra experiencia y compromiso en ofrecer productos de calidad en el ámbito deportivo nos convierten en tu compañero de confianza. Como dice nuestro lema: "¡Vivakits, para siempre en movimiento, siempre hacia adelante!""",
                        size="2"),
            align="center",
            justify="center",
            width=w,
            spacing="4"
        ),
    align="center",
    justify="center",
    padding_top=st.Size.INTERMEDIATE.value,
    padding_bottom=st.Size.INTERMEDIATE.value)
