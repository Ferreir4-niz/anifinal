# animaivos.nucleo.habilita_clique()

import turtle

def habilita_clique() -> None:
    """Habilita o clique do mouse na tela.
    """

    tela = turtle.Screen()
    tela.title("Clique para ver as coordenadas do mouse")
    tela.onclick(exibir_coordenadas)

