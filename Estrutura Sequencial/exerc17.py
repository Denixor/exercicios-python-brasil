#Faça um Programa para uma loja de tintas.
#v O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#v Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
#v que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#v comprar apenas latas de 18 litros;
#v comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metros_pintar = float(input('Insira a quantidade de metros quadrados que tem a parede que você vai pintar: '))
litros_tinta = metros_pintar/ 6
lata_tinta = (litros_tinta / 18) + ((litros_tinta / 18) * 10 / 100)
galoes = (litros_tinta / 3.6) + ((litros_tinta / 3.6) * 10 / 100)

print(f'Se vocÊ comprar apenas latas de 18 litros o preço final vai ser R${(int(lata_tinta) + 1) * 80}')
print(f'Se vocÊ comprar apenas galões de 3,6 litros o preço final vai ser R${int(galoes*25)}')
if lata_tinta % 18 != 0:
    if lata_tinta < 1:
        print(f'você pode comprar só uma lata para pintar toda a parede o preço final vai ser: R$ 80,00')
    else:
        print(
            f'Para evitar disperdicio você pode pegar {int(lata_tinta)} + 1 galão, o preço final vai ser R$: {int(lata_tinta * 80 + 1 * 25)}')
else:
    print(f'pegando {lata_tinta}, não haverá disperdicio, e o preço final vai ser R$: {int(int(lata_tinta) * 80)}')