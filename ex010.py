#Exercício 10 - Conversor de Moedas

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.73
euro = real / 6.83
print('Com R${:.2f}, em dolar você pode comprar US${:.2f} e em euro você pode comprar {:.2f}'.format(real, dolar, euro))
