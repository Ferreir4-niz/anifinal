# animaivos.nucleo.fala()

import time
import turtle

balao = turtle.textinput

def fala(personagem: turtle.Turtle, 
         texto: str, 
         angulo: int = 45, 
         distancia: int = 150,
         tempo: float = 5):

    x,y = personagem.pos()
    balao.up() 
    balao.goto(x, y) 
    balao.down()
    balao.left(angulo)
    balao.forward(distancia)
    balao.write(texto)
    time.sleep(tempo)
    balao.undo()
    balao.undo()
    balao.undo()
