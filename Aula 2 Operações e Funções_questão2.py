import random

# Gerando aleatoriamente o número de elementos entre 5 e 20
num_elementos = random.randint(5, 20)

# Gerando aleatoriamente os valores entre 1 e 10 e armazenando na lista elementos
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Imprimindo a lista elementos
print("Lista elementos:", elementos)

# Calculando a soma dos valores da lista
soma_valores = sum(elementos)
print("Soma dos valores:", soma_valores)

# Calculando a média dos valores da lista
media_valores = soma_valores / num_elementos
print("Média dos valores:", media_valores)
