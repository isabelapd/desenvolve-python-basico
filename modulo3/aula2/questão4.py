Classe=input("Escolha a classe (guerreiro, mago, ouarqueiro): ")
força=int(input("Digite os pontos de força (de 1 a 20):"))
magia=int(input("Digite os pontos de magia (de 1 a 20):"))

print ("Pontos de atributo consistentes com a classe escolhida:" ((Classe=="guerreiro" and força>= 15 and magia <=10) or (Classe=="mago" and força<=10 and magia>=15) or (Classe=="arqueiro" and (força>5 and força<15) and (magia>5 and magia<15) )))
