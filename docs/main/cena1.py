import turtle
import time

def fala(personagem: turtle.Turtle, 
         texto: str, 
         angulo: int = 45, 
         distancia: int = 150,
         tempo: float = 5):
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
        turtle.bgpic(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\fundos\fundo2.png")
 # Certifique-se de que o arquivo está na pasta correta
    except:
        print("Erro: fundo2.gif não encontrado!")

    # Criar personagem
    finnEjake = turtle.Turtle()
    finnEjake.up()
    
    # Registrar e definir imagem
    try:
        turtle.addshape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
        finnEjake.shape(r"C:\Users\nick\Documents\GitHub\anifinal\NiSaAn.py\personagens\finnEjake.gif")
    except:
        print("Erro: finnEjake.gif não encontrado!")

    # Movimentação
    finnEjake.goto(-MEIA_LARG, 0)
    finnEjake.goto(0, 0)

    # Exibir texto
    turtle.write("Olá!")

    # Manter a janela aberta
    turtle.done()

# Chamar a função
cena1()
