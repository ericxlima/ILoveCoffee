from time import sleep
import json


class Banco:

    def __init__(self, nick):
        self.nick = nick
        self.geral, self.user, self.values = None, None, None
        self.load_values()
        self.exe()
        sleep(2)

    def load_values(self):
        with open('etc/usuarios.json', 'r') as file:
            self.geral = json.load(file)
            for idx, pessoa in enumerate(self.geral['usuarios']):
                if pessoa['nome'] == self.nick:
                    self.user, self.values = ((idx, pessoa), (pessoa['pontos'], pessoa['recursos']['dinheiro']))

    def comprar_money(self):
        pontos, dinheiro = self.values
        print(f'\nVocê tem {pontos} pontos e pode comprar até {int(pontos / 5)} de dinheiro')
        buy = input('Quanto de dinheiro você quer comprar? ')
        try:
            buy = int(buy)
            if buy <= pontos / 5:
                pontos -= buy * 5
                dinheiro += buy
                self.user[1]['pontos'], self.user[1]['recursos']['dinheiro'] = (pontos, dinheiro)
                with open('etc/usuarios.json', 'w') as file:
                    self.geral['usuarios'][self.user[0]] = self.user[1]
                    geral = json.dumps(self.geral, indent=4)
                    file.write(geral)
                print('Compra realizada com sucesso')
            else:
                print(f'Você só pode comprar até {pontos / 5} de dinheiro')
        except ValueError:
            print('O valor tem de ser numeral')

    def exe(self):
        print('Bem vindo(a) ao Banco, aqui você pode trocar pontos por dinheiro, fazer um cartão de crédito, \nefetuar '
              'depósitos, entre outras coisas futuras')
        fzr = input('O que querer fazer?\n  1- Comprar dinheiro\n   sair - Sair do Banco\n')
        if fzr == '1':
            self.comprar_money()
