import datetime

# Obter a data e hora atuais
data_hora_atual = datetime.datetime.now()

# Extrair os componentes de data e hora
dia = data_hora_atual.day
mes = data_hora_atual.month
ano = data_hora_atual.year
hora = data_hora_atual.hour
minuto = data_hora_atual.minute

# Formatar a data e hora para o formato desejado
data_formatada = f"{dia:02}/{mes:02}/{ano}"
hora_formatada = f"{hora:02}:{minuto:02}"

# Exibir a data e hora formatadas
print("Data:", data_formatada)
print("Hora:", hora_formatada)
