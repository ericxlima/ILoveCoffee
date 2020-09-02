import json


class Banco:

    def __init__(self, nick):
        self.nick = nick
        self.geral, self.user, self.values = None, None, None
        self.load_values()
        self.exe()

    def load_values(self):
        with open('etc/usuarios.json', 'r') as file:
            self.geral = json.load(file)
            for idx, pessoa in enumerate(self.geral['usuarios']):
                if pessoa['nome'] == self.nick:
                    self.user, self.values = ((idx, pessoa), (pessoa['pontos'], pessoa['recursos']['dinheiro']))

    def comprar_money(self):
        pontos, dinheiro = self.values
        print(f'Você tem {pontos} pontos e pode comprar até {int(pontos / 5)} de dinheiro')
        buy = int(input('Quanto de dinheiro você quer comprar?'))
        if buy <= pontos / 5:
            pontos -= buy * 5
            dinheiro += buy
            self.user[1]['pontos'], self.user[1]['recursos']['dinheiro'] = (pontos, dinheiro)
        with open('etc/usuarios.json', 'w') as file:
            self.geral['usuarios'][self.user[0]] = self.user[1]
            geral = json.dumps(self.geral, indent=4)
            file.write(geral)

    def exe(self):
        print('Bem vindo(a) ao Banco, aqui você pode trocar pontos por dinheiro, fazer um cartão de crédito, efetuar '
              'depósitos, entre outras coisas futuras')
        fzr = input('O que querer fazer?\n1- Comprar dinheiro\nsair - Sair do Banco')
        while fzr != 'sair':
            if fzr == '1':
                self.comprar_money()
            fzr = input('O que querer fazer?\n1- Comprar dinheiro\nsair - Sair do Banco')
