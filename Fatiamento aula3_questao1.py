# Solicita ao usuário pelo menos 4 números inteiros
numeros = []
while len(numeros) < 4:
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)
    continuar = input("Deseja continuar inserindo números? (s/n): ")
    if continuar.lower() != 's' and len(numeros) >= 4:
        break

# Exibe a lista original
print("Lista original:", numeros)

# Exibe os 3 primeiros elementos
print("Os 3 primeiros elementos:", numeros[:3])

# Exibe os 2 últimos elementos
print("Os 2 últimos elementos:", numeros[-2:])

# Exibe a lista invertida
print("Lista invertida:", numeros[::-1])

# Exibe os elementos de índice par
print("Elementos de índice par:", numeros[::2])

# Exibe os elementos de índice ímpar
print("Elementos de índice ímpar:", numeros[1::2])
