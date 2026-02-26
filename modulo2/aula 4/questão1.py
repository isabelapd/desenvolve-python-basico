# Dados
compr = int(input("Digite o comprimento:"))
largura =int(input("Digite a largura:"))
preço_m2 = float(input("Valor do m2: "))

area_m2 = compr * largura #m2
preco_total = area_m2 * preço_m2

print(f' O terreno possuiI {area_m2}m2 e custa R$ {preco_total:,.2f}')
