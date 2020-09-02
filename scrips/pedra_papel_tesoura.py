from random import choice
import json


class PedraPapelTesoura:

    def __init__(self, nick):
        self.user = nick
        self.pontos = 0
        self.jogar()
        self.salvar()

    def jogar(self):
        print('\n Bem vindo ao Jogo Pedra Papel e Tesoura\n')
        print('Instruções: Ao jogar escolha uma entre as opções [pedra, papel, tesoura]')
        print('Pressione a qualquer momento "sair" para sair ou "pontos" para exibir sua pontuação')
        lista = ["pedra", "papel", "tesoura"]
        perdedor = {"pedra": "papel", "tesoura": "pedra", "papel": "tesoura"}
        user_choice = input('Você escolhe: ').lower().strip()
        while user_choice != 'sair':
            pc = choice(lista)
            if user_choice == 'pontos':
                print(f'Sua pontuação atual é {self.pontos}\n')
            elif user_choice not in lista:
                print('Entrada Inválida\n')
            else:
                if perdedor[user_choice] == pc:
                    print(f'Que pena, a máquina escolheu "{pc}" e você perdeu 50 pontos :(\n')
                    self.pontos -= 50
                elif user_choice == pc:
                    print(f'A máquina escolheu "{pc}" e deu empate :| (niguém ganhou nada)\n')
                else:
                    print(f'Parabéns! A máquina escolheu "{pc}" e você ganhou 100 pontos :)\n')
                    self.pontos += 100
            user_choice = input('Você escolhe: ').lower().strip()

    def salvar(self):
        with open('etc/usuarios.json', 'r') as file:
            geral = json.load(file)
            for idx, pessoa in enumerate(geral['usuarios']):
                if pessoa['nome'] == self.user:
                    line, user = (idx, geral['usuarios'][idx])
                    user['pontos'] += self.pontos
                    geral['usuarios'][idx] = user
        with open('etc/usuarios.json', 'w') as file2:
            geral = json.dumps(geral, indent=4)
            file2.write(geral)
