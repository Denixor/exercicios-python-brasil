import random
class Blackjack:
    def __init__(self):
        self.cartas_usuario = []
        x = random.randint(1, 12)
        y = random.randint(1, 12)
        self.cartas_usuario.append(x)
        self.cartas_usuario.append(y)
        self.valor_cartas_usuario = self.cartas_usuario[0] + self.cartas_usuario[1]
        self.condicao = True
        while self.condicao:
            self.atualizar()
            print(f'o total de sua mão é: {self.valor_cartas_usuario}')
            self.acao = int(input('1- Pedir cartas, 2- Manter, 3- Sair do Jogo: '))
            match self.acao:
                case 1:
                    self.pedir_cartas()
                    self.atualizar()
                case 2:
                    print('você manteve')
                case 3:
                    print('Fim de jogo')
                    self.condicao = False
                case _:
                    print('Comando Invalido')
    #Função Atualizar Valores
    def atualizar(self):
        if self.valor_cartas_usuario > 21:
            print(f'Você passou de 21, o total foi: {self.valor_cartas_usuario}')
            self.condicao = False
        elif self.valor_cartas_usuario == 21:
            print(f'BlackJack')
            self.condicao = False
    #Função Pedir Cartas
    def pedir_cartas(self):
        x = random.randint(1, 12)
        print(f'a carta que veio foi: {x}')
        self.cartas_usuario.append(x)
        self.valor_cartas_usuario += x
Blackjack()