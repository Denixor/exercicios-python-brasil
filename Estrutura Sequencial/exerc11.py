#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input('coloque um número inteiro: '))
n2 = int(input('coloque um outro número inteiro: '))
n3 = float(input('coloque um número real: '))

print(f'O dobro de {n1}, somado com metade de {n2} da {n1*2 + n2/2}')
print(f'a soma do triplo de {n1} com {n3} da: {n1*3 + n3}')
print(f'{n3} elevado ao cubo da {n3**3}')