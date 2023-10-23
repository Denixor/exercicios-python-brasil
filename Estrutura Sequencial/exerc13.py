#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input('Coloque a sua altura: '))
print(f'com a altura de: {altura}, o peso ideal para homens é {72.7*altura - 58}, e para mulheres é {62.1*altura - 44.7}')