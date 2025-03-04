# animaivos.nucleo.carrega_personagens()

import turtle


def carrega_personagens():
    """Carrega os personagens da animação.

    Carrega os personagens da animação, que são arquivos `.gif`
    presentes no diretório `animaivos/personagens/`.
    """

    cam_personagens = Path(__file__).parent / "personagens"
    cam_atual = Path.cwd()

    os.chdir(cam_personagens.as_posix())
    for img in glob("*.gif"):
        turtle.register_shape(img)

    os.chdir(cam_atual.as_posix())
