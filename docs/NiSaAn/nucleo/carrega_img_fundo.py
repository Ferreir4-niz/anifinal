# animaivos.nucleo.carrega_img_fundo()

import turtle

def carrega_img_fundo(img_fundo: str):
    """Carrega uma imagem de fundo para a tela.

    Carrega uma imagem de fundo para a tela, que é um arquivo `.gif`
    ou um arquivo `.png` presente no diretório `animaivos/fundos/`.

    Args:
        img_fundo (str): Imagem de plano de fundo que será carregada.
    """

    cam_img_fundo = Path(__file__).parent / "fundos" / img_fundo

    if cam_img_fundo.exists() and cam_img_fundo.is_file():
        turtle.bgpic(cam_img_fundo.as_posix())
    else:
        print(cam_img_fundo.as_posix())
        print('Imagem de fundo não encontrada!')

