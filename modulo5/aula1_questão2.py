import random
import math

n = int(input("Digite a quantidade de números aleatórios entre 0 e 100: "))
numeros = [random.randint(0, 100) for _ in range(n)]
raiz_quadrada = math.sqrt(sum(numeros))

print(f"Raiz quadrada da soma: {round(raiz_quadrada, 2)}")
