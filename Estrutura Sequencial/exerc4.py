#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input('Qual a nota do primeiro bimestre? '))
n2 = float(input('Qual a nota do segundo bimestre? '))
n3 = float(input('Qual a nota do terceiro bimestre? '))
n4 = float(input('Qual a nota do quarto bimestre? '))
media = (n1+n2+n3+n4) / 4
print(f'a media final foi: {media}')