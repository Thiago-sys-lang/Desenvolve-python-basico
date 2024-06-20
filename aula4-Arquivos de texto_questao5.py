import csv

# Lista de livros com suas informações
livros = [
    ["Título 1", "Autor 1", 2001, 300],
    ["Título 2", "Autor 2", 2002, 320],
    ["Título 3", "Autor 3", 2003, 250],
    # Adicione mais livros conforme necessário
]

# Nome do arquivo CSV
nome_arquivo_csv = "meus_livros.csv"

# Cria e escreve no arquivo CSV
with open(nome_arquivo_csv, "w", newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    escritor_csv.writerows(livros)

print(f"Arquivo '{nome_arquivo_csv}' criado com sucesso.")
