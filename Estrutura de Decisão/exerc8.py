#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


n1 = float(input('Coloque o primeiro preço: '))
n2 = float(input('Coloque o segundo preço: '))
n3 = float(input('Coloque o terceiro preço: '))

if n1 < n2 and n1 < n3:
    print(f'você deve comprar o produto de valor R${n1}')
elif n2 < n1 and n2 < n3:
    print(f'você deve comprar o produto de valor R${n2}')
else:
    print(f'você deve comprar o produto de valor R${n3}')