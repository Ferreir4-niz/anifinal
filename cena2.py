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
    """Define o tamanho da tela."""
    turtle.setup(1150, 694)  # Configura a tela para 1150x694

# Chama a função para configurar a tela antes de iniciar o loop principal
cena2()

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
jakeEfinn.goto(x=371, y=-115 )
jakeEfinn.showturtle()

coordenadas = [(443, -123), (377, -122), (280, -116), (171, -130), (66, -144), (-53, -154), (-152, -158), (-257, -144),]
mover_com_while(jakeEfinn, coordenadas)

jujuba = turtle.Turtle()
try:
    turtle.addshape("nisaan/personagens/jujuba.gif")        
    jujuba.shape("nisaan/personagens/jujuba.gif")
except:
    print("Erro: jujuba.gif não encontrado!")
jujuba.hideturtle()
jujuba.penup()
jujuba.goto(-404,-187)
jujuba.showturtle()

#falas

turtle.ontimer(lambda: fala(jakeEfinn, "Oi, princesa jujuba!"), 8000)
turtle.ontimer(lambda: fala(jujuba, """Oi, meninos! 
como vocês estão?"""), 10000)
turtle.ontimer(lambda: fala(jakeEfinn,"""Estamos bem, e você? Estavamos te
procurando""" ), 13000)
turtle.ontimer(lambda: fala(jujuba, """Eu estava por aqui, meditando, como sempre"""), 17000)
turtle.ontimer(lambda: fala(jujuba, """Mas o que vocês queriam comigo afinal?"""), 22000)
turtle.ontimer(lambda: fala(jakeEfinn,"""Estavamos pensando em dar uma volta, nós todos,
como nos velhos tempos, lembra?""" ), 26000)
turtle.ontimer(lambda: fala(jujuba, """ah, sim! como eu poderia me esquecer
desses dias incriveis?"""), 30000)
turtle.ontimer(lambda: fala(jujuba, """Vamos procurar a Lady  Íris!"""), 35000)
turtle.ontimer(lambda: fala(jakeEfinn, """vamos!"""), 38000)

#apagar falas
turtle.ontimer(lambda: apagar_balao(jakeEfinn),10000 )
turtle.ontimer(lambda: apagar_balao(jujuba),13000 )
turtle.ontimer(lambda: apagar_balao(jakeEfinn), 17000)
turtle.ontimer(lambda: apagar_balao(jujuba),22000 )
turtle.ontimer(lambda: apagar_balao(jujuba),26000 )
turtle.ontimer(lambda: apagar_balao(jakeEfinn),30000 )
turtle.ontimer(lambda: apagar_balao(jujuba),35000 )
turtle.ontimer(lambda: apagar_balao(jujuba),38000)
turtle.ontimer(lambda: apagar_balao(jakeEfinn),41000 )

# Inicia o loop principal do Turtle
turtle.mainloop()

cena2()
