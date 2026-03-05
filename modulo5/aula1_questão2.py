import random
import math

n = int(input("Digite a quantidade de números aleatórios entre 0 e 100: "))
soma = 0 
for i in range(n):
    numeros = random.randint(0, 100)
    print(numeros)
    soma += numeros

print (soma)

raiz_quadrada = math.sqrt(soma)

print(f"Raiz quadrada da soma: {round(raiz_quadrada, 2)}")
