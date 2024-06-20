3.5 - Decisões Múltiplas
Q1.
Vamos fazer uma calculadora! Escreva um programa que solicita 3 entradas: o primeiro operando (float), o operador (caracter) e o segundo operando (float). Seu programa deve imprimir o resultado da operação solicitada, entre soma (+), subtração (-), divisão (/), multiplicação (*) ou potência (**). Seu programa também deve imprimir uma mensagem de erro se a operação solicitada não estiver dentre as opções disponíveis.

Seguem alguns exemplos de interação com seu código no terminal.

Digite o primeiro operando: 5.2
Digite o operador (+, -, /, *, **): *
Digite o segundo operando` 3
Resultado: 5.2 * 3.0 = 15.6
Digite o primeiro operando: 8
Digite o operador (+, -, /, *, **): **
Digite o segundo operando: 2
Resultado: 8.0 * 2.0 = 64.0
Digite o primeiro operando: 7
Digite o operador (+, -, /, *, **): %
Digite o segundo operando: 3.4
Erro! Operação inválida. 
Digite o primeiro operando: 10
Digite o operador (+, -, /, *, **): /
Digite o segundo operando: 2.5
Resultado: 10.0 / 2.5 = 4.0



#resposta Q1
# Solicita as entradas do usuário
primeiro_operando = float(input("Digite o primeiro operando: "))
operador = input("Digite o operador (+, -, /, *, **): ")
segundo_operando = float(input("Digite o segundo operando: "))

# Realiza a operação de acordo com o operador fornecido
if operador == '+':
    resultado = primeiro_operando + segundo_operando
elif operador == '-':
    resultado = primeiro_operando - segundo_operando
elif operador == '/':
    if segundo_operando == 0:
        print("Erro! Divisão por zero.")
        exit()
    else:
        resultado = primeiro_operando / segundo_operando
elif operador == '*':
    resultado = primeiro_operando * segundo_operando
elif operador == '**':
    resultado = primeiro_operando ** segundo_operando
else:
    print("Erro! Operação inválida.")
    exit()

# Imprime o resultado
print(f"Resultado: {primeiro_operando} {operador} {segundo_operando} = {resultado}")








Q2.
Escreva um programa que leia os comprimentos dos 3 lados de um triângulo e diga se o triângulo é equilátero, isóceles ou escaleno. Regras:

Isóceles: Quaisquer dois lados com o mesmo comprimento
Equilátero: Os três lados tem o mesmo comprimento
Escaleno: Três lados de comprimento diferente
Note que a ordem das condições importa! Seguem alguns exemplos de interação com seu código no terminal.

Digite o comprimento do lado 1: 4
Digite o comprimento do lado 2: 4
Digite o comprimento do lado 3: 6
Triângulo: Isóceles
Digite o comprimento do lado 1: 5
Digite o comprimento do lado 2: 5
Digite o comprimento do lado 3: 5
Triângulo: Equilátero
Digite o comprimento do lado 1: 7
Digite o comprimento do lado 2: 4
Digite o comprimento do lado 3: 9
Triângulo: Escaleno




#resposta Q2
# Solicita os comprimentos dos lados do triângulo
lado1 = float(input("Digite o comprimento do lado 1: "))
lado2 = float(input("Digite o comprimento do lado 2: "))
lado3 = float(input("Digite o comprimento do lado 3: "))

# Verifica o tipo de triângulo
if lado1 == lado2 == lado3:
    print("Triângulo: Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo: Isóceles")
else:
    print("Triângulo: Escaleno")





Q3.
Você está desenvolvendo um sistema de avaliação de desempenho para um jogo. Escreva um programa em Python que avalia a pontuação do jogador em uma missão e atribui uma classificação com base nas seguintes condições:

Se a pontuação for menor que 70, atribua a classificação "Insatisfatório".
Se a pontuação for maior ou igual a 70, atribua a classificação "Regular".
Se a pontuação for maior ou igual a 80, atribua a classificação "Bom".
Se a pontuação for maior ou igual a 90, atribua a classificação "Excelente".
Escreva um programa que solicita ao usuário a pontuação e imprime a classificação correspondente.




#resposta Q3
# Solicita a pontuação do jogador
pontuacao = int(input("Digite a pontuação do jogador: "))

# Atribui a classificação com base na pontuação
if pontuacao < 70:
    print("Classificação: Insatisfatório")
elif pontuacao < 80:
    print("Classificação: Regular")
elif pontuacao < 90:
    print("Classificação: Bom")
else:
    print("Classificação: Excelente")




Q4.
Você está implementando um sistema de desconto em uma loja online. Escreva um programa em Python que calcula o desconto com base no valor total da compra e atribui diferentes níveis de desconto de acordo com as seguintes condições:

Se o valor total da compra for menor que R$ 50, não há desconto.
Se o valor total da compra for maior ou igual a R$ 50, atribua um desconto de 10%.
Se o valor total da compra for maior ou igual a R$ 100, atribua um desconto de 20%.
Seguem alguns exemplos de interação com seu código no terminal. Preste atenção na formatação esperada para as saídas.

Digite o valor total da compra: 120
Desconto aplicado: 20.0%
Valor final com desconto: R$96.00
Digite o valor total da compra: 65
Desconto aplicado: 10.0%
Valor final com desconto: R$58.50
Digite o valor total da compra: 40
Desconto aplicado: 0.0%
Valor final com desconto: R$40.00




#resposta Q4
# Solicita o valor total da compra
valor_compra = float(input("Digite o valor total da compra: "))

# Calcula o desconto com base no valor total da compra
if valor_compra < 50:
    desconto = 0
elif valor_compra < 100:
    desconto = 10
else:
    desconto = 20

# Calcula o valor final com desconto
valor_desconto = valor_compra * (desconto / 100)
valor_final = valor_compra - valor_desconto

# Imprime o desconto aplicado e o valor final com desconto
print(f"Desconto aplicado: {desconto}%")
print(f"Valor final com desconto: R${valor_final:.2f}")





Q5.
Você está projetando um sistema de autenticação baseado na análise da íris (parte colorida do olho). Ao acionado, o sistema coleta e retorna 3 valores inteiros referentes a atributos da íris visível. Mas o sistema não é perfeito, tendo uma margem de erro do sensor de +/- 
.

O código abaixo tem os atributos dos 4 usuários cadastrados no sistema. Você deve completar om código, pedindo ao usuário para inserir uma nova leitura de padrão de íris. O programa deve comparar o padrão inserido com os padrões cadastrados no banco de dados. Se o padrão estiver dentro da tolerância estabelecida, o usuário é autenticado com sucesso. Caso contrário, a autenticação falha.

Dica: A função do python abs() retorna o valor absoluto de um elemento. Ex:

>>> print(abs(987-982))
5
>>> print(abs(987-992))
5
Seguem alguns exemplos de interação com seu código no terminal.

Insira o padrão de íris para autenticação.
Atributo 1: 111
Atributo 2: 222
Atributo 3: 333
Autenticação bem-sucedida! 
Usuário: 3
Insira o padrão de íris para autenticação.
Atributo 1: 111
Atributo 2: 200
Atributo 3: 333
Autenticação falhou! 
Insira o padrão de íris para autenticação.
Atributo 1: 982
Atributo 2: 653
Atributo 3: 324
Autenticação bem-sucedida! 
Usuário: 2
## Não altere os atributos definidos a seguir
iris1_a1, iris1_a2, iris1_a3 = 123, 456, 789
iris2_a1, iris2_a2, iris2_a3 = 987, 654, 321
iris3_a1, iris3_a2, iris3_a3 = 111, 222, 333
iris4_a1, iris4_a2, iris4_a3 = 444, 555, 666





#resposta Q5
# Atributos dos usuários cadastrados
iris1_a1, iris1_a2, iris1_a3 = 123, 456, 789
iris2_a1, iris2_a2, iris2_a3 = 987, 654, 321
iris3_a1, iris3_a2, iris3_a3 = 111, 222, 333
iris4_a1, iris4_a2, iris4_a3 = 444, 555, 666

# Solicita ao usuário para inserir a leitura do padrão de íris
print("Insira o padrão de íris para autenticação.")
atributo1 = int(input("Atributo 1: "))
atributo2 = int(input("Atributo 2: "))
atributo3 = int(input("Atributo 3: "))

# Define a margem de erro permitida
tolerancia = 5

# Compara o padrão inserido com os padrões cadastrados
if abs(atributo1 - iris1_a1) <= tolerancia and abs(atributo2 - iris1_a2) <= tolerancia and abs(atributo3 - iris1_a3) <= tolerancia:
    print("Autenticação bem-sucedida!")
    print("Usuário: 1")
elif abs(atributo1 - iris2_a1) <= tolerancia and abs(atributo2 - iris2_a2) <= tolerancia and abs(atributo3 - iris2_a3) <= tolerancia:
    print("Autenticação bem-sucedida!")
    print("Usuário: 2")
elif abs(atributo1 - iris3_a1) <= tolerancia and abs(atributo2 - iris3_a2) <= tolerancia and abs(atributo3 - iris3_a3) <= tolerancia:
    print("Autenticação bem-sucedida!")
    print("Usuário: 3")
elif abs(atributo1 - iris4_a1) <= tolerancia and abs(atributo2 - iris4_a2) <= tolerancia and abs(atributo3 - iris4_a3) <= tolerancia:
    print("Autenticação bem-sucedida!")
    print("Usuário: 4")
else:
    print("Autenticação falhou!")
