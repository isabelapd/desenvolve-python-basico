idade = int(input ("Digite sua idade: "))
ndejogos=(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
vitorias= int(input("Quantos jogos já venceu? "))
print("Apto para ingressar nos jogos de clube de tabuleiro: ", (idade>=16 and idade<=18) or (ndejogos==True) or (vitorias>=1))
