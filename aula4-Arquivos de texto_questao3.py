# Baixe o arquivo "estomago.txt" no seu computador antes de executar este script

# Abrir o arquivo "estomago.txt" para leitura
import re


with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Imprimir as primeiras 25 linhas
print("Texto das primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.strip())

# Número de linhas do arquivo
num_linhas = len(linhas)
print(f"Número de linhas do arquivo: {num_linhas}")

# Linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print(f"Linha com maior número de caracteres ({len(linha_maior.strip())} caracteres):\n{linha_maior.strip()}")

# Contar menções aos nomes "Nonato" e "Íria"
contagem_nonato = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
contagem_iria = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))
print(f"Número de menções ao personagem 'Nonato': {contagem_nonato}")
print(f"Número de menções ao personagem 'Íria': {contagem_iria}")
