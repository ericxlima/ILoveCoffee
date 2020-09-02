from etc.instrucoes import menu, historia_geral
from scrips.maquina_cafe import CoffeeMachine
from scrips.jogo_da_forca import Jogo
from scrips.usuario import usuario
from scrips.mercado import Mercado
from scrips.pedra_papel_tesoura import PedraPapelTesoura
from scrips.jogo_da_velha import JogoDaVelha


def menu_principal(log):
    print('\n' + historia_geral())
    print('\nSeja bem vindo(a) ao Menu Principal\n\nO que deseja fazer?')
    user = input('1- Jogo da Forca\n2- Máquina de café (em construção)\n3- Mercado\n4- Instruções\n'
                 '5- Pedra, Papel e Tesoura\n6- Jogo da Velha\n Sair - para sair do programa\n')
    while user != 'sair':
        if user == '1':
            Jogo(log)
        elif user == '2':
            CoffeeMachine(log)
        elif user == '3':
            Mercado(log)
        elif user == '4':
            menu()
        elif user == '5':
            PedraPapelTesoura(log)
        elif user == '6':
            JogoDaVelha(log)
        print('\nSeja bem vindo(a) ao Menu Principal\n\nO que deseja fazer?')
        user = input('1- Jogo da Forca\n2- Máquina de café\n3- Mercado\n4- Instruções\n5- Pedra, Papel e Tesoura\n'
                     '6- Jogo da Velha\n Sair - para sair do programa\n')


login = usuario()  # nick e senha
menu_principal(login)
