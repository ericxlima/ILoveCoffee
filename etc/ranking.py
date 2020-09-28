import json


class Rank:

    def __init__(self):
        self.geral = None
        self.sorted_dict = None
        self.exe()

    def load_users(self):
        with open('etc/usuarios.json', 'r+') as file:
            geral = json.load(file)
        self.geral = geral

    def classificacao(self):
        sorted_dic = {}
        for lista in self.geral["usuarios"]:
            sorted_dic[lista['nome']] = lista['rank']
        sorted_dic = sorted(sorted_dic.items(), key=lambda item: item[1], reverse=True)
        self.geral = sorted_dic

    def print_ranking(self):
        for i in range(len(self.geral)):
            print(f'{i+1}ºLugar: {self.geral[i][0]} com {self.geral[i][1]} pontos')

    def exe(self):
        print('Bem vindo(a) ao Ranking do Rei do Café\n')
        self.load_users()
        self.classificacao()
        self.print_ranking()
        input('\nPressione qualquer tecla para continuar: ')
