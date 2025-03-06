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

def cena1():
    turtle.setup(1150, 694)

    try:
        turtle.bgpic(r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\NiSaAn.py\\fundos\\fundo2.gif")
    except:
        print("Erro: fundo2.gif não encontrado!")

    bmo = turtle.Turtle()
    try:
        turtle.addshape(r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\NiSaAn.py\\personagens\\bmo.gif")
        bmo.shape(r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\NiSaAn.py\\personagens\\bmo.gif")
    except:
        print("Erro: bmo.gif não encontrado!")

    bmo.hideturtle()
    bmo.penup()
    bmo.goto(345, -149)
    bmo.showturtle()

    finnEjake = turtle.Turtle()
    try:
        turtle.addshape(r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\NiSaAn.py\\personagens\\finnEjake.gif")
        finnEjake.shape(r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\NiSaAn.py\\personagens\\finnEjake.gif")
    except:
        print("Erro: finnEjake.gif não encontrado!")

    finnEjake.hideturtle()
    finnEjake.penup()
    finnEjake.goto(-515, -148)
    finnEjake.showturtle()

    coordenadas = [(-254, -145), (-175, -143), (-20, -143), (114, -120), (175, -116)]
    mover_com_while(finnEjake, coordenadas)

    # Esconder finnEjake corretamente antes de mostrar jakeEfinn
    turtle.ontimer(finnEjake.hideturtle, 35000)

    def criar_jakeEfinn():
        """Cria e move Jake e Finn após a saída de finnEjake"""
        jakeEfinn = turtle.Turtle()
        try:
            turtle.addshape(r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\NiSaAn.py\\personagens\\jakeEfinn.gif")
            jakeEfinn.shape(r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\NiSaAn.py\\personagens\\jakeEfinn.gif")
        except:
            print("Erro: jakeEfinn.gif não encontrado!")
            return

        jakeEfinn.hideturtle()
        jakeEfinn.penup()
        jakeEfinn.goto(175, -116)
        jakeEfinn.showturtle()

        coordenadas2 = [(196, -111), (88, -124), (39, -115), (-125, -112), (-265, -106), (-497, -100)]
        mover_com_while(jakeEfinn, coordenadas2)

    # Criar Jake e Finn após finnEjake desaparecer
    turtle.ontimer(criar_jakeEfinn, 34000)

    # Diálogos ajustados sem sobreposição
    turtle.ontimer(lambda: fala(finnEjake, "E aí, BMO! Como vai, cara?"), 5000)
    turtle.ontimer(lambda: fala(bmo, "Olá, garotos. Eu estou bem... apenas relaxando."), 9000)
    turtle.ontimer(lambda: fala(finnEjake, "Estamos procurando a Lady Íris e a Princesa Jujuba."), 13000)
    turtle.ontimer(lambda: fala(finnEjake, "Por acaso você não as viu por aqui?"), 17000)
    turtle.ontimer(lambda: fala(bmo, """Não, não as vi, mas a Princesa Jujuba me 
    disse que iria para o lago."""), 21000)
    turtle.ontimer(lambda: fala(finnEjake, "Obrigado, BMO! Vamos procurar ela agora mesmo."), 25000)
    turtle.ontimer(lambda: fala(finnEjake, "Tchau, BMO!"), 29000)
    turtle.ontimer(lambda: fala(bmo, "Tchau, garotos!"), 32000)

    # Remover balões corretamente
    turtle.ontimer(lambda: apagar_balao(finnEjake), 8500)
    turtle.ontimer(lambda: apagar_balao(bmo), 12500)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 16500)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 20500)
    turtle.ontimer(lambda: apagar_balao(bmo), 24500)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 28500)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 31500)
    turtle.ontimer(lambda: apagar_balao(bmo), 34500)

    # Escondendo o personagem após sua última fala
    turtle.ontimer(finnEjake.hideturtle, 32000)

    turtle.mainloop()

cena1()
