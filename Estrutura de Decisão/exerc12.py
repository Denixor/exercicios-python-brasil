#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Salario
horas = float(input('Coloque quantas horas você trabalhou este mês: '))
valor_horas = float(input('Coloque quanto você recebe por hora trabalhada: '))
salario_bruto = horas * valor_horas
sindicato = salario_bruto * 3 / 100
fgts = salario_bruto * 11 / 100
salario_liquido = salario_bruto

# Imposto de renda
if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500 and salario_bruto > 900:
    ir = salario_bruto * 5 /100
elif salario_bruto <= 2500 and salario_bruto > 1500:
    ir = salario_bruto * 10 /100
else:
    ir = salario_bruto * 20 /100

# Calculo IR
if ir == 0:
    salario_liquido = salario_bruto
    ir = 'Isento'
else:
    salario_liquido -= ir

# Saídas
print(f'O valor que a empresa vai pagar de sindicato é: {sindicato}, o valor que a empresa vai pagar de fgts é {fgts}')
print(f'O valor do salario bruto é: {salario_bruto}, o Imposto de renda é: {ir}, e o salario liquido é: {salario_liquido}')