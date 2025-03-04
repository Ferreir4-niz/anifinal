# animaivos.nucleo.exibir_coordenadas()

"""Função utilizada para exibir as coordenadas quando o usuário clicar com o mouse em determinada posição da janela criada pelo módulo `turtle`. Esta função é chamada quando você utilizar a função [habilita_clique()](habilita_clique.md)."""

import turtle

def exibir_coordenadas(x: float, y: float) -> None:
    """Exibe as coordenadas de um clique do mouse.

    Args:
        x (float): Coordenada `x` do clique do mouse.
        y (float): Coordenada `y` do clique do mouse.
    """

    print(f"Coordenadas do clique: x={x:0.0f}, y={y:0.0f}")

    # Exibe as coordenadas na tela com o turtle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"x={x:0.0f}, y={y:0.0f}", align="center")
    turtle.stamp()
