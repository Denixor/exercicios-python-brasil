import random

class Aplicativo():
    def __init__(self):
        self.fichas_usuario:int = 10 # Valor inicial que o usuario vai começar a partida
        print('Bem vindo a mesa de blackjack')
        while True: #Loop do Jogo
            if self.fichas_usuario == 0:
                print('Você ficou sem fichas')
                break
            jogada = int(input(f'Você tem: {self.fichas_usuario} fichas. \n Oque gostaria de fazer?'
                           f'\n 1- Jogar uma partida \n 2- Sair \n -'))
            match jogada:
                case 1:
                    print(f'Vamos jogar \n Qual a sua aposta inicial? (você tem {self.fichas_usuario} fichas)')
                    aposta_player = int(input('1- Uma Ficha \n 2- Duas Fichas \n 3- Quatro Fichas \n 4- Dez Fichas \n -'))
                    match aposta_player:
                        case 1:
                            aposta_player = 1
                            aposta_total = aposta_player * 2
                            self.fichas_usuario -= aposta_player
                            print(f'Você apostou {aposta_player}, então o pote vai ser {aposta_total}')
                            self.Blackjack(aposta_total)
                        case 2:
                            if self.fichas_usuario >= 2:
                                aposta_player = 2
                                aposta_total = aposta_player * 2
                                self.fichas_usuario -= aposta_player
                                print(f'Você apostou {aposta_player}, então o pote vai ser {aposta_total}')
                                self.Blackjack(aposta_total)
                            else:
                                print('Você não tem esse valor de aposta')
                        case 3:
                            if self.fichas_usuario >= 4:
                                aposta_player = 4
                                aposta_total = aposta_player * 2
                                self.fichas_usuario -= aposta_player
                                print(f'Você apostou {aposta_player}, então o pote vai ser {aposta_total}')
                                self.Blackjack(aposta_total)
                            else:
                                print('Você não tem esse valor de aposta')
                        case 4:
                            if self.fichas_usuario >= 10:
                                aposta_player = 10
                                aposta_total = aposta_player * 2
                                self.fichas_usuario -= aposta_player
                                print(f'Você apostou {aposta_player}, então o pote vai ser {aposta_total}')
                                self.Blackjack(aposta_total)
                            else:
                                print('Você não tem esse valor de aposta')
                case 2:
                    print(f'Obrigado por jogar, você terminou com {self.fichas_usuario} fichas')
                    break
                case _:
                    print('Opção Invalida')
    def Blackjack(self, aposta_total):
        aposta = aposta_total #Valor do pote
        carta1_mesa = random.randint(1, 12)
        carta2_mesa = random.randint(1, 12)
        total_mesa = carta1_mesa + carta2_mesa
        carta1_usuario = random.randint(1, 12)
        carta2_usuario = random.randint(1, 12)
        total_usuario = carta1_usuario + carta2_usuario
        print(f'Sua primeira carta é: {carta1_usuario} \n Sua segunda carta é: {carta2_usuario} \n O seu total é: {total_usuario}')
        print(f'Minha primeira carta é {carta1_mesa} \n Minha segunda carta é: {carta2_mesa} \n O meu total é: {total_mesa}')
        while True: #JOGO
            if self.checagem_cartas(total_usuario) == True:
                print('BLACKJACK, você ganhou.')
                self.fichas_usuario += aposta
                break #ACABAR JOGO
            elif self.checagem_cartas(total_usuario) == False:
                print('Você passou de 21, infelizmente você perdeu')
                break #ACABAR JOGO
            else:
                acao = int(input(f'Qual vai ser sua ação (você tem: {total_usuario} total):'
                                 f'\n 1 - Pedir mais uma carta \n 2 - Segurar mão ' '\n 3- Aumentar Aposta'
                                 '\n 4- Desistir \n -'))
                match acao:
                    case 1: #Pedir uma carta Nova
                        nova_carta = random.randint(1, 12)
                        print(f'sua nova carta é: {nova_carta}')
                        total_usuario += nova_carta
                    case 2: # Segurar a Mão
                        while True: #TURNO MESA
                            if total_mesa < 17:
                                nova_carta_mesa = random.randint(1, 12)
                                print(f'Eu comprei essa carta: {nova_carta_mesa}')
                                total_mesa += nova_carta_mesa
                            elif total_mesa > 21:
                                print(f'Eu passei de 21, eu perdi, você ganhou {aposta}')
                                self.fichas_usuario += aposta
                                break # ACABAR TURNO MESA
                            elif total_mesa == 21:
                                print(f'BLACKJACK, eu ganhei')
                                break #ACABAR TURNO MESA
                            else:
                                if total_mesa > total_usuario:
                                    print(f'meu total ({total_mesa}) foi maior que o seu ({total_usuario}), você perdeu!')
                                    break
                                elif total_mesa == total_usuario:
                                    print(f'meu total ({total_mesa} foi igual ao seu, empate o jogador vence, então você venceu!)')
                                    self.fichas_usuario += aposta
                                    break
                                else:
                                    print(f'seu total ({total_usuario}) foi maior que o meu ({total_mesa}), você ganhou!')
                                    self.fichas_usuario += aposta
                                    break
                        break   #ACABAR JOGO
                    case 3:  #Aumentar a Aposta
                        print(f'O pote autal é de: {aposta}, você deseja apostar quanto a mais?')
                        x = int(input('-'))
                        if x > self.fichas_usuario:
                            print('Você não tem esse dinheiro!')
                        else:
                            self.fichas_usuario -= x
                            aposta += x*2
                            print(f'o pote atual é de: {aposta}')
                    case 4: # Desistir
                        print(f'Você perdeu.')
                        break
                    case _:
                        print('Opção invalida')

        print('Fim de jogo')
    def checagem_cartas(self, total):
        if total == 21:
            return True
        elif total > 21:
            return False

Aplicativo()