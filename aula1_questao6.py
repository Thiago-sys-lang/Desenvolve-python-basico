N = int(input("Digite a quantidade de experimentos registrados: "))

total_cobaias = 0
cobaias_tipo = {'S': 0, 'R': 0, 'C': 0}

for _ in range(N):
    quantidade, tipo = input("Digite a quantidade e o tipo de cobaia (S, R ou C): ").split()
    quantidade = int(quantidade)
    total_cobaias += quantidade
    cobaias_tipo[tipo] += quantidade

print(f"Total: {total_cobaias} cobaias")

for tipo, quantidade in cobaias_tipo.items():
    print(f"Total de {tipo.lower()}s: {quantidade}")
    percentual = (quantidade / total_cobaias) * 100
    print(f"Percentual de {tipo.lower()}s: {percentual:.2f}%")
