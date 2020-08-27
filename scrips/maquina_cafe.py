class CoffeeMachine:

    def __init__(self, nick, senha):
        """ Dados relativos a Máquina e ao Score do Usuário """

        self.nick = nick
        self.senha = senha
        print(f'Seja Bem Vindo(a) {self.nick} a Máquina de Café')
        self.dict_values = {}
        self.iventario_maquina()
        self.dados = {'ml_bebido': 0, 'money_gasto': 0, 'copos_usados': 0, 'tipos': []}
        self.exe()

    def iventario_maquina(self):
        """ Volta para o estado anterior da máquina (arquivo recursos_maquina.etc)"""

        with open('../etc/recursos_maquina.etc', 'r+') as file:
            recursos = list(map(int, file.readlines()[0].split(',')))
        for index, value in enumerate(['água', 'leite', 'café', 'copos', 'money']):
            self.dict_values[value] = recursos[index]

    def remaining(self):
        """ Mostra os recursos da Máquina de Café """

        print('\nA Máquina de Café tem:')
        descricao = ['ml de água', 'ml de leite', 'g de café', 'copos disponíveis', 'R$ de dinheiro']
        recurses_numbers = list(self.dict_values.values())
        for i in range(5):
            print(f'{recurses_numbers[i]} {descricao[i]}')

    def buy_coffee(self, tipo):
        """ O usuário escolhe o tipo de café (int) e ele retorna a compra (se possível)"""

        custo = None
        if tipo == 1:
            custo = {'água': 250, 'leite': 0, 'café': 16, 'copos': 1, 'money': -4}
        elif tipo == 2:
            custo = {'água': 350, 'leite': 75, 'café': 20, 'copos': 1, 'money': -7}
        elif tipo == 3:
            custo = {'água': 200, 'leite': 100, 'café': 12, 'copos': 1, 'money': -6}

        lista_falta = [i for i in list(self.dict_values.keys()) if self.dict_values[i] + custo[i] < 0]

        if lista_falta:
            print('Desculpe, não tenho {}.'.format(', '.join(lista_falta)))
        else:
            self.dados['ml_bebido'] += abs(sum(list(custo.values())[:3]))
            self.dados['money_gasto'] += custo['money']
            self.dados['copos_usados'] += abs(custo['copos'])
            self.dados['tipos'].append(str(tipo))
            for key in self.dict_values:
                self.dict_values[key] -= custo[key]
            recursos_maquina = list(map(str, self.dict_values.values()))
            with open('../etc/recursos_maquina.etc', 'w+') as file:
                file.write(', '.join(recursos_maquina))
            print('Tenho recursos. Aproveite seu café :)')
        lista_falta.clear()

    def fill(self):
        """ Lê o arquivo etc/iventario.etc e acescenta a Máquina de café os ingredientes
        Se o usuário não tiver ingredientes sufientes, ele não faz nada"""

        with open('../etc/iventario.etc', 'r+') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                if self.nick in line:
                    pop_line = lines.pop(index)
        recursos = list(map(int, pop_line.split(', ')[1:]))

        def comparar(qtdds_user, fill_qtdds):
            resultados = []
            for i in range(4):
                resultados.append(bool(qtdds_user >= fill_qtdds))
            return True if sum(resultados) == 4 else False

        agua = int(input('\nQuantos ml de água você vai adicionar: \n'))
        leite = int(input('Quantos ml de leite você vai adicionar: \n'))
        cafe = int(input('Quantas gramas de café você vai adicionar: \n'))
        copos = int(input('Quantos copos você vai adicionar: \n'))

        user_qtdds = [agua, leite, cafe, copos]

        if not comparar(user_qtdds, recursos):
            print('Você não tem estes recursos no inventário, lamento :(')
        else:
            print('Máquina de café abastecida com sucesso :)')
            for index, value in enumerate(['água', 'leite', 'café', 'copos']):
                self.dict_values[value] += user_qtdds[index]
                recursos[index] = recursos[index] - user_qtdds[index]
            with open('../etc/iventario.etc', 'r+') as file:
                file.write(f"{self.nick}, {', '.join(recursos)}")

    def user_buy(self):
        user = input(
            '\nO que você quer comprar? \n1- Café espresso\n2- Café com leite, \n3- Cappuccino\n')
        try:
            self.buy_coffee(int(user))
        except ValueError:
            print('Digite um dos números indicados...')

    def salvar(self):
        with open('../etc/user_info.etc', 'r+') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                if self.nick in line:
                    pop_line = lines.pop(index)
            new_score = f'{pop_line.split(", ")[0]}, {int(self.dados["copos_usados"])}'
        with open('../etc/user_info.etc', 'r+') as file:
            file.write(new_score)

    def exe(self):
        user = input('\nEscolha uma ação: \n1- Comprar\n2- Reabastecer\n3- Recursos\n'
                     '4- Salvar e Sair\n5- Sair\n').strip().lower()
        while user != '5':
            if user == '1':
                self.user_buy()
            elif user == '2':
                self.fill()
            elif user == '3':
                self.remaining()
            elif user == '4':
                #  falta salvar os recursos da máquina, o inventário, e o score do usuário
                self.salvar()
            user = input('\nEscolha uma ação: \n1- Comprar\n2- Reabastecer\n3- Recursos'
                         '\n4- Salvar\n5- Sair\n').strip().lower()


playgame = CoffeeMachine('EVL')
