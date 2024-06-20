import random

# Função para criptografar uma lista de nomes
def encrypt(nomes):
    # Gera uma chave de criptografia aleatória entre 1 e 10
    n = random.randint(1, 10)
    nomes_criptografados = []

    # Criptografa cada nome na lista
    for nome in nomes:
        nome_cript = ''.join(chr((ord(char) - 33 + n) % 94 + 33) for char in nome)
        nomes_criptografados.append(nome_cript)

    return nomes_criptografados, n

# Lista de nomes
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

# Criptografa os nomes
nomes_criptografados, chave_aleatoria = encrypt(nomes)

# Exibe os nomes criptografados e a chave de criptografia
print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_criptografados}")
