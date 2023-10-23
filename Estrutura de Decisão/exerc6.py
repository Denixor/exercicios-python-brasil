#Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Coloque um numero: '))
n2 = float(input('Coloque um outro numero: '))
n3 = float(input('Coloque um terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior numero')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior numero')
else:
    print(f'{n3} é o maior numero')