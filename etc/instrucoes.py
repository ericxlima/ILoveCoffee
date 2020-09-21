def historia_geral():
    texto = '''Seja Bem-Vindo(a) ao seu primeiro emprego.Nesta cafeteria como você pode ver, temos de tudo um pouco.
Aqui você pode fazer de tudo para ganhar pontos, que poderá ser usado para trocar por dinheiro. O seu objetivo é 
conseguir o máximo de cafeína tomado para conseguir ser o Rei do Café. Quantas xícaras de café és capaz de tomar?...'''
    return texto


def jogo_da_forca_desc():
    texto = '''No Jogo da Forca, o usuário tem 8 vidas e o objetivo do jogo é acertar o máximo de letras da palavra
desconhecida. Existem 3 categorias do jogo, e um total de 40 palavras. Ao completar uma palavra você ganha um total
de 100 pontos para cada vida restante.'''
    return texto


def mercado_desc():
    texto = '''O Mercado é o lugar onde você pode trocas pontos por ingredientes (água, leite e café) além de copos e
dinheiro. Caso você não tenha pontos sufientes, a compra não será efetuada. Caso você esteja precisando urgentemente
realizar a compra, não exite em tentar um empréstimo no banco :)'''
    return texto


def maquina_cafe_desc():
    texto = '''A Máquina de Café é sem dúvidas a melhor parte desta experiência do ILoveCoffe, é o objetivo principal
do mesmo. Na Máquina de Café você pode utilizar seus ingredientes e dinheiro para fazer cafés deliciosos. Temos 3 
opções de Café, ambos variam em quantidades de produtos, e quanto mais café você toma, mais próximo do topo no 
"Ranking Do Rei do Café" você fica.'''
    return texto


def pedra_papel_tesoura():
    texto = '''O Jogo "Pedra Papel Tesousa" é exatamente como o clássico, cada vez que você ganhar um jogo contra a
máquina, ganha 100 pontos. Quando perder, perde 50 pontos e em casos de empate, não ganha nada. O jogo utiliza um 
sistema de pseudo-aleatoriedade, e não é do jeito que está, não é possível prever as jogadas da máquina. Divirta-se 
jogando, nas suas vitórias e derrotas :)'''
    return texto


def banco():
    texto = '''No Banco você pode fazer pequenos empréstimos com base no "Ranking do Rei do Café", além disso, você pode
fazer cartões de crédito, e realizar depósitos em contas de amigos/parceiros. O dinheiro pode ser visto como um item
de "ostentação" no jogo ultimamente, futuramente adicionaremos novas funções para fazer com o dinheiro. Até lá,
depositem o máximo que conseguirem :)'''
    return texto


def jogo_da_velha():
    texto = '''O jogo da Velha é o primeiro projeto MultiPlayer do ILoveCoffe, o plano é fazer com que nele possamos
logar dois players simultaneamente, e suas respectivas pontuações. Nele, 2 players poderão jogar PvP (Player vs Player)
até com que um saia vencedor ou dê velha. As pontuações serão definidas depois...'''
    return texto


def instrucoes():
    escolha = input('\nBem vindo(a) ao Menu de Instruções, escolha uma das opções para saber mais:'
                    '\n1- História Geral\n2- Jogo da Forca\n3- Mercado\n4- Máquina de café\n5- Pedra Papel Tesoura'
                    '6- Banco\n7- Jogo da Velha\nSair -> para sair deste menu')
    while escolha.lower() != 'sair':
        print('*'*45)
        if escolha == '1':
            print(historia_geral())
        elif escolha == '2':
            print(jogo_da_forca_desc())
        elif escolha == '3':
            print(mercado_desc())
        elif escolha == '4':
            print(maquina_cafe_desc())
        elif escolha == '5':
            print(pedra_papel_tesoura())
        elif escolha == '6':
            print(banco())
        elif escolha == '7':
            print(jogo_da_forca_desc())
        print('*' * 45)
        escolha = input('\nBem vindo(a) ao Menu de Instruções, escolha uma das opções para saber mais:'
                        '\n1- História Geral\n2- Jogo da Forca\n3- Mercado\n4- Máquina de café\n5- Pedra Papel Tesoura'
                        '6- Banco\n7- Jogo da Velha\nSair -> para sair deste menu')
