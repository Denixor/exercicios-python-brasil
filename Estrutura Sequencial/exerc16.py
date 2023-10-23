#Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros  quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros_pintar = float(input('Insira a quantidade de metros quadrados que tem a parede que você vai pintar: '))
litros_tinta = metros_pintar/3
lata_tinta = litros_tinta / 18

if lata_tinta % 18 != 0:
    lata_tinta = int(lata_tinta) + 1
print(f'Para pintar essa parede você deve comprar {lata_tinta} latas de tinta, e o preço total vai ser {lata_tinta * 80}')