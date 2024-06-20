import random

# Gerando 20 valores inteiros aleatórios entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Criando uma cópia da lista original para ordenar
valores_ordenados = sorted(valores)

# Imprimindo a lista ordenada
print("Lista ordenada:", valores_ordenados)

# Imprimindo a lista original
print("Lista original:", valores)

# Encontrando o índice do maior valor da lista
indice_maior = valores.index(max(valores))
print("Índice do maior valor:", indice_maior)

# Encontrando o índice do menor valor da lista
indice_menor = valores.index(min(valores))
print("Índice do menor valor:", indice_menor)
