import json


class MaquinaDeCafe:

    def __init__(self, nick):
        """ Dados relativos a Máquina e ao Score do Usuário """

        self.nick = nick
        print(f'Seja Bem Vindo(a) {self.nick} a Máquina de Café')
        self.geral, self.line, self.user, self.user_rank = None, None, None, 0
        self.user_values = None
        self.load_info()
        self.exe()

    def load_info(self):
        with open('etc/usuarios.json', 'r') as file:
            self.geral = json.load(file)
            for idx, pessoa in enumerate(self.geral['usuarios']):
                if pessoa['nome'] == self.nick:
                    self.line = idx
                    self.user_values = self.geral['usuarios'][idx]['recursos']
                    self.user_rank = self.geral['usuarios'][idx]['rank']
                    self.user = self.geral['usuarios'][idx]

    def remaining(self):
        """ Mostra os recursos da Máquina de Café """

        print('\nA Máquina de Café tem:')
        descricao = ['ml de água', 'ml de leite', 'g de café', 'copos disponíveis', 'R$ de dinheiro']
        recurses_numbers = list(self.user_values.values())
        for i in range(5):
            print(f'{recurses_numbers[i]} {descricao[i]}')

    def buy_coffee(self, tipo):
        """ O usuário escolhe o tipo de café (int) e ele retorna a compra (se possível)"""

        custo = None
        if tipo == 1:
            custo = {'agua': 250, 'leite': 0, 'cafe': 16, 'copos': 1, 'dinheiro': 4}
        elif tipo == 2:
            custo = {'agua': 350, 'leite': 75, 'cafe': 20, 'copos': 1, 'dinheiro': 7}
        elif tipo == 3:
            custo = {'agua': 200, 'leite': 100, 'cafe': 12, 'copos': 1, 'dinheiro': 6}

        lista_falta = [i for i in list(self.user_values.keys()) if self.user_values[i] - custo[i] < 0]

        if lista_falta:
            print('Desculpe, não tenho {}.'.format(', '.join(lista_falta)))
        else:
            self.user_rank += tipo
            for key in self.user_values:
                self.user_values[key] -= custo[key]
            print('Tenho recursos. Aproveite seu café :)')
        lista_falta.clear()

    def user_buy(self):
        user = input(
            '\nO que você quer comprar? \n1- Café espresso\n2- Café com leite\n3- Cappuccino\n')
        while user not in '123':
            print('O café tem de ser um dos 3:\n1- Café espresso\n2- Café com leite\n3- Cappuccino\n')
            user = input('\nO que você quer comprar? \n1- Café espresso\n2- Café com leite\n3- Cappuccino\n')
        try:
            self.buy_coffee(int(user))
        except ValueError:
            print('Digite um dos números indicados (1, 2, 3)...')

    def salvar(self):
        geral = self.geral
        with open('etc/usuarios.json', 'w') as file:
            self.user['recursos'] = self.user_values
            self.user['rank'] = self.user_rank
            geral['usuarios'][self.line] = self.user
            geral = json.dumps(self.geral, indent=4)
            file.write(geral)

    def exe(self):
        user = None
        while user != 'sair':
            if user == '1':
                self.user_buy()
            elif user == '2':
                self.remaining()
            self.salvar()
            user = input('\nEscolha uma ação: \n1- Comprar\n2- Recursos\nSair - Para sair da Máquina\n>>> ').strip().lower()
