#Faça um Programa que pergunte em que turno você estuda.
# #Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# #Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

periodo = input('Coloque o turno que você estuda (M-matutino ou V-Vespertino ou N- Noturno): ')
periodo = periodo.upper()
match periodo:
    case 'M':
        print('Bom Dia!')
    case 'V':
        print('Boa Tarde!')
    case 'N':
        print('Boa Noite')
    case _:
        print(f'{periodo} é INVALIDO, as respostas aceitaveis são: M-matutino ou V-Vespertino ou N- Noturno')