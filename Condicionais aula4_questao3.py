# Solicita o ano ao usuário
ano = int(input("Insira um ano: "))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")

# Testando com os valores fornecidos
testes = [1900, 2000, 2016, 2017]
for ano in testes:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano}: Bissexto")
    else:
        print(f"{ano}: Não Bissexto")
