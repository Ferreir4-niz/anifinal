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
        1: "cena1.py",
        2: "cena2.py",
        3: "cena3.py",
        4: "cena4.py"
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
            script_path = os.path.join(os.path.dirname(__file__), cenas[op])  # Caminho relativo
            if os.path.exists(script_path):  # Verifica se o arquivo existe
                print(f"Executando {script_path}...\n")
                subprocess.run(["python", script_path])  # Executa e aguarda
            else:
                print(f"Erro: Arquivo {script_path} não encontrado.")
        else:
            print("Opção inválida! Escolha um número entre 1 e 5.")

# Executa a função principal
if __name__ == "__main__":
    main()