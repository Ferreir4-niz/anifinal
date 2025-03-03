# main.cena_demo()

"""
Cena de demonstração que exibe um gato :cat2: e um rato :mouse2: falando.

"""


def cena_demo():
    """Cena de demonstração."""

    LARG=1110
    ALT=694
    MEIA_LARG=(LARG//2)
    MEIA_ALT=(ALT//2)
    turtle.setup(1110, 694)

    animaivos.nucleo.carrega_img_fundo("fundo-com-degraus.png")

    # O gato será visto em todo o programa
    global gato
    global rato

    gato = turtle.Turtle(shape="_cat.gif")
    gato.up()
    animaivos.nucleo.fala(gato, "Olá!")
    animaivos.nucleo.fala(gato, "Estou no centro da imagem.")
    gato.goto(-MEIA_LARG, 0)
    gato.shape("cat_.gif")
    gato.goto(0, 0)

    rato = turtle.Turtle(shape="mouse_.gif")
    rato.up()
    animaivos.nucleo.fala(rato, "Olá!")
    animaivos.nucleo.fala(rato, "Estou no centro da imagem.")
    rato.goto(+MEIA_LARG, 0)
    rato.shape("_mouse.gif")
    rato.goto(0, 0)