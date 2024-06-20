# escreva uma expressão que avalie com base no gênero, na idade e no tempo de serviço, se uma pessoa já pode se aposentar, regras:
#A: Para mulheres ter mais de 60 anos, para homens, 65.
#B: ou ter trabalhado pelo menos 30 anos 
#C: ou ter 60 anos e trabalhando pelo menos 25.

#entrada de dados 
#genero, idade e tempo de serviço 
genero = input()
idade = int(input())
tempo = int(input())

#processmento 
#A: Para mulheres ter mais de 60 anos. para homens, 65.
# B: ou ter trabalhado pelo menos 30 anos 
# C: ou ter 60 anos e trabalhando pelo menos 25.
# genero = f | idade > 65 | genero f and idade > 65
a = (genero == 'f' and idade >= 60) or \
    (genero == 'm' and idade >= 65)
b = tempo > 30 
c = idade >= 60 and tempo >=25
pode_aposentar = a or b or c 

#saida
print (a, b, c, pode_aposentar)

#resultado
#f
# 63
# 30
# true false true true
