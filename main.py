from etc.instrucoes import menu
from scrips.maquina_cafe import CoffeeMachine
from scrips.jogo_da_forca import Jogo
from scrips.usuario import usuario
from scrips.mercado import Mercado
from scrips.pedra_papel_tesoura import PedraPapelTesoura
from scrips.jogo_da_velha import JogoDaVelha

nick, senha = usuario()


def menu_principal():
    print('Seja bem vindo(a)\nO que deseja fazer?')
    user = input('1- Jogo da Forca\n2- Máquina de café\n3- Mercado\n4- Instruções\n 5- Pedra, Papel e Tesoura'
                 '6- Jogo da Velha'
                 '\n Sair - para sair do programa')
    while user != 'sair':
        if user == '1':
            Jogo(nick, senha)
        elif user == '2':
            CoffeeMachine(nick, senha)
        elif user == '3':
            Mercado(nick, senha)
        elif user == '4':
            menu()
        elif user == '5':
            PedraPapelTesoura(nick, senha)
        elif user == '6':
            JogoDaVelha(nick, senha)
        user = input('1- Jogar o Jogo da Forca\n2- Ir para a Máquina de café\n Sair - para sair do programa')
