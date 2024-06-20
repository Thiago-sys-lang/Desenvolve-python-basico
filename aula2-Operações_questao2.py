# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Lista de vogais
vogais = "aeiouAEIOU"

# Substitui cada vogal na frase por '*'
frase_modificada = ''.join('*' if char in vogais else char for char in frase)

# Exibe a frase modificada
print("Frase modificada:", frase_modificada)
