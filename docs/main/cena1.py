# main.cena1()

import turtle

def cena1():

    LARG=1110
    ALT=694
    MEIA_LARG=(LARG//2)
    MEIA_ALT=(ALT//2)
    turtle.setup(1110, 694)

    NiSaAn.nucleo.carrega_img_fundo("fundo1.gif")

 
    gato = turtle.Turtle(shape="_cat.gif")
    gato.up()
    NiSaAn.nucleo.fala(gato, "Olá!")
    NiSaAn.nucleo.fala(gato, "Estou no centro da imagem.")
    gato.goto(-MEIA_LARG, 0)
    gato.shape("cat_.gif")
    gato.goto(0, 0)


