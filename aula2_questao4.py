#Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. Cada personagem tem uma classe específica com requisitos de atributos. 
#Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. 
#O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:
#Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
#Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
#Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.

#entrada

classe_personagem = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pontos_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pontos_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

#processamento

if classe_personagem == "guerreiro":
    if pontos_forca >= 15 and pontos_magia <= 10:
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else:
        print("Pontos de atributo consistentes com a classe escolhida: False")
elif classe_personagem == "mago":
    if pontos_forca <= 10 and pontos_magia >= 15:
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else:
        print("Pontos de atributo consistentes com a classe escolhida: False")
elif classe_personagem == "arqueiro":
    if 5 < pontos_forca < 15 and 5 < pontos_magia < 15:

#saida 
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else:
        print("Pontos de atributo consistentes com a classe escolhida: False")
else:
    print("Classe de personagem inválida.")
