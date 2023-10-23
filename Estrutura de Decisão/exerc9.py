#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input('Coloque um número: '))
n2 = float(input('Coloque um outro número: '))
n3 = float(input('Coloque um terceiro número: '))
lista = [n1, n2, n3]
lista.sort(reverse=True)

for i in range(0, len(lista)):
    print(lista[i])