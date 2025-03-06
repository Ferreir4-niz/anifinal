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

    def cena2():
        turtle.setup(1150, 694)

    try:
        turtle.bgpic("nisaan/fundos/fundo4.gif")
    except:
        print("Erro: fundo4.gif não encontrado!")

    jakeEfinn = turtle.Turtle()
    try:
        turtle.addshape("nisaan/personagens/jakeEfinn.gif")
        jakeEfinn.shape("nisaan/personagens/jakeEfinn.gif")
    except:
        print("Erro: jakeEfinn.gif não encontrado!")

    jakeEfinn.hideturtle()
    jakeEfinn.penup()
    jakeEfinn.goto(-515, -148)
    jakeEfinn.showturtle()

    coordenadas = [(-254, -145), (-175, -143), (-20, -143), (114, -120), (175, -116)]
    mover_com_while(jakeEfinn, coordenadas)

jujuba = turtle.Turtle()
try:
    turtle.addshape("nisaan/personagens/jujuba.gif")        
    jujuba.shape("nisaan/personagens/jujuba.gif")
except:
    print("Erro: jujuba.gif não encontrado!")
jujuba.hideturtle()
jujuba.penup()
jujuba.goto()
jujuba.showturtle()

#falas

turtle.ontimer(lambda: fala(jakeEfinn, "Oi princesa jujuba"), 5000)
turtle.ontimer(lambda: fala(jujuba, "Oi meninos, como vocês estão?"), 9000)
turtle.ontimer(lambda: fala(jakeEfinn,"Estamos bem, e você?" ), 13000)
turtle.ontimer(lambda: fala(), 17000)
turtle.ontimer(lambda: fala(), 21000)
turtle.ontimer(lambda: fala(), 25000)
turtle.ontimer(lambda: fala(), 29000)
turtle.ontimer(lambda: fala(), 32000)