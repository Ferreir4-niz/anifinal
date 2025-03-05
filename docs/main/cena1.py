import turtle

def exibir_coordenadas(x: float, y: float) -> None:
    """Exibe as coordenadas do clique do mouse."""
    print(f"Coordenadas do clique: x={x:0.0f}, y={y:0.0f}")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"x={x:0.0f}, y={y:0.0f}", align="center")
    turtle.stamp()

# Configuração inicial do turtle
turtle.speed(0)
turtle.onscreenclick(exibir_coordenadas)

baloes = {}

def fala(personagem: turtle.Turtle, texto: str, angulo: int = 45, distancia: int = 90, tempo: float = 5):
    """Exibe um balão de fala com um balão oval envolta do texto."""

    if not isinstance(personagem, turtle.Turtle):
        print("Erro: personagem passado não é um objeto Turtle!")
        return

    personagem.showturtle()  # Garante que o personagem fique visível

    balao = turtle.Turtle()
    balao.hideturtle()
    balao.speed(0)
    balao.penup()

    x, y = personagem.pos()
    balao.goto(x, y + 50)  # Ajusta posição para cima do personagem
    balao.pendown()

    # Desenhar a linha do balão
    balao.setheading(angulo)
    balao.forward(distancia)
    
    texto_x, texto_y = balao.pos()
    
    balao.penup()
    balao.goto(texto_x, texto_y)
    balao.write(texto, align="center", font=("Arial", 12, "bold"))

    baloes[personagem] = balao

    turtle.ontimer(lambda: apagar_balao(personagem), int(tempo * 1000))

def apagar_balao(personagem: turtle.Turtle):
    """Apaga o balão de fala do personagem especificado."""
    if personagem in baloes:
        baloes[personagem].clear()
        baloes[personagem].hideturtle()
        del baloes[personagem]

def mover_com_while(personagem: turtle.Turtle, coordenadas):
    """Move o personagem entre as coordenadas usando um loop while com delay."""
    index = 0

    def mover():
        nonlocal index
        if index >= len(coordenadas):
            return  # Para o movimento sem esconder o personagem
        x, y = coordenadas[index]
        personagem.goto(x, y)
        index += 1
        turtle.ontimer(mover, 1000)

    mover()

def cena1():
    turtle.setup(1150, 694)

    try:
        turtle.bgpic(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\fundos\fundo2.gif")
    except:
        print("Erro: fundo2.gif não encontrado!")

    # Criar personagem BMO
    bmo = turtle.Turtle()
    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\bmo.gif")
        bmo.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\bmo.gif")
    except:
        print("Erro: bmo.gif não encontrado!")

    bmo.hideturtle()
    bmo.up() 
    bmo.goto(345, -149)
    bmo.down()
    bmo.showturtle()

    # Criar personagem Finn e Jake
    finnEjake = turtle.Turtle()
    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
        finnEjake.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
    except:
        print("Erro: finnEjake.gif não encontrado!")

    finnEjake.hideturtle()
    finnEjake.up()
    finnEjake.goto(-515, -148)
    finnEjake.showturtle()

    coordenadas = [(-254, -145), (-175, -143), (-20, -143), (114, -120), (175, -116)]
    coordenadas_finnEjake2 = coordenadas[::-1]  # Inverte a ordem das coordenadas

    mover_com_while(finnEjake, coordenadas)

    # Falas
    turtle.ontimer(lambda: finnEjake.showturtle(), 5000)
    turtle.ontimer(lambda: fala(finnEjake, "Eai, BMO! como vai, cara?"), 5000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 9000)

    turtle.ontimer(lambda: bmo.showturtle(), 9000)
    turtle.ontimer(lambda: fala(bmo, "Olá, garotos. Eu estou bem... apenas relaxando."), 9000)
    turtle.ontimer(lambda: apagar_balao(bmo), 13000)

    turtle.ontimer(lambda: fala(bmo, "Vocês deviam se juntar a mim."), 13000)
    turtle.ontimer(lambda: apagar_balao(bmo), 16000)

    turtle.ontimer(lambda: finnEjake.showturtle(), 16000)
    turtle.ontimer(lambda: fala(finnEjake, "Obrigado, BMO."), 16000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 19000)

    turtle.ontimer(lambda: fala(finnEjake, "Mas estamos procurando a Lady Rainicorn e a princesa Jujuba."), 19000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 22000)

    turtle.ontimer(lambda: fala(finnEjake, "Por acaso você não as viu por aqui?"), 22000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 25000)

    turtle.ontimer(lambda: fala(bmo, "Não, não as vi, mas a princesa Jujuba me disse que iria para o lago."), 25000)
    turtle.ontimer(lambda: apagar_balao(bmo), 28000)

    turtle.ontimer(lambda: fala(finnEjake, "Obrigado, BMO! Vamos procurar ela agora mesmo."), 28000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 32000)

    turtle.ontimer(lambda: fala(finnEjake, "Tchau, BMO!"), 32000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 35000)

    turtle.ontimer(lambda: fala(bmo, "Tchau, garotos!"), 35000)
    turtle.ontimer(lambda: apagar_balao(bmo), 38000)

    # Criar Finn e Jake voltando
    finnEjake2 = turtle.Turtle()
    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake2.gif")
        finnEjake2.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake2.gif")
    except:
        print("Erro: finnEjake2.gif não encontrado!")

    finnEjake2.hideturtle()
    finnEjake2.up()
    finnEjake2.goto(175, -116)

    turtle.ontimer(lambda: finnEjake2.showturtle(), 38000)
    turtle.ontimer(lambda: mover_com_while(finnEjake2, coordenadas_finnEjake2), 39000)

    turtle.mainloop()

# Chamar a função
cena1()
import turtle

def exibir_coordenadas(x: float, y: float) -> None:
    """Exibe as coordenadas do clique do mouse."""
    print(f"Coordenadas do clique: x={x:0.0f}, y={y:0.0f}")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"x={x:0.0f}, y={y:0.0f}", align="center")
    turtle.stamp()

turtle.speed(0)
turtle.onscreenclick(exibir_coordenadas)

baloes = {}

import turtle

def fala(personagem: turtle.Turtle, texto: str, tempo: float = 5):
    """Exibe um balão de fala com um tempo definido para desaparecer."""
    if not isinstance(personagem, turtle.Turtle):
        print("Erro: personagem passado não é um objeto Turtle!")
        return

    personagem.showturtle()

    balao = turtle.Turtle()
    balao.hideturtle()
    balao.speed(0)
    balao.penup()

    x, y = personagem.pos()
    balao.goto(x, y + 50)
    
    balao.write(texto, align="center", font=("Arial", 12, "bold"))

    baloes[personagem] = balao

    # Apagar o balão no tempo correto
    turtle.ontimer(lambda: apagar_balao(personagem), int(tempo * 1000))

def apagar_balao(personagem: turtle.Turtle):
    """Apaga o balão de fala corretamente."""
    if personagem in baloes:
        baloes[personagem].clear()
        baloes[personagem].hideturtle()
        del baloes[personagem]

def mover_com_while(personagem: turtle.Turtle, coordenadas):
    """Move o personagem entre as coordenadas usando um loop while com delay."""
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

def cena1():
    turtle.setup(1150, 694)

    try:
        turtle.bgpic(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\fundos\fundo2.gif")
    except:
        print("Erro: fundo2.gif não encontrado!")

    bmo = turtle.Turtle()
    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\bmo.gif")
        bmo.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\bmo.gif")
    except:
        print("Erro: bmo.gif não encontrado!")

    bmo.hideturtle()
    bmo.up() 
    bmo.goto(345, -149)
    bmo.down()
    bmo.showturtle()

    finnEjake = turtle.Turtle()
    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
        finnEjake.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
    except:
        print("Erro: finnEjake.gif não encontrado!")

    finnEjake.hideturtle()
    finnEjake.up()
    finnEjake.goto(-515, -148)
    finnEjake.showturtle()

    coordenadas = [(-254, -145), (-175, -143), (-20, -143), (114, -120), (175, -116)]
    coordenadas_finnEjake2 = coordenadas[::-1]

    mover_com_while(finnEjake, coordenadas)

#falas da cena 
import turtle

def fala(personagem: turtle.Turtle, texto: str, tempo: float = 5):
    """Exibe um balão de fala com um tempo definido para desaparecer."""
    if not isinstance(personagem, turtle.Turtle):
        print("Erro: personagem passado não é um objeto Turtle!")
        return

    personagem.showturtle()

    balao = turtle.Turtle()
    balao.hideturtle()
    balao.speed(0)
    balao.penup()

    x, y = personagem.pos()
    balao.goto(x, y + 50)
    
    balao.write(texto, align="center", font=("Arial", 12, "bold"))

    baloes[personagem] = balao

    # Apagar o balão no tempo correto
    turtle.ontimer(lambda: apagar_balao(personagem), int(tempo * 1000))

def apagar_balao(personagem: turtle.Turtle):
    """Apaga o balão de fala corretamente."""
    if personagem in baloes:
        baloes[personagem].clear()
        baloes[personagem].hideturtle()
        del baloes[personagem]

# Ajuste no tempo para evitar sobreposição de falas


    turtle.ontimer(lambda: fala(finnEjake, "Eai, BMO! como vai, cara?", 4), 5000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 9000)

    turtle.ontimer(lambda: fala(bmo, "Olá, garotos. Eu estou bem... apenas relaxando.", 4), 9000)
    turtle.ontimer(lambda: apagar_balao(bmo), 13000)

    turtle.ontimer(lambda: fala(bmo, "Vocês deviam se juntar a mim.", 3), 13000)
    turtle.ontimer(lambda: apagar_balao(bmo), 16000)  # Aumentei o tempo de fala para garantir que apague antes da próxima

    turtle.ontimer(lambda: fala(finnEjake, "Obrigado, BMO.", 3), 17000)  # Começa um pouco depois do apagar_balao anterior
    turtle.ontimer(lambda: apagar_balao(finnEjake), 20000)

    turtle.ontimer(lambda: fala(finnEjake, "Mas estamos procurando a Lady Rainicorn e a princesa Jujuba.", 3), 21000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 24000)

    turtle.ontimer(lambda: fala(finnEjake, "Por acaso você não as viu por aqui?", 3), 25000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 28000)

    turtle.ontimer(lambda: fala(bmo, "Não, não as vi, mas a princesa Jujuba me disse que iria para o lago.", 3), 29000)
    turtle.ontimer(lambda: apagar_balao(bmo), 32000)

    turtle.ontimer(lambda: fala(finnEjake, "Obrigado, BMO! Vamos procurar ela agora mesmo.", 3), 33000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 36000)

    turtle.ontimer(lambda: fala(finnEjake, "Tchau, BMO!", 3), 37000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 40000)

    turtle.ontimer(lambda: fala(bmo, "Tchau, garotos!", 3), 41000)
    turtle.ontimer(lambda: apagar_balao(bmo), 44000)

    finnEjake2 = turtle.Turtle()
    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake2.gif")
        finnEjake2.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake2.gif")
    except:
        print("Erro: finnEjake2.gif não encontrado!")

    finnEjake2.hideturtle()
    finnEjake2.up()
    finnEjake2.goto(175, -116)


    turtle.ontimer(lambda: turtle.showturtle(finnEjake2), 38000)
    turtle.ontimer(lambda: turtle.hideturtle(finnEjake), 36000)

    turtle.done()

cena1()
