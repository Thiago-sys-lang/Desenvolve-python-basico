def calcular_diferenca_absoluta(num1, num2):
    diferenca = abs(num1 - num2)
    return round(diferenca, 2)

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    diferenca_absoluta = calcular_diferenca_absoluta(num1, num2)
    print("A diferença absoluta entre os números é:", diferenca_absoluta)

except ValueError:
    print("Por favor, insira números válidos.")


