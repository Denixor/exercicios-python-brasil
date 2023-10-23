#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato (5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

ganha_hora = float(input('Insira o quanto você ganha por hora: '))
horas_mes = float(input('Insira quantas horas você trabalhou no mês: '))
salario_bruto = float(ganha_hora * horas_mes)
IR = (salario_bruto * 11) / 100
INSS = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - IR - INSS - sindicato

print(f'você ganhando {ganha_hora} por hora, e trabalhando {horas_mes}, tem um salario bruto de {salario_bruto}')
print(f'os descontos que você tem no salario são: imposto de renda {IR}, INSS {INSS}, sindicato {sindicato}')
print(f'o salario final (liquido) ficou em: {salario_liquido}')