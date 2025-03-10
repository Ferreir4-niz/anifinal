import turtle
import time

arquivo = open('falas1.csv', 'r', encoding='utf-8')

def fala():
    personagem = turtle.Turtle() 
    personagem.hideturtle()
    personagem.penup()
    personagem.goto(0, 0)

    for linha in arquivo:
        if ";" in linha:  
            personagem_nome, fala = linha.strip().split(";")

            personagem.clear()

            personagem.write(f"{personagem_nome}: {fala}")

            time.sleep(2)

fala()

arquivo.close()

turtle.done()
