import random

# Função para imprimir o enforcado
def imprime_enforcado(erros):
    with open("gabarito_enforcado.txt", "r") as arquivo:
        estagios = arquivo.read().split("\n\n")
    print(estagios[erros])

# Carregar palavras do arquivo "gabarito_forca.txt"
with open("gabarito_forca.txt", "r") as arquivo:
    palavras = arquivo.read().splitlines()

# Escolher uma palavra aleatória
palavra_secreta = random.choice(palavras).lower()
tentativas = 6
letras_adivinhadas = ["_"] * len(palavra_secreta)
letras_erradas = []

print(" ".join(letras_adivinhadas))

# Jogo da forca
while tentativas > 0 and "_" in letras_adivinhadas:
    letra = input("Digite uma letra: ").lower()
    if letra in palavra_secreta:
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                letras_adivinhadas[i] = letra
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        imprime_enforcado(len(letras_erradas))

    print(" ".join(letras_adivinhadas))

if "_" not in letras_adivinhadas:
    print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)
