class Mercado:
    def __init__(self, nick, senha):
        self.nick = nick
        self.senha = senha
        self.dict_values = {'agua': 0, 'leite': 0, 'cafe': 0, 'copos': 0, 'dinheiro': 0, 'pontos': 0}
        self.load_info()
        self.exe()

    def load_info(self):
        """
        aprender a manipular arquivos json para logar as informações do usuário
        """
        pass

    def comprar(self):
        def check(lst):
            prices = (10, 15, 25, 50, 100)
            compras = [prices[i] * lst[i] for i in range(5)]
            if sum(compras) <= self.dict_values['pontos']:
                self.dict_values['pontos'] -= sum(compras)
                return True

        precos = '''Preços tabelados:
            1 Dinheiro -> 10  pontos
            1 ml Água  -> 15  pontos
            1 ml Leite -> 25  pontos
            1 g Café   -> 50  pontos
            1 copo     -> 100 pontos'''
        print(precos)
        new_values = []
        for item in self.dict_values.keys()[:-1]:
            new_values.append(int(input(f"Quantos unidades de {item} queres comprar? ")))
        resultado = check(new_values)
        if resultado:
            for idx, key in enumerate(self.dict_values.keys()[:-1]):
                self.dict_values[key] += new_values[idx]

    def exe(self):
        print('Bem vindo ao Mercado, aqui você pode trocar pontos por dinheiro e/ou ingredientes')
        fzr = input('O que deseja fazer? [comprar/sair]')
        while fzr != 'sair':
            self.comprar()
            fzr = input('O que deseja fazer? [comprar/sair]')
