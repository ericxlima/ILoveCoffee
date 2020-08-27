from scrips.descricoes import historia
from scrips.maquina_cafe import CoffeeMachine
from scrips.jogo_da_forca import Jogo
from scrips.usuario import usuario

print(historia())
nick, senha = usuario()


def menu():
    print('Seja bem vindo(a)\nO que deseja fazer?')
    user = input('1- Jogar o Jogo da Forca\n2- Ir para a Máquina de café\n Sair - para sair do programa')
    while user != 'sair':
        if user == '1':
            Jogo(nick, senha)
        else:
            CoffeeMachine(nick, senha)
        user = input('1- Jogar o Jogo da Forca\n2- Ir para a Máquina de café\n Sair - para sair do programa')


menu()
