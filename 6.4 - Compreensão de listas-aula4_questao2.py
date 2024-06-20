# Solicitar uma frase ao usuário
frase = input("Digite uma frase: ")

# List comprehension para obter as vogais e as consoantes
vogais = [char.lower() for char in frase if char.lower() in 'aeiou']
consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']

# Ordenar a lista de vogais
vogais.sort()

print("Vogais:", vogais)
print("Consoantes:", consoantes)
