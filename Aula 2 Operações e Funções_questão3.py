import random
from collections import Counter

# Preenchendo as duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Encontrando a interseção entre as duas listas
interseccao = list(set(lista1) & set(lista2))

# Ordenando a lista de interseção
interseccao.sort()

# Imprimindo ambas as listas
print("lista1 -", lista1)
print("lista2 -", lista2)

# Imprimindo a lista de interseção
print("Interseccao -", interseccao)

# Contando a quantidade de vezes que cada elemento aparece em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

print("Contagem:")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem_lista1[elemento]}, lista2={contagem_lista2[elemento]})")
