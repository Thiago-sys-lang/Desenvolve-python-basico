import csv

# Abrir o arquivo "spotify-2023.csv" para leitura
with open("spotify-2023.csv", "r", encoding='latin-1') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    musicas_por_ano = {}

    # Processar cada linha do arquivo
    for linha in leitor_csv:
        ano = int(linha["released_year"])
        if 2012 <= ano <= 2022:
            streams = int(linha["streams"])
            if ano not in musicas_por_ano or streams > musicas_por_ano[ano]["streams"]:
                musicas_por_ano[ano] = {
                    "track_name": linha["track_name"],
                    "artist(s)_name": linha["artist(s)_name"],
                    "released_year": ano,
                    "streams": streams
                }

# Criar lista final com as músicas mais tocadas de cada ano
musicas_mais_tocadas = [
    [info["track_name"], info["artist(s)_name"], info["released_year"], info["streams"]]
    for ano, info in sorted(musicas_por_ano.items())
]

# Imprimir a lista produzida
print(musicas_mais_tocadas)
