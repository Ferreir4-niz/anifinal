import turtle
import time

arquivo = open('falas1.csv', 'r', encoding='utf-8')

def fala():
    finnEjake = turtle.Turtle(shape='turtle') 
    finnEjake.color('red')
    #finnEjake.hideturtle()
    finnEjake.penup()
    finnEjake.goto(-30, 30)

    BMO = turtle.Turtle(shape='turtle') 
    finnEjake.color('red')
    #BMO.hideturtle()
    BMO.penup()
    BMO.goto(30, -30)

    for linha in arquivo:
            personagem,fala = linha.strip().split(";")
            if personagem == "finnEjake":
                  finnEjake.write(fala)
                  time.sleep(2)
                  finnEjake.undo()
            elif personagem == "BMO":
                  BMO.write(fala)
                  time.sleep(2)
                  BMO.undo()

fala()

arquivo.close()

turtle.done()
