# Lista com os nomes dos meses por extenso
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Solicita a data de nascimento ao usuário
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Divide a data em dia, mês e ano
dia, mes, ano = data_nascimento.split('/')

# Converte o mês de string para inteiro e ajusta o índice da lista
mes = int(mes) - 1

# Exibe a data de nascimento com o nome do mês por extenso
print(f"Você nasceu em {dia} de {meses[mes]} de {ano}.")
