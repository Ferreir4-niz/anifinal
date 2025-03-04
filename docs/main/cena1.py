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

# Dicionário para armazenar os balões por personagem
baloes = {}

def fala(personagem: turtle.Turtle, texto: str, angulo: int = 45, distancia: int = 50, tempo: float = 5):
    """Exibe um balão de fala para um personagem e o remove automaticamente após um tempo."""
    
    if not isinstance(personagem, turtle.Turtle):
        print("Erro: personagem passado não é um objeto Turtle!")
        return

    # Criar uma turtle para o balão de fala
    balao = turtle.Turtle()
    balao.hideturtle()
    balao.speed(0)

    # Obter posição do personagem
    x, y = personagem.pos()

    # Criar a linha do balão
    balao.penup()
    balao.goto(x, y)
    balao.pendown()
    balao.setheading(angulo)
    balao.forward(distancia)

    # Posicionar o texto do balão
    texto_x, texto_y = balao.pos()
    balao.penup()
    balao.goto(texto_x, texto_y + 10)
    balao.write(texto, align="left", font=("Arial", 12, "bold"))

    # Armazena o balão no dicionário para referência posterior
    baloes[personagem] = balao

    # Agendar remoção automática após o tempo especificado
    turtle.ontimer(lambda: apagar_balao(personagem), int(tempo * 1000))

def apagar_balao(personagem: turtle.Turtle):
    """Apaga o balão de fala do personagem especificado."""
    if personagem in baloes:
        baloes[personagem].clear()  # Apaga o texto e o traço do balão
        baloes[personagem].hideturtle()  # Esconde a tartaruga do balão
        del baloes[personagem]  # Remove o balão do dicionário para liberar memória

def cena1():
    turtle.setup(1110,694)
    
    # Definir fundo
    try:
        turtle.bgpic(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\fundos\fundo2.gif")
    except:
        print("Erro: fundo2.gif não encontrado!")

    bmo = turtle.Turtle()
    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\bmo.gif")
        bmo.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\bmo.gif")
        # Tentar diminuir o tamanho do "shape" (não afeta imagem gif, mas afeta a tartaruga)
        bmo.shapesize(stretch_wid=0.1, stretch_len=0.1)  # Tentando diminuir a tartaruga
    except:
        print("Erro: bmo.gif não encontrado!")

    bmo.hideturtle()
    bmo.up() 
    bmo.goto(x=459, y=-138)
    bmo.down()
    bmo.showturtle()

    # Criar personagem
    finnEjake = turtle.Turtle()

    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
        finnEjake.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
        finnEjake.shapesize(stretch_wid=0.1, stretch_len=0.1)
    except:
        print("Erro: finnEjake.gif não encontrado!")

    finnEjake.up()

    # Função de movimentação com loop while
    def mover_com_while(personagem):
        """Move o personagem entre as coordenadas usando um loop while com delay."""
        
        coordenadas = [(-543, -187), (-239, -197), (449, -142)]  # Lista de coordenadas
        index = 0  # Índice para acompanhar a posição da lista

        def mover():
            nonlocal index
            if index < len(coordenadas):
                x, y = coordenadas[index]
                personagem.goto(x, y)
                index += 1
                turtle.ontimer(mover, 1000)  # Atraso de 1 segundo para o próximo movimento

        mover()  # Chama a função de movimento pela primeira vez

    # Iniciar o movimento
    mover_com_while(finnEjake)

    # Falas
    turtle.ontimer(lambda: fala(finnEjake, "Eai, BMO! como vai, cara?"), 5000)
    turtle.ontimer(lambda: apagar_balao(finnEjake), 11000)

    turtle.ontimer(lambda: fala(bmo, "Olá, garotos. Eu estou bem... apenas relaxando."), 11000)
    turtle.ontimer(lambda: apagar_balao(bmo), 17000)

    turtle.ontimer(lambda: fala(bmo, "Vocês deviam se juntar a mim."), 17000)
    turtle.ontimer(lambda: apagar_balao(bmo), 23000)

    turtle.ontimer(lambda: fala(finnEjake, "Obrigado, BMO."), 23000)
    turtle.ontimer(lambda: apagar_balao( finnEjake),26000 )
    turtle.ontimer(lambda: fala(finnEjake , "Porém, estamos procurando a Lady Rainicorn e a princesa Jujuba."), 2600)
    turtle.ontimer(lambda: apagar_balao(finnEjake),32000 )
    turtle.ontimer(lambda: fala(finnEjake, "Por acaso você não as viu por aqui?"),32000 )
    turtle.ontimer(lambda: apagar_balao(finnEjake ),35000 )

    turtle.ontimer(lambda: fala( bmo, ""), )
    turtle.ontimer(lambda: apagar_balao( ), )
    turtle.ontimer(lambda: fala( , ""), )
    turtle.ontimer(lambda: apagar_balao( ), )
    turtle.ontimer(lambda: fala( , ""), )
    turtle.ontimer(lambda: apagar_balao( ), )
    turtle.ontimer(lambda: fala( , ""), )
    turtle.ontimer(lambda: apagar_balao( ), )
    turtle.ontimer(lambda: fala( , ""), )
    turtle.ontimer(lambda: apagar_balao( ), )
    turtle.ontimer(lambda: fala( , ""), )
    turtle.ontimer(lambda: apagar_balao( ), )
    turtle.ontimer(lambda: fala( , ""), )
    turtle.ontimer(lambda: apagar_balao( ), )
    turtle.ontimer(lambda: fala( , ""), )
    turtle.ontimer(lambda: apagar_balao( ), )

    # Manter a janela aberta
    turtle.done()

# Chamar a função
cena1()
