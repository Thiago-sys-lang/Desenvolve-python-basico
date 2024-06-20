# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Lista de domínios extraídos
dominios = [url[4:-4] for url in urls]

# Exibe a lista de domínios
print("Domínios:", dominios)
