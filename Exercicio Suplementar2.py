"""Faça um programa que converta um valor em Real (R$) em Dolár e Euro"""


valor_reais = float(input('Digite o valor em Reais: '))
valor_dolar = valor_reais/5.09
valor_euro = valor_reais/6.18
print('O valor em dólar é de: {:.2f}'.format(valor_dolar))
print('O valor em euro é de: {:.2f}'.format(valor_euro))