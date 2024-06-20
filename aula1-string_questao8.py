# Função para validar o CPF
def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf_numeros = [int(char) for char in cpf if char.isdigit()]

    # Verifica se o CPF tem 11 dígitos
    if len(cpf_numeros) != 11:
        return "Inválido"

    # Calcula o primeiro dígito verificador
    soma = sum(cpf_numeros[i] * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Calcula o segundo dígito verificador
    soma = sum(cpf_numeros[i] * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # Verifica se os dígitos calculados correspondem aos dígitos do CPF
    if digito1 == cpf_numeros[9] and digito2 == cpf_numeros[10]:
        return "Válido"
    else:
        return "Inválido"

# Solicita o CPF do usuário
cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

# Verifica e exibe se o CPF é válido ou inválido
print(validar_cpf(cpf))
