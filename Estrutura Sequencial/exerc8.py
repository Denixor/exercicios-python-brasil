#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

ganho_hora = int(input('quanto você ganha por hora: '))
horas_trabalhas = int(input('quantas horas você trabalhou esse mês? '))
print(f'em {horas_trabalhas} você ganhou {ganho_hora*horas_trabalhas}')