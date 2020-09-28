from os import name
from time import sleep


class Descricoes:

    historia_geral_desc = '''   Seja Bem-Vindo(a) ao seu primeiro emprego. Nesta cafeteria como você pode ver, temos de tudo um 
pouco. Aqui você pode jogar diversos minigames para ganhar pontos, que poderá ser usado para trocar por dinheiro. O seu objetivo é 
conseguir o máximo de cafeína tomado para se manter no Pódio do Ranking Rei do Café. Quantas xícaras de café será capaz de tomar?...'''

    jogo_da_forca_desc = '''    No Jogo da Forca, o usuário tem 8 vidas e o objetivo do jogo é acertar o máximo de letras da 
palavra desconhecida. Existem 3 categorias do jogo, e um total de 40 palavras. Ao completar uma palavra você ganha um 
total de 100 pontos para cada vida restante.'''

    mercado_desc = '''  O Mercado é o lugar onde você pode trocas pontos por ingredientes (água, leite e café) além de copos.
Caso você não tenha pontos sufientes, a compra não será efetuada. Caso você esteja precisando urgentemente
realizar a compra, não hesite em tentar um empréstimo no banco :)'''

    maquina_cafe_desc = ''' A Máquina de Café é sem dúvidas a melhor parte desta de trabalhar no ILoveCoffe, é o objetivo 
principal do mesmo. Na Máquina de Café você pode utilizar seus ingredientes e dinheiro para fazer cafés deliciosos. 
Temos 3 opções de Café distintas, ambos variam em quantidades de produtos, e no rank que cada uma dá quanto mais café você toma,
mais próximo do Pódio Ranking Do Rei do Café" você estará.'''

    pedra_papel_tesoura_desc = '''  O Jogo "Pedra Papel Tesousa" é exatamente como o clássico, cada vez que você ganhar um
jogo contra a máquina, ganha 100 pontos. Quando perder, perde 50 pontos e em casos de empate, não ganha nada. O jogo 
utiliza um sistema de pseudo-aleatoriedade, portanto, não é possível prever as jogadas da máquina. 
Divirta-se nas suas vitórias e derrotas :)'''

    banco_desc = '''    No Banco, você pode ver quantos pontos você tem e assim, poder comprar dinheiro. Na próxima fase do
projeto, será possível fazer pequenos empréstimos com base no "Ranking do Rei do Café; fazer cartões de crédito; realizar 
depósitos em contas de amigos entre outras funcionalidades'''

    jogo_da_velha_desc = '''    O jogo da Velha é o primeiro projeto MultiPlayer do ILoveCoffe, nele logamos dois players 
simultaneamente, e suas respectivas pontuações (Obrigatório ter 2 players). O jogo consiste no PvP (Player vs
Player) até que um saia vencedor ou dê velha. Quem vencer ganha 750 pontos'''

    ranking_desc = '''O Ranking Rei do Café mostra o placar geral, ordenando em ordem Decrescente todos os trabalhadores do
ILoveCoffee, quanto mais cafés forem tomados, e quanto mais caros os cafés, mais próximo do Pódio deste Ranking você estará.'''

    logo = '''
XXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXX  XXXXXX  XXXXX  XXXXX  XXXXX  XXXXX
XXXXXXXXX    XX       XXXX     XXXXXX      XX         X       X    X  X      X      X      X
   XXX       XX    XXXX  XX   XX    XXX    XXXXXX     X       X    X  X      X      X      X
   XXX       XX   XX      XXXX        XX   XX   XX    X       X    X  XXXXX  XXXXX  XXXXX  XXXXX
   XXX       XX   XX        X         XX   XX    X    X       X    X  X      X      X      X
   XXX       XX    XX                XX    XX    X    X       X    X  X      X      X      X
   XXX        XX    XXX             XX    XX     X    X       X    X  X      X      X      X
   XXX         XX     XXX         XX     XXXXXXXX     X       X    X  X      X      X      X
   XXX          XX      XXX    XXX      XX            X       X    X  X      X      X      X
XXXXXXXX         XX       XXXXXX      XXX             X       X    X  X      X      X      X
XXXXXXXX          XXXXXXXXXXXXXXXXXXXXXX              XXXXXX  XXXXXX  X      X      XXXXX  XXXXX
'''
    jogo_da_forca_logo = '''
XXXXXXXXXXXXXX       XXXXXX  XXXXXX  XXXXXX   XXXXXX      XXXXX   XXXXXX      XXXXX  XXXXXX  XXXX    XXXXXX  XXXXXX
XXXXXXXXXXXXXX           X   X    X  X    X   X    X      X    X  X    X      X      X    X  X   X   X       X    X
   XX     X              X   X    X  X        X    X      X    X  X    X      X      X    X  X    X  X       X    X
   XX     X              X   X    X  X        X    X      X    X  XXXXXX      XXXXX  X    X  XXXXXX  X       XXXXXX
   XX    X X             X   X    X  X        X    X      X    X  X    X      X      X    X  X    X  X       X    X
   XX     X              X   X    X  X        X    X      X    X  X    X      X      X    X  X    X  X       X    X
   XX                    X   X    X  X        X    X      X    X  X    X      X      X    X  X    X  X       X    X
   XX                    X   X    X  X   XX   X    X      X    X  X    X      X      X    X  X    X  X       X    X
   XX                    X   X    X  X    X   X    X      X    X  X    X      X      X    X  X    X  X       X    X
   XX                X   X   X    X  X    X   X    X      X    X  X    X      X      X    X  X    X  X       X    X
   XX                 XXXX   XXXXXX  XXXXXX   XXXXXX      XXXXX   X    X      X      XXXXXX  X    X  XXXXXX  X    X 
'''

    maquina_cafe_logo = '''
XXXXXXXXXXXXXXXXXXXXXXXX      XX   XX  XXXXXX  XXXXXX  X    X  XXXXX  XX    X  XXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX XXXXXXXXXXX        XX      X X X X  X    X  X    X  X    X    X    XX    X  X    X     XX       XXXX     XXXXXX      XX
XX X         X  XXXXX XX      X  X  X  X    X  X    X  X    X    X    X X   X  X    X     XX    XXXX  XX   XX    XXX    XXXXXX
XX X   XXXX  X  XXXXX XX      X  X  X  XXXXXX  X    X  X    X    X    X X   X  XXXXXX     XX   XX      XXXX        XX   XX   XX
XX X   XXX   X  XXXXX XX      X     X  X    X  X    X  X    X    X    X  X  X  X    X     XX   XX        X         XX   XX    X
XX XXXXXXXXXXX  XXXXX XX      X     X  X    X  X    X  X    X    X    X  X  X  X    X     XX    XX                XX    XX    X
XX                    XX      X     X  X    X  X    X  X    X    X    X  X  X  X    X      XX    XXX             XX    XX     X
XX  XXXXXXXX   X X X  XX      X     X  X    X  X    X  X    X    X    X   X X  X    X       XX     XXX         XX     XXXXXXXX
XX  XXXXXXXX   X X X  XX      X     X  X    X  X X  X  X    X    X    X   X X  X    X        XX      XXX    XXX      XX
XX                    XX      X     X  X    X  X  X X  X    X    X    X    XX  X    X         XX       XXXXXX      XXX
XXXXXXXXXXXXXXXXXXXXXXXX      X     X  X    X  XXXXXX  XXXXXX  XXXXX  X    XX  X    X          XXXXXXXXXXXXXXXXXXXXXX
'''

    mercado_logo = '''
+---------+     XX   XX  XXXXXX  XXXX    XXXXXX  XXXXXX  XXXX    XXXXXX     +---------+
|    |    |     X X X X  X       X   X   X       X    X  X   X   X    X     |    |    |
| +-----+ |     X  X  X  X       X    X  X       X    X  X    X  X    X     | +-----+ |
| |  |    |     X  X  X  XXXXXX  XXXXXX  X       XXXXXX  X    X  X    X     | |  |    |
| |  |    |     X     X  X       X    X  X       X    X  X    X  X    X     | |  |    |
| +-----+ |     X     X  X       X    X  X       X    X  X    X  X    X     | +-----+ |
|    |  | |     X     X  X       X    X  X       X    X  X    X  X    X     |    |  | |
|    |  | |     X     X  X       X    X  X       X    X  X    X  X    X     |    |  | |
| +-----+ |     X     X  X       X    X  X       X    X  X    X  X    X     | +-----+ |
|    |    |     X     X  X       X    X  X       X    X  X   X   X    X     |    |    |
+---------+     X     X  XXXXXX  X    X  XXXXXX  X    X  XXXX    XXXXXX     +---------+
'''

    instrucoes_logo = '''
+-----------+       XXXX    XXXXXX  XXXXXX  XXXXXX  XXXX    XXXXX  XXXXXX  XXXXXX  XXXXXX  XXXXXX       +-----------+
| --------- |       X   X   X       X       X       X   X     X    X       X    X  X       X            | --------- |
| --------- |       X    X  X       X       X       X    X    X    X       X    X  X       X            | --------- |
| --------- |       X    X  XXXXXX  XXXXXX  X       XXXXXX    X    X       X    X  XXXXXX  XXXXXX       | --------- |
| --------- |       X    X  X            X  X       X    X    X    X       X    X  X            X       | --------- |
| --------- |       X    X  X            X  X       X    X    X    X       X    X  X            X       | --------- |
| --------- |       X    X  X            X  X       X    X    X    X       X    X  X            X       | --------- |
| --------- |       X    X  X            X  X       X    X    X    X       X    X  X            X       | --------- |
| --------- |       X    X  X            X  X       X    X    X    X       X    X  X            X       | --------- |
| --------- |       X   X   X            X  X       X    X    X    X       X    X  X            X       | --------- |
+-----------+       XXXX    XXXXXX  XXXXXX  XXXXXX  X    X  XXXXX  XXXXXX  XXXXXX  XXXXXX  XXXXXX       +-----------+
'''

    pedra_papel_tesoura_logo = '''
+-------------------------------+-------------------------------+-------------------------------------------+
| XXXXX XXXXX XXX   XXX   XXXXX | XXXXX XXXXX XXXXX XXXXX X     | XXXXX XXXXX XXXXX XXXXX X   X XXX   XXXXX |
| X   X X     X  X  X  X  X   X | X   X X   X X   X X     X     |   X   X     X     X   X X   X X  X  X   X |
| X   X X     X   X X   X X   X | X   X X   X X   X X     X     |   X   X     X     X   X X   X X   X X   X |
| XXXXX XXXXX X   X XXXXX XXXXX | XXXXX XXXXX XXXXX XXXXX X     |   X   XXXXX XXXXX X   X X   X XXXXX XXXXX |
| X     X     X   X X   X X   X | X     X   X X     X     X     |   X   X         X X   X X   X X   X X   X |
| X     X     X   X X   X X   X | X     X   X X     X     X     |   X   X         X X   X X   X X   X X   X |
| X     X     X   X X   X X   X | X     X   X X     X     X     |   X   X         X X   X X   X X   X X   X |
| X     X     X   X X   X X   X | X     X   X X     X     X     |   X   X         X X   X X   X X   X X   X |
| X     X     X   X X   X X   X | X     X   X X     X     X     |   X   X         X X   X X   X X   X X   X |
| X     X     X  X  X   X X   X | X     X   X X     X     X     |   X   X         X X   X X   X X   X X   X |
| X     XXXXX XXX   X   X X   X | X     X   X X     XXXXX XXXXX |   X   XXXXX XXXXX XXXXX XXXXX X   X X   X |
+-------------------------------+-------------------------------+-------------------------------------------+
'''
    jogo_da_velha_logo = '''
                        +-------------------------+-------------+-------------------------------+
  X   |   X X  |        | XXXXX XXXXX XXXXX XXXXX | XXX   XXXXX | X   X XXXXX X     X   X XXXXX |        |        | X X
 X X  |    X   |        |    X  X   X X   X X   X | X  X  X   X | X   X X     X     X   X X   X |        |        |  X
  X   |   X X  |        |    X  X   X X     X   X | X   X X   X | X   X X     X     X   X X   X |        |        | X X
----------------------  |    X  X   X X     X   X | X   X XXXXX | X   X XXXXX X     XXXXX XXXXX |  ----------------------
      |   X X  |        |    X  X   X X     X   X | X   X X   X | X   X X     X     X   X X   X |   X X  |   X    |
      |    X   |        |    X  X   X X     X   X | X   X X   X |  X X  X     X     X   X X   X |    X   |  X X   |
      |   X X  |        |    X  X   X X     X   X | X   X X   X |  X X  X     X     X   X X   X |   X X  |   X    |
----------------------  |    X  X   X X XXX X   X | X   X X   X |  X X  X     X     X   X X   X |  ----------------------
      |  X X   |   X    |    X  X   X X   X X   X | X   X X   X |  X X  X     X     X   X X   X |        |  X X   |
      |   X    |  X X   | X  X  X   X X   X X   X | X  X  X   X |  X X  X     X     X   X X   X |        |   X    |
      |  X X   |   X    |  XXX  XXXXX XXXXX XXXXX | XXX   X   X |   X   XXXXX XXXXX X   X X   X |        |  X X   |
                        +-------------------------+-------------+-------------------------------+ 
'''

    banco_logo = '''
XXXXXXXXXXXXXXX     XXXXXX    XXXXXX   XX    X   XXXXXX   XXXXXX     +----+----+
XXX         XXX     X     X   X    X   XX    X   X        X    X     |    |    |
XX   $$$$$   XX     X     X   X    X   X X   X   X        X    X     | +----+  |
XX   $$$$$   XX     XXXXXX    XXXXXX   X X   X   X        X    X     | |  |    |
XX           XX     X     X   X    X   X  X  X   X        X    X     | |  |    |
XXXXXXXXXXXXXXX     X     X   X    X   X  X  X   X        X    X     | +----+  |
XXXXX     XXXXX     X     X   X    X   X  X  X   X        X    X     |    | |  |
XX  XXX XXX  XX     X     X   X    X   X   X X   X        X    X     |    | |  |
XX   XXXXX   XX     X     X   X    X   X   X X   X        X    X     | +----+  |
XXXXXX   XXXXXX     X     X   X    X   X    XX   X        X    X     |    |    |
XXXXXXXXXXXXXXX     XXXXXX    X    X   X    XX   XXXXXX   XXXXXX     +----+----+ 
'''

    ranking_logo = '''
                     XXXX     XXXXXX   XX    X   X   X   XXXXX   XX    X   XXXXXX            O  X
   XXXXXXXXXXX       X   X    X    X   XX    X   X  X      X     XX    X   X    X            | X
 XXX         XXX     X    X   X    X   X X   X   X X       X     X X   X   X              XXX|X
XXX     X     XXX    XXXXXX   XXXXXX   X X   X   XX        X     X X   X   X                 |
XX    X X      XX    X    X   X    X   X  X  X   XX        X     X  X  X   X                X X
XX      X      XX    X    X   X    X   X  X  X   XX        X     X  X  X   X               X   X
XX      X      XX    X    X   X    X   X  X  X   X X       X     X  X  X   X              +-----+
XX    XXXXX    XX    X    X   X    X   X   X X   X X       X     X   X X   X  XXX         | 1st |
 XXX         XXX     X    X   X    X   X   X X   X  X      X     X   X X   X    X         |     +----+
  XXXXXXXXXXXXX      X    X   X    X   X    XX   X  X      X     X    XX   X    X    +----+     |    |
                     X    X   X    X   X    XX   X   X   XXXXX   X    XX   XXXXXX    +----------+----+

'''

    def instrucoes(self):

        def ler_texto(texto):
            if name == 'nt':
                print(texto)
            else:
                for letra in texto:
                    sleep(0.5)
                    print(letra, end='')

        escolha = input('\nBem vindo(a) ao Menu de Instruções, escolha uma das opções para saber mais:'
                            '\n1- História Geral\n2- Jogo da Forca\n3- Mercado\n4- Máquina de café\n5- Pedra Papel Tesoura'
                            '6- Banco\n7- Jogo da Velha\n8- Ranking Rei do Café\nSair -> para sair deste menu\n')
        while escolha.lower() != 'sair':
            print('*' * 125)
            if escolha == '1':
                ler_texto(self.historia_geral_desc)
            elif escolha == '2':
                ler_texto(self.jogo_da_forca_desc)
            elif escolha == '3':
                ler_texto(self.mercado_desc)
            elif escolha == '4':
                ler_texto(self.maquina_cafe_desc)
            elif escolha == '5':
                ler_texto(self.pedra_papel_tesoura_desc)
            elif escolha == '6':
                ler_texto(self.banco_desc)
            elif escolha == '7':
                ler_texto(self.jogo_da_velha_desc)
            elif escolha == '8':
                ler_texto(self.ranking_desc)
            print('*' * 125)
            escolha = input('\nBem vindo(a) ao Menu de Instruções, escolha uma das opções para saber mais:'
                            '\n1- História Geral\n2- Jogo da Forca\n3- Mercado\n4- Máquina de café\n5- Pedra Papel Tesoura'
                            '6- Banco\n7- Jogo da Velha\n8- Ranking Rei do Café\nSair -> para sair deste menu\n')
