from datetime import datetime

data_hora_atual = datetime.now()

data_formatada = f"{data_hora_atual.day:02}/{data_hora_atual.month:02}/{data_hora_atual.year}"
hora_formatada = f"{data_hora_atual.hour:02}:{data_hora_atual.minute:02}"

print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")
