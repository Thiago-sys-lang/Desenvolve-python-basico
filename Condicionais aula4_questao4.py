# Solicita a distância e o peso do pacote
distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))

# Calcula o valor do frete baseado nas regras fornecidas
if distancia <= 100:
    custo_por_kg = 1.0
elif distancia <= 300:
    custo_por_kg = 1.5
else:
    custo_por_kg = 2.0

# Calcula o custo base do frete
frete = custo_por_kg * peso

# Adiciona taxa extra se o peso for superior a 10 kg
if peso > 10:
    frete += 10

# Imprime o valor do frete
print(f"O valor do frete é: R${frete:.2f}")
