#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

vogais = ['A', 'E', 'I', 'O', 'U']
letra = input('Coloque uma letra: ')
if letra.upper() in vogais:
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante')