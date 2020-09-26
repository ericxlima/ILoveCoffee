import json
from time import sleep


class JogoDaVelha:

    def __init__(self, nick):
        self.nick = nick
        self.other_nick = None
        self.tentativas = 0

        self.matriz = [[' ' for _ in range(3)] for _ in range(3)]
        self.other_player()
        if self.other_nick:
            self.jogar()
            sleep(3.5)

    def print_matriz(self):
        print('  1  2  3 ')
        print(' ---------')
        print('1| {} |'.format(' '.join(self.matriz[0])))
        print('2| {} |'.format(' '.join(self.matriz[1])))
        print('3| {} |'.format(' '.join(self.matriz[2])))
        print(' ---------')

    def other_player(self):
        try:
            other_nick = input('Insira o nick do segundo jogador: ')
            other_senha = input('Insira a senha do segundo jogador: ')

            def other_player_exist(nick, senha):
                with open('etc/usuarios.json', 'r') as file:
                    geral = json.load(file)
                    for idx, pessoa in enumerate(geral['usuarios']):
                        if pessoa['nome'] == nick and pessoa['senha'] == senha:
                            return True
                return False

            while not other_player_exist(other_nick, other_senha):
                print('\nO usuário inserido não existe (Senha ou Nick inválido)\n')
                continuar = input('Insira "sair" para sair ou "continuar" para inserir outro usuário? ')
                if continuar == 'sair':
                    raise TypeError('')
                else:
                    other_nick = input('Insira o nick do segundo jogador: ')
                    other_senha = input('Insira a senha do segundo jogador: ')
            self.other_nick = other_nick
        except TypeError:
            self.other_nick = None

    def ganhador(self):
        """ Checa a matriz para ver se alguém conseguiu vencer"""

        def salvar(nome):
            with open('etc/usuarios.json', 'r') as file:
                geral = json.load(file)
                for idx, pessoa in enumerate(geral['usuarios']):
                    if pessoa['nome'] == nome:
                        line, user = (idx, geral['usuarios'][idx])
                        user['pontos'] += 250
                        geral['usuarios'][idx] = user
            with open('etc/usuarios.json', 'w') as file2:
                geral = json.dumps(geral, indent=4)
                file2.write(geral)

        m = self.matriz.copy()
        p1 = m[0][0] if m[0][0] == m[0][1] == m[0][2] else False
        p2 = m[0][0] if m[0][0] == m[1][0] == m[2][0] else False
        p3 = m[2][2] if m[2][0] == m[2][1] == m[2][2] else False
        p4 = m[0][2] if m[0][2] == m[1][2] == m[2][2] else False
        p5 = m[1][0] if m[1][0] == m[1][1] == m[1][2] else False
        p6 = m[1][1] if m[0][1] == m[1][1] == m[2][1] else False
        p7 = m[0][0] if m[0][0] == m[1][1] == m[2][2] else False
        p8 = m[0][2] if m[0][2] == m[1][1] == m[2][0] else False
        ganhou = [x for x in [p1, p2, p3, p4, p5, p6, p7, p8] if x == 'X' or x == 'O']
        if ganhou:
            if ganhou == 'X':
                salvar(self.other_nick)
                return f"X - {self.other_nick} Ganhou! 750 pontos"
            else:
                salvar(self.nick)
                return f"O - {self.nick} Ganhou! 750 pontos"
        else:
            return False

    def coordenadas(self):
        def x_or_o():
            self.tentativas += 1
            return 'O' if not self.tentativas % 2 else 'X'

        def analise(coordenada, linha=None, coluna=None):
            try:
                linha, coluna = list(map(int, list(coordenada)))
            except ValueError:
                print('Você deve inserir apenas números')
            if linha not in [1, 2, 3] or coluna not in [1, 2, 3]:
                print('As coordenadas devem estar entre [1, 2, 3]')
                return False
            elif self.matriz[linha - 1][coluna - 1] != ' ':
                print('Esta celula já está ocupada')
                return False
            else:
                self.matriz[linha - 1][coluna - 1] = x_or_o()
                return True

        user_coordenada = input('Insira as coordenadas [linha coluna]: ').replace(' ', '')
        while not analise(user_coordenada):
            user_coordenada = input('Insira as coordenadas [linha coluna]: ').replace(' ', '')

    def jogar(self):
        print(f'O jogador {self.other_nick} começa com X\n'
              f'O jogador {self.nick} é o O')
        while not self.ganhador() or self.tentativas >= 9:
            self.print_matriz()
            self.coordenadas()
            self.ganhador()
            if self.tentativas >= 9:
                print("Deu velha")
                return False
        else:
            print(self.ganhador())
