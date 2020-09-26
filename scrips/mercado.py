import json


class Mercado:
    def __init__(self, nick):
        self.nick = nick
        self.geral, self.line, self.user_values = None, None, None
        self.user = None
        self.load_info()
        self.exe()

    def load_info(self):
        with open('etc/usuarios.json', 'r') as file:
            self.geral = json.load(file)
            for idx, pessoa in enumerate(self.geral['usuarios']):
                if pessoa['nome'] == self.nick:
                    self.line, self.user_values = (idx, self.geral['usuarios'][idx]['recursos'])
                    self.user = self.geral['usuarios'][idx]

    def comprar(self):
        def check(lst):
            prices = (15, 25, 50, 100)
            try:
                compras = [prices[i] * lst[i] for i in range(4)]
                if sum(compras) <= self.user_values['dinheiro']:
                    self.user_values['dinheiro'] -= sum(compras)
                    print('Compra realizada com sucesso\n')
                    return True
            except IndexError:
                print('Não foi possível realizar as compras :(\n')

        precos = '''\nPreços tabelados:
            1 ml Água  -> 15  pontos
            1 ml Leite -> 25  pontos
            1 g Café   -> 50  pontos
            1 copo     -> 100 pontos'''
        print(precos)
        new_values = []
        for item in ['agua', 'leite', 'cafe', 'copos']:  # erro
            try:
                new_values.append(int(input(f"Quantos unidades de {item} queres comprar? ")))
            except ValueError:
                print('Entrada Inválida')
        if check(new_values):
            for idx, key in enumerate(['agua', 'leite', 'cafe', 'copos']):
                self.user_values[key] += new_values[idx]

    def salvar(self):
        geral = self.geral
        with open('etc/usuarios.json', 'w') as file:
            self.user['recursos'] = self.user_values
            geral['usuarios'][self.line] = self.user
            geral = json.dumps(self.geral, indent=4)
            file.write(geral)

    def exe(self):
        print('\nBem vindo ao Mercado, aqui você pode trocar pontos por dinheiro e/ou ingredientes')
        fzr = None
        while fzr != 'sair':
            self.comprar()
            fzr = input('O que deseja fazer? [comprar/sair]\n>>> ')
        self.salvar()
