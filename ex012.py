#Exercício 12 - Calculando Descontos

preço = float(input('Qual é preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(preço, novo))

