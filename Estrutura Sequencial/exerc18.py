#Faça um programa que peça o tamanho de um arquivo para download
# (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb = int(input('Insira quantos MBs tem o seu arquivo de download: '))
mbps = int(input('Insira a velocidade do link da sua interent: '))
segundos = int((mb * 8) / mbps)
minutos = int(segundos / 60)
print(f'Vai levar aproximadamente {minutos} minutos e {segundos % 60} segundos para fazer o download')