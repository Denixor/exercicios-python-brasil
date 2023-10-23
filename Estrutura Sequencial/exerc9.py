#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

F = float(input('Qual temperatura em Fahrenheit você quer converter: '))
C = 5 * ((F-32) / 9)
print(f'{F}Fahrenheit em graus Celsius da {C}')