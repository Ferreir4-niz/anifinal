import subprocess
import os

menu_principal = """
Escolha uma cena para executar:
1 - Cena 1
2 - Cena 2
3 - Cena 3
4 - Cena 4
5 - Sair
Digite sua opção: """

def main():
    cenas = {
        1: r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\docs\\main\\cena1.py",
        2: r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\docs\\main\\cena2.py",
        3: r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\docs\\main\\cena3.py",
        4: r"C:\\Users\\nick\\Documents\\GitHub\\anifinal\\docs\\main\\cena4.py"
    }

    while True:
        try:
            op = int(input(menu_principal))  # Solicita a opção ao usuário
        except ValueError:
            print("Opção inválida! Digite um número entre 1 e 5.")
            continue  # Retorna ao menu

        if op == 5:
            print("Saindo...")
            break  # Sai do loop

        if op in cenas:
            if os.path.exists(cenas[op]):  # Verifica se o arquivo existe
                print(f"Executando {cenas[op]}...\n")
                subprocess.run(["python", cenas[op]])  # Executa e aguarda
            else:
                print(f"Erro: Arquivo {cenas[op]} não encontrado.")
        else:
            print("Opção inválida! Escolha um número entre 1 e 5.")

# Executa a função principal
if __name__ == "__main__":
    main()
