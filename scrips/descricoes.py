def historia_geral():
    texto = ''' Seja Bem-Vindo(a) ao seu primeiro emprego.\n
    Nesta cafeteria como você pode ver, temos de tudo um pouco.\n
    Aqui você pode fazer de tudo para ganhar pontos, que poderá ser usado para trocar por dinheiro\n
    O seu objetivo é conseguir o máximo de cafeína tomado para conseguir ser o Rei do Café.\n
    Quantas xícaras de café és capaz de tomar?...\n '''

    return texto


def jogo_da_forca_desc():
    texto = 'No Jogo da Forca, o usuário tem 8 vidas e o objetivo do jogo é acertar o máximo de letras da palavra' \
            'desconhecida. Existem 3 categorias do jogo, e um total de 40 palavras. Ao completar uma palavra' \
            'você ganha um total de 100 pontos para cada vida restante.'
    return texto


def mercado_desc():
    texto = 'O Mercado é o lugar onde você pode trocas pontos por ingredientes (água, leite e café)' \
            ' além de copos e dinheiro. Caso você não tenha pontos sufientes, a compra não será efetuada.' \
            'Caso você esteja precisando urgentemente realizar a compra, não exite em tentar um empréstimo no banco :)'
    return texto


def maquina_cafe_desc():
    texto = 'A Máquina de Café é sem dúvidas a melhor parte desta experiência do ILoveCoffe, é o objetivo principal' \
            ' do mesmo. Na Máquina de Café você pode utilizar seus ingredientes e dinheiro para fazer cafés' \
            ' deliciosos. Temos 3 opções de Café, ambos variam em quantidades de produtos, e quanto mais café você' \
            'toma, mais próximo do topo no "Ranking Do Rei do Café" você fica.'
    return texto


def menu():
    escolha = input('Bem vindo(a) ao Menu de Instruções, escolha uma das opções para saber mais:'
                    '1- História Geral\n 2- Jogo da Forca\n 3- Mercado\n 4- Máquina de café')
    if escolha == '1':
        print(historia_geral())
    elif escolha == '2':
        print(jogo_da_forca_desc())
    elif escolha == '3':
        print(mercado_desc())
    elif escolha == '4':
        print(maquina_cafe_desc())
