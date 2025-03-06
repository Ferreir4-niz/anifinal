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

def cena4():
    turtle.setup(1150, 694)

    try:
        turtle.bgpic("nisaan/fundos/fundo3.gif")
    except:
        print("Erro: fundo3.gif não encontrado!")

    iris = turtle.Turtle()
    try:
        turtle.addshape("nisaan/personagens/everybody.gif")
        iris.shape("nisaan/personagens/everybody.gif")
    except:
        print("Erro: everybody.gif não encontrado!")

    iris.hideturtle()
    iris.penup()
    iris.goto(-537, -57)
    iris.showturtle()

coordenadas = [(415, 12), (281, -34), (87, 37), (-51, -79), (194, 36), (-413, -57), (-551, 56)]

# Agendamento de falas
turtle.ontimer(lambda: fala(iris, ), 1000)
turtle.ontimer(lambda: fala(iris, ), 6000)
turtle.ontimer(lambda: fala(iris, ), 12000)
turtle.ontimer(lambda: fala(iris, ), 18000)

    # Agendamento de apagar falas
turtle.ontimer(lambda: apagar_balao(iris), 10000)
turtle.ontimer(lambda: apagar_balao(iris), 16000)
turtle.ontimer(lambda: apagar_balao(iris), 22000)

# Inicia a cena
cena4()

# Mantém a tela aberta
turtle.mainloop()
