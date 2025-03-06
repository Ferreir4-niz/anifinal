import turtle

# Dicionário para armazenar os balões de fala
baloes = {}

def exibir_coordenadas(x: float, y: float) -> None:
    """Exibe as coordenadas do clique do mouse."""
    print(f"Coordenadas do clique: x={x:0.0f}, y={y:0.0f}")

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"x={x:0.0f}, y={y:0.0f}", align="center", font=("Arial", 10, "normal"))
    turtle.stamp()

# Configuração inicial
turtle.speed(0)
turtle.onscreenclick(exibir_coordenadas)

def fala(personagem: turtle.Turtle, texto: str, angulo: int = 90, distancia: int = 40, tempo: float = 5):
    """Exibe um balão de fala acima do personagem e remove automaticamente após um tempo."""

    if not isinstance(personagem, turtle.Turtle):
        print("Erro: personagem passado não é um objeto Turtle!")
        return

    balao = turtle.Turtle()
    balao.hideturtle()
    balao.speed(0)

    # Obter posição do personagem
    x, y = personagem.pos()

    # Criar a linha do balão mais alta
    balao.penup()
    balao.goto(x, y + 30)
    balao.pendown()
    balao.setheading(angulo)
    balao.forward(distancia)

    # Posicionar o texto do balão mais acima
    texto_x, texto_y = balao.pos()
    balao.penup()
    balao.goto(texto_x, texto_y + 60)
    balao.write(texto, align="center", font=("Arial", 12, "bold"))

    baloes[personagem] = balao

    # Agendar remoção do balão
    turtle.ontimer(lambda: apagar_balao(personagem), int(tempo * 1000))

def apagar_balao(personagem: turtle.Turtle):
    """Apaga o balão de fala do personagem."""
    if personagem in baloes:
        balao = baloes.pop(personagem)
        balao.clear()
        balao.hideturtle()

def mover_com_while(personagem: turtle.Turtle, coordenadas):
    """Move o personagem entre as coordenadas com um delay."""
    index = 0

    def mover():
        nonlocal index
        if index >= len(coordenadas):
            return
        x, y = coordenadas[index]
        personagem.goto(x, y)
        index += 1
        turtle.ontimer(mover, 1000)

    mover()

def cena3():
        turtle.setup(1150, 694)

try:
        turtle.bgpic("nisaan/fundos/fundo5.gif")
except:
        print("Erro: fundo5.gif não encontrado!")

jakeEfinn = turtle.Turtle()
try:
        turtle.addshape("nisaan/personagens/jakeEfinn.gif")
        jakeEfinn.shape("nisaan/personagens/jakeEfinn.gif")
except:
        print("Erro: jakeEfinn.gif não encontrado!")

jakeEfinn.hideturtle()
jakeEfinn.penup()
jakeEfinn.goto((397, -224))
jakeEfinn.showturtle()

coordenadas = [(397, -165), (63, -160), (-49, -163)]
coordenadas2 = [(397, -165), (63, -160), (-49, -163), (49, -132)]
mover_com_while(jakeEfinn, coordenadas)


jujuba2 = turtle.Turtle()
try:
        turtle.addshape("nisaan/personagens/jujuba2.gif")        
        jujuba.shape("nisaan/personagens/jujuba2.gif")
except:
        print("Erro: jujuba2.gif não encontrado!")
jujuba2.hideturtle()
jujuba2.penup()
jujuba2.goto(49, -132)
jujuba2.showturtle()

mover_com_while(jujuba2, coordenadas2)

iris = turtle.Turtle()
try:
      turtle.addshape("nisaan/personagens/unicorn.gif")
      iris.shape("nisaan/personagens/unicorn.gif")
except:
      print("Erro: iris.gif não encontrado")

iris.hideturtle()
iris.penup()
iris.goto(-313, -122)
iris.showturtle()

#falas
turtle.ontimer(lambda: fala(jujuba2,"Oi, Lady!"),5000)
turtle.ontimer(lambda: fala(jakeEfinn,"Como vai, Lady?"),8000 )
turtle.ontimer(lambda: fala(iris, """annyeong yaedeul-a!"""),11000)
turtle.ontimer(lambda: fala(Jujuba2, ""Os meninos nos convidaram para 
dar um passeio, Íris."""),15000)
turtle.ontimer(lambda: fala(jakeEfinn, """Você tem que aceitar,
Lady! Vai ser irado!"""), 20000 )
turtle.ontimer(lambda: fala(iris, """mullon! jeongmal meosjil
geoyeyo!"""), 24000)
turtle.ontimer(lambda: fala(),28000 )
turtle.ontimer(lambda: fala(), )

#apagar fala
turtle.ontimer(lambda: apagar_balao(jujuba2),8000 )
turtle.ontimer(lambda: apagar_balao(jakeEfinn),11000 )
turtle.ontimer(lambda: apagar_balao(iris),15000)
turtle.ontimer(lambda: apagar_balao(jujuba2),20000 )
turtle.ontimer(lambda: apagar_balao(jakeEfinn),24000 )
turtle.ontimer(lambda: apagar_balao(),28000 )
turtle.ontimer(lambda: apagar_balao(), )

turtle.mainloop()

cena3()