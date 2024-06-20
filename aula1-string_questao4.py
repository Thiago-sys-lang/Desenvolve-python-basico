# Solicita o número de celular do usuário
numero = input("Digite o número: ")

# Verifica o comprimento do número e ajusta se necessário
if len(numero) == 8:
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":
    numero = "9" + numero

# Adiciona o separador "-" e exibe o número completo
numero_formatado = numero[:5] + "-" + numero[5:]
print(f"Número completo: {numero_formatado}")
