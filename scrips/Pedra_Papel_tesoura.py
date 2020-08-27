from random import choice


class PedraPapelTesoura:

    def __init__(self, nick, senha):
        self.user = nick
        self.senha = senha
        self.pontos = 0
        self.jogar()

    def jogar(self):
        print('Instruções: Ao jogar escolha uma entre as opções [pedra, papel, tesoura]')
        print('Pressione a qualquer momento "sair" para sair ou "pontos" para exibir sua pontuação')
        lista = ["pedra", "papel", "tesoura"]
        perdedor = {"pedra": "papel", "tesoura": "pedra", "papel": "tesoura"}
        user_choice = input().lower().strip()
        pc = choice(lista)
        while user_choice != 'sair':
            if user_choice == 'pontos':
                print(f'Sua pontuação atual é {self.pontos}')
            elif user_choice not in lista:
                print('Entrada Inválida')
            else:
                if perdedor[user_choice] == pc:
                    print(f'Que pena, a máquina escolheu {pc} e você perdeu 50 pontos :(')
                    self.pontos -= 50
                elif user_choice == pc:
                    print(f'A máquina escolheu {pc} e deu empate :| (niguém ganhou nada)')
                else:
                    print('Parabéns! A máquina escolheu {pc} e você ganou 100 pontos :)')
                    self.pontos += 100
                user_choice = input().lower().strip()

    def salvar(self):
        """
        Devo aprender a manipular arquvos json pra salvar os dados :(
        """
        return
