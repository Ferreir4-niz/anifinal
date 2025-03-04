import turtle

def exibir_coordenadas(x: float, y: float) -> None:
    """Exibe as coordenadas do clique do mouse."""

    # Exibe as coordenadas no console
    print(f"Coordenadas do clique: x={x:0.0f}, y={y:0.0f}")

    # Exibe as coordenadas na tela com o turtle
    turtle.penup()  # Levanta a caneta para não desenhar linhas
    turtle.goto(x, y)  # Move para as coordenadas
    turtle.pendown()  # Abaixa a caneta para começar a desenhar ou escrever
    turtle.write(f"x={x:0.0f}, y={y:0.0f}", align="center")  # Escreve as coordenadas
    turtle.stamp()  # Coloca uma marca no local do clique

# Configuração inicial do turtle
turtle.speed(0)  # Define a velocidade do turtle (0 = mais rápido)

# Usa a função onscreenclick para capturar o clique do mouse
turtle.onscreenclick(exibir_coordenadas)

def fala(personagem: turtle.Turtle, texto: str, angulo: int = 45, distancia: int = 150, tempo: float = 5):
    """Exibe um balão de fala para um personagem."""

    # Criando um turtle para o balão
    balao = turtle.Turtle()
    balao.hideturtle()  # Não queremos ver a tartaruga desenhando
    balao.speed(0)
    
    # Pegando a posição do personagem
    x, y = personagem.pos()
    
    # Desenhando a linha do balão
    balao.up()
    balao.goto(x, y)
    balao.down()
    balao.setheading(angulo)  # Garante que o ângulo esteja correto
    balao.forward(distancia)

    # Escrevendo o texto
    balao.write(texto, align="left", font=("Arial", 12, "bold"))

    # Função para apagar o balão após um tempo
    def apagar_balao():
        balao.clear()

    # Agendar a remoção do balão após `tempo` segundos
    turtle.ontimer(apagar_balao, int(tempo * 1000))

def cena1():
    # Tamanho da tela
    LARG = 1110
    ALT = 694
    MEIA_LARG = LARG // 2
    MEIA_ALT = ALT // 2

    # Configurações da tela
    turtle.setup(LARG, ALT)
    
    # Definir fundo
    try:
        turtle.bgpic(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\fundos\fundo2.gif")
    except:
        print("Erro: fundo2.gif não encontrado!")

    # Criar personagem
    finnEjake = turtle.Turtle()


    # Definir imagem e tamanho (tentando ajustar com shapesize, mas só afeta o tamanho da tartaruga)
    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
        finnEjake.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
        
        # Tentar diminuir o tamanho do "shape" (não afeta imagem gif, mas afeta a tartaruga)
        finnEjake.shapesize(stretch_wid=0.1, stretch_len=0.1)  # Tentando diminuir a tartaruga
    except:
        print("Erro: finnEjake.gif não encontrado!")

    # Movimentação
    finnEjake.up()
    finnEjake.goto(x=-543, y=-187)
    finnEjake.down()  
    finnEjake.goto(x=-239, y=-197)
    finnEjake.goto( x=449, y=-142)

  
    # Exibir texto
    turtle.penup()
    turtle.goto(0, 100)  # Definir uma posição para o texto "Olá!"
    turtle.write("Olá!", align="center", font=("Arial", 18, "bold"))

    # Manter a janela aberta
    turtle.done()

# Chamar a função
cena1()

