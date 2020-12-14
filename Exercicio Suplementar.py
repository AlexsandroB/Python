"""Faça um programa em Python utilizando os conceitos de listas para armazenar
o nome e o preço de um grupo de produtos. Ao final o programa deve exibir o valor
médio dos produtos e os nomes dos produtos com preço superior a média."""

roupa_1 = (input('Digite o nome da primeira roupa: '))
valor_1 =  (float(input('Digite o valor da primeira roupa: ')))
roupa_2 = (input('Digite o nome da segunda roupa: '))
valor_2 =  (float(input('Digite o valor da segunda roupa: ')))
roupa_3 = (input('Digite o nome da terceira roupa: '))
valor_3 =  (float(input('Digite o valor da terceira roupa: ')))
roupa_4 = (input('Digite o nome da quarta roupa: '))
valor_4 =  (float(input('Digite o valor da quarta roupa: ')))

total = valor_1+valor_2+valor_3+valor_4
media = total/4
print('A média de preço das roupas foi de:', media)
