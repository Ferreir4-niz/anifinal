import turtle
import time
import csv


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

      leitor = csv.DictReader(open('falas1beta.csv', 'r', encoding='utf-8'))

      for linha in leitor:
            personagem = linha['personagem']
            fala = linha['fala']
            if personagem == "finnEjake":
                  finnEjake.write(fala)
                  time.sleep(2)
                  finnEjake.undo()
            elif personagem == "BMO":
                  BMO.write(fala)
                  time.sleep(2)
                  BMO.undo()

fala()



turtle.done()
