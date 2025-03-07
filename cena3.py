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

# Função para exibir falas
def fala(personagem: turtle.Turtle, texto: str, angulo: int = 90, distancia: int = 40, tempo: float = 5):
    """Exibe um balão de fala acima do personagem e remove automaticamente após um tempo."""
    if not isinstance(personagem, turtle.Turtle):
        print("Erro: personagem passado não é um objeto Turtle!")
        return

    balao = turtle.Turtle()
    balao.speed(0)
    balao.penup()
    balao.hideturtle()

    x, y = personagem.pos()
    
    balao.goto(x, y + 30)
    balao.pendown()
    balao.setheading(angulo)
    balao.forward(distancia)
    
    texto_x, texto_y = balao.pos()
    balao.penup()
    balao.goto(texto_x, texto_y + 60)
    balao.write(texto, align="center", font=("Arial", 12, "bold"))

    baloes[personagem] = balao
    turtle.ontimer(lambda: apagar_balao(personagem), int(tempo * 1000))

# Função para apagar o balão de fala
def apagar_balao(personagem: turtle.Turtle):
    """Apaga o balão de fala do personagem."""
    if personagem in baloes:
        balao = baloes.pop(personagem)
        balao.clear()
        balao.hideturtle()

# Função para mover os turtles simultaneamente
def mover_simultaneo(personagens, coordenadas):
    """Move os personagens simultaneamente pelas coordenadas."""
    index = 0
    
    def mover():
        nonlocal index
        if index >= len(coordenadas):
            return
        for i, personagem in enumerate(personagens):
            x, y = coordenadas[index][i]
            personagem.goto(x, y)
        index += 1
        turtle.ontimer(lambda: mover(), 1000)

    mover()

# Função para configurar a cena
def cena3():
    turtle.setup(1150, 694)
    try:
        turtle.bgpic("nisaan/fundos/fundo5.gif")
    except:
        print("Erro: fundo5.gif não encontrado!")

# Inicializando a cena
cena3()

# Criando o turtle 'jakeEfinn'
jakeEfinn = turtle.Turtle()
jakeEfinn.hideturtle()
jakeEfinn.penup()
try:
    turtle.addshape("nisaan/personagens/jakeEfinn.gif")
    jakeEfinn.shape("nisaan/personagens/jakeEfinn.gif")
except:
    print("Erro: jakeEfinn.gif não encontrado!")

jakeEfinn.goto(443, -123)
jakeEfinn.showturtle()

# Criando o turtle 'jujuba2'
jujuba2 = turtle.Turtle()
try:
    turtle.addshape("nisaan/personagens/jujuba2.gif")
    jujuba2.shape("nisaan/personagens/jujuba2.gif")
except:
    print("Erro: jujuba2.gif não encontrado!")

jujuba2.hideturtle()
jujuba2.penup()
jujuba2.goto(443, -123)
jujuba2.showturtle()

# Criando o turtle 'iris' (unicorn)
iris = turtle.Turtle()
try:
    turtle.addshape("nisaan/personagens/unicorn.gif")
    iris.shape("nisaan/personagens/unicorn.gif")
except:
    print("Erro: unicorn.gif não encontrado")

iris.hideturtle()
iris.penup()
iris.goto(-370, -78)
iris.showturtle()

# Coordenadas de movimento ajustadas para fazer jujuba2 mais à direita e jakeEfinn mais à esquerda na última posição
coordenadas = [
    [(443, -123), (377, -122)],  # jakeEfinn e jujuba2 na primeira posição
    [(397, -115), (333, -118)],  # jakeEfinn e jujuba2 na segunda posição
    [(350, -109), (290, -112)],  # jakeEfinn e jujuba2 na terceira posição
    [(303, -98), (244, -106)],   # jakeEfinn e jujuba2 na quarta posição
    [(256, -87), (197, -103)],   # jakeEfinn e jujuba2 na quinta posição
    [(189, -76), (150, -92)],    # jakeEfinn e jujuba2 na sexta posição
    [(130, -64), (90, -78)],     # jakeEfinn e jujuba2 na sétima posição
    [(190, -53), (70, -69)],    # Última posição: jujuba2 mais à direita e jakeEfinn mais à esquerda
]

# Mover os personagens simultaneamente
mover_simultaneo([jujuba2, jakeEfinn], coordenadas)

# Falas programadas para ocorrer depois que os personagens pararem de se mover
turtle.ontimer(lambda: fala(jujuba2, "Oi, Lady!"), 8000)  # Após movimento
turtle.ontimer(lambda: fala(jakeEfinn, "Como vai, Lady?"), 11000)  # Após jujuba2
turtle.ontimer(lambda: fala(iris, "annyeong yaedeul-a!"), 14000)  # Após jakeEfinn
turtle.ontimer(lambda: fala(jujuba2, """Os meninos nos convidaram para
dar um passeio, Íris."""), 18000)  # Após iris
turtle.ontimer(lambda: fala(jakeEfinn, """Você tem que aceitar,
Lady! Vai ser irado!"""), 24000)  # Após jujuba2
turtle.ontimer(lambda: fala(iris, """mullon! jeongmal meosjil
geoyeyo!"""), 28000)  # Após jakeEfinn
turtle.ontimer(lambda: fala(iris, """nae mog-e ollatala
yaedeul-a!"""), 32000)

# Apagar falas após um tempo
turtle.ontimer(lambda: apagar_balao(jujuba2), 11000)
turtle.ontimer(lambda: apagar_balao(jakeEfinn), 14000)
turtle.ontimer(lambda: apagar_balao(iris), 18000)
turtle.ontimer(lambda: apagar_balao(jujuba2), 24000)
turtle.ontimer(lambda: apagar_balao(jakeEfinn), 28000)
turtle.ontimer(lambda: apagar_balao(iris), 32000)
turtle.ontimer(lambda: apagar_balao(iris), 37000)

# Iniciar a janela do turtle
turtle.mainloop()
