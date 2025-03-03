# main.main()

"""
Esta é a função principal de sua animação.

O propósito dela é oferecer um laço no qual o usuário possa escolher qual cena ele deseja ver.

Altere a função de acordo com necessidade de seu grupo.

O ideal é que você reescreva esta função do zero.
"""

def main():

    animaivos.nucleo.carrega_personagens()    
    print("Os seguintes personagens foram carregados:")
    formas_gif = [forma for forma in turtle.getshapes() if forma.endswith('.gif')]
    print('\n'.join(formas_gif))

    op = int(input(animaivos.menus.menu_principal))
    while op != 5:
        if op == 1:
            cena1()
        elif op == 2:
            cena2()
        elif op == 3:
            cena3()
        elif op == 4:
            cena4()
        else:
            print("Opção inválida.")

        op = int(input(animaivos.menus.menu_principal))


