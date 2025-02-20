"""
Módulo principal
"""

from nisaan.menus import menu_principal

def cena1():
    pass

def cena2():
    pass

def cena3():
    pass 

def cena4():
    
    pass

def main():
    op = int(input(menu_principal))
    while op != 5:
        if op ==1:
            cena1()
        elif op==2:
            cena2()
        elif op==3:
            cena3()
        elif op==4:
            cena4()
        else:
            print("opção inválida")

op = int(input(menu_principal))

main()