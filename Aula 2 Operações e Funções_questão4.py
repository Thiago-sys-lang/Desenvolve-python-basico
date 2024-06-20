def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    tamanho_menor = min(len(lista1), len(lista2))

    for i in range(tamanho_menor):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])

    if len(lista1) > len(lista2):
        lista_intercalada.extend(lista1[tamanho_menor:])
    else:
        lista_intercalada.extend(lista2[tamanho_menor:])

    return lista_intercalada

# Recebendo as duas listas do usuário
lista1 = []
lista2 = []

num_elementos_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
print("Digite os elementos da lista 1:")
for _ in range(num_elementos_lista1):
    elemento = int(input())
    lista1.append(elemento)

num_elementos_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
print("Digite os elementos da lista 2:")
for _ in range(num_elementos_lista2):
    elemento = int(input())
    lista2.append(elemento)

# Intercalando as duas listas
lista_intercalada = intercalar_listas(lista1, lista2)

# Imprimindo a lista intercalada
print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))
