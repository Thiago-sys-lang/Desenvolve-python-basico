n = int(input("Digite a quantidade de números a serem lidos: "))
maior = 0
while n > 0:
    x = int(input("Digite um número: "))
    if x > maior:
        maior = x
        n = n - 1
    print(maior)
    
