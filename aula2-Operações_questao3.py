import string

def limpar_frase(frase):
    # Remove espaços em branco e sinais de pontuação, e converte para minúsculas
    return ''.join(char.lower() for char in frase if char.isalnum())

def verificar_palindromo(frase):
    frase_limpa = limpar_frase(frase)
    return frase_limpa == frase_limpa[::-1]

while True:
    # Solicita ao usuário que digite uma frase
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    # Verifica se o usuário deseja encerrar o programa
    if frase.lower() == "fim":
        break
    
    # Verifica se a frase é um palíndromo
    if verificar_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
