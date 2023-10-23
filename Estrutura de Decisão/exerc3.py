#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
x = input('Coloque o sexo (F ou M): ')
if x == 'M':
    print('Masculino')
elif x == 'F':
    print('Feminino')
else:
    print(f'{x} é um Sexo Invalido')