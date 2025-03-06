import subprocess
import os
import sys

menu_principal = """
Escolha uma cena para executar:
1 - Cena 1
2 - Cena 2
3 - Cena 3
4 - Cena 4
5 - Sair
Digite sua opção: """

def main():
    # Pasta onde os arquivos de cena estão (relativa ao script atual)
    pasta_cenas = "docs/main"
    
    # Cria um dicionário associando as opções às cenas
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
            # Constrói o caminho relativo para o arquivo da cena
            caminho_cena = os.path.join(, cenas[op])
            
            if os.path.exists(caminho_cena):  # Verifica se o arquivo existe
                print(f"Executando {cenas[op]}...\n")
                
                # Usando sys.executable para garantir que o Python correto seja utilizado
                subprocess.run([sys.executable, caminho_cena])  # Executa e aguarda
            else:
                print(f"Erro: Arquivo {cenas[op]} não encontrado no diretório {pasta_cenas}.")
        else:
            print("Opção inválida! Escolha um número entre 1 e 5.")

# Executa a função principal
if __name__ == "__main__":
    main()
