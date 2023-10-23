#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Coloque um numero: '))
n2 = float(input('Coloque um outro numero: '))
n3 = float(input('Coloque um terceiro numero: '))

lista = [n1, n2, n3]
maior = n1
menor = n1
for i in range(0, len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
print(f'o menor numero foi: {menor}, e o maior numero foi: {maior}')