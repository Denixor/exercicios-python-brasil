#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#	(0 °C × 9/5) + 32

C = float(input('qual temperatura em graus Celsius você deseja converter? '))
F = (C * 9/5) + 32

print(f'{C} graus celsius em Fahrenheit da {F}')