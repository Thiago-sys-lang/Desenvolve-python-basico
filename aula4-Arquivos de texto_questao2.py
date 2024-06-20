import re

# Abre e lê o arquivo "frase.txt"
with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()

# Remove espaços em branco e caracteres não alfabéticos, separa palavras
palavras = re.findall(r'\b[a-zA-Z]+\b', conteudo)

# Salva as palavras no arquivo "palavras.txt", cada uma em uma linha
with open("palavras.txt", "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Lê e imprime o conteúdo do arquivo "palavras.txt"
with open("palavras.txt", "r") as arquivo:
    conteudo_palavras = arquivo.read()

print(conteudo_palavras)
