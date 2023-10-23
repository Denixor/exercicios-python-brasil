#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Coloque a primeira nota: '))
n2 = float(input('Coloque a segunda nota: '))
media = (n1+n2)/2
if media >= 7 and media != 10:
    print(f'Aprovado, a media foi: {media}')
elif media == 10:
    print(f'Aprovado com Distinção, a media foi: {media}')
elif media < 7:
    print(f'Reprovado, a media foi: {media}')
else:
    print(f'Valores Incorretos, {media}')