import random

# Gera uma lista com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Exibe a lista original
print("Original:", lista)

# Encontra o intervalo com a maior quantidade de números negativos
max_negativos = 0
start_index = 0

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        sublista = lista[i:j]
        negativos = sum(1 for num in sublista if num < 0)
        if negativos > max_negativos:
            max_negativos = negativos
            start_index = i
            end_index = j

# Remove o intervalo da lista
del lista[start_index:end_index]

# Exibe a lista editada
print("Editada:", lista)
