# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Define as vogais
vogais = "aeiouAEIOU"

# Inicializa a contagem e a lista de índices
contagem_vogais = 0
indices_vogais = []

# Percorre a frase para encontrar as vogais e seus índices
for i, letra in enumerate(frase):
    if letra in vogais:
        contagem_vogais += 1
        indices_vogais.append(i)

# Exibe a contagem de vogais e seus índices
print(f"{contagem_vogais} vogais")
print(f"Índices {indices_vogais}")
