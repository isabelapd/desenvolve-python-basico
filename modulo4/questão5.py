n = int(input("Digite a quantidade de respondente: "))

# inicializar as variaveis
soma = 0 # resultado -> soma + idade
cont = 0 # variavel de controle do laço

while cont < n:
    idade = int(input("Digite a idade do respondente"))
    soma += idade #soma = soma + idade

    # atualizando a variavel de controle do laço cont += 1 # cont = cont + 1
    cont += 1 # cont = cont + 1

# imprimir a média
print (f"A média das idades é {soma/n:.0f} anos")    
