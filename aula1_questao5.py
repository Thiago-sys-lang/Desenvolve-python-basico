N = int(input("Digite a quantidade de respondentes: "))

soma_idades = 0

for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i+1}: "))
    soma_idades += idade

media_idades = soma_idades / N

print(f"A média das idades dos respondentes é: {media_idades}")
