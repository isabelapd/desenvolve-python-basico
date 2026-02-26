# Leitura do número de valores a serem comparados
n = int(input("Digite a quantidade de número: "))

# Inicializa a váriavel para armazenar o maior número
maior = 0

# Loop para ler os valores enquanto n for maior que 0
while n > 0:
    x = int (input("Digite um número: ")) # Leitura de um número

    if x > maior: # verifica se o número é maior que o maior atual
        maior = x # Atualiza o maior número

    n -=1 # Decrementa o contador

# Exibe o maior número encontrado
print("O maior número é:", maior)     
