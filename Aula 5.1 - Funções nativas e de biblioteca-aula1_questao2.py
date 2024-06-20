import random
from math import sqrt

def calcular_raiz_soma(n):
    valores = [random.randint(0, 100) for _ in range(n)]
    soma = sum(valores)
    raiz_soma = sqrt(soma)
    return raiz_soma

try:
    n = int(input("Digite o valor de n: "))
    if n <= 0:
        print("Por favor, insira um valor inteiro positivo para n.")
    else:
        raiz_soma = calcular_raiz_soma(n)
        print(f"A raiz quadrada da soma dos {n} valores inteiros aleatórios é: {raiz_soma:.2f}")

except ValueError:
    print("Por favor, insira um valor inteiro válido para n.")
