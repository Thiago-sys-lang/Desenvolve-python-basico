import random
from math import sqrt

def calcular_raiz_quadrada_soma(valores):
    soma = sum(valores)
    raiz_quadrada = sqrt(soma)
    return raiz_quadrada

try:
    n = int(input("Digite o valor de n: "))
    valores_aleatorios = [random.randint(0, 100) for _ in range(n)]
    
    raiz_quadrada_soma = calcular_raiz_quadrada_soma(valores_aleatorios)
    
    print("Os valores aleatórios gerados são:", valores_aleatorios)
    print("A raiz quadrada da soma dos valores é:", raiz_quadrada_soma)

except ValueError:
    print("Por favor, insira um valor inteiro válido para n.")
