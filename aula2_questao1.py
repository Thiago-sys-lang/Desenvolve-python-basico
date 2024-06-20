 
# EXERCICIOS 
# Juliana e cris querem entra em um bar, mas só podem se ambos forem maior de idade [>17].
# escreva um programa que pergunte suas idades e impirma true se puderem entrar e false caso contrário.

# entrada de dados 
#idade de juliana 
# idade de cris 
idade_juliana = int(input("Digite a idade da Juliana: "))
idade_cris = int(input("Digite a idade da Cris: "))

#processamento 
# true se ambos forem maior de idade / se pelo menos um for maior de idade 
# <exp1> juliana é maior de idade 
# <exp2> cris é maior de idade 
# <exp1> and <exp2>
# false em qualquer outro caso

pode_entrar = resultado =  idade_juliana >= 18 and idade_cris >= 18 
#saida
print(pode_entrar)