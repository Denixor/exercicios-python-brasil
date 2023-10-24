#Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado_1 = float(input('Coloque o primeiro lado: '))
lado_2 = float(input('Coloque o segundo lado: '))
lado_3 = float(input('Coloque o terceiro lado: '))

lista = [lado_1, lado_2, lado_3]
diferentes = 0
for i in range(0, len(lista)):
    for y in range(i, len(lista)):
        if lista[i] != lista[y]:
            diferentes += 1
            
match diferentes:
    case 0:
        print('Triângulo Equilátero')
    case 2:
        print('Triângulo Isósceles')
    case 3:
        print('Triângulo Escaleno')
    case _:
        print('Erro desconhecido')
        