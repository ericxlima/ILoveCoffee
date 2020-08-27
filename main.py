from etc.descricoes import menu
from scrips.maquina_cafe import CoffeeMachine
from scrips.jogo_da_forca import Jogo
from scrips.usuario import usuario
from scrips.mercado import Mercado
from scrips.Pedra_Papel_tesoura import PedraPapelTesoura

nick, senha = usuario()


def menu_principal():
    print('Seja bem vindo(a)\nO que deseja fazer?')
    user = input('1- Jogo da Forca\n2- Máquina de café\n3- Mercado\n4- Instruções\n 5- Pedra, Papel e Tesoura'
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
        user = input('1- Jogar o Jogo da Forca\n2- Ir para a Máquina de café\n Sair - para sair do programa')
