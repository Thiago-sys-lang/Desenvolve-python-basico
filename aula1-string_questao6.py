from collections import Counter

# Solicita uma frase e a palavra objetivo do usuário
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

# Função para verificar se duas palavras são anagramas
def sao_anagramas(palavra1, palavra2):
    return Counter(palavra1) == Counter(palavra2)

# Inicializa a lista de anagramas encontrados
anagramas = []

# Percorre a frase para encontrar anagramas
palavras = frase.split()
for palavra in palavras:
    if sao_anagramas(palavra, palavra_objetivo):
        anagramas.append(palavra)

# Exibe os anagramas encontrados
print(f"Anagramas: {anagramas}")
