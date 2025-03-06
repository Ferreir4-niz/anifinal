nomes_arquivos = ["cena1.py", "cena2.py", "cena3.py", "cena4.py"]

conteudo = """print("Executando {}")\n"""

for nome in nomes_arquivos:
    with open(nome, "w") as arquivo:
        arquivo.write(conteudo.format(nome))  # Escreve um print com o nome do arquivo
    print(f"{nome} criado com sucesso!")
dir
