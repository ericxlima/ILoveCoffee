from os import system, name

from etc.instrucoes import Descricoes
from scrips.banco import Banco
from scrips.jogo_da_forca import JodoDaForca
from scrips.jogo_da_velha import JogoDaVelha
from scrips.maquina_cafe import MaquinaDeCafe
from scrips.mercado import Mercado
from scrips.pedra_papel_tesoura import PedraPapelTesoura
from scrips.usuario import usuario
#from etc.ranking import Rank


def limpar():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def menu_principal():
    limpar()
    login = usuario()
    limpar()
    print(Descricoes.logo)
    print('\n' + Descricoes.historia_geral_desc)
    print('\nSeja bem vindo(a) ao Menu Principal\n\nO que deseja fazer?')
    user = input('1- Jogo da Forca\n2- Máquina de café\n3- Mercado\n4- Instruções\n5- Pedra, Papel e Tesoura\n'
                 '6- Jogo da Velha\n7- Banco\n8- Ranking\nSair - para sair do programa\n>>> ').strip()

    while user != 'sair':
        limpar()
        if user == '1':
            JodoDaForca(login)
        elif user == '2':
            MaquinaDeCafe(login)
        elif user == '3':
            Mercado(login)
        elif user == '4':
            Descricoes().instrucoes()
        elif user == '5':
            PedraPapelTesoura(login)
        elif user == '6':
            JogoDaVelha(login)
        elif user == '7':
            Banco(login)
        #elif user == '8':
            #Rank()
        limpar()
        print(Descricoes.logo)
        print('\n' + Descricoes.historia_geral_desc)
        print('\nSeja bem vindo(a) ao Menu Principal\n\nO que deseja fazer?')
        user = input('1- Jogo da Forca\n2- Máquina de café\n3- Mercado\n4- Instruções\n5- Pedra, Papel e Tesoura\n'
                     '6- Jogo da Velha\n7- Banco\n8- Ranking\nSair - para sair do programa\n>>> ').strip()


if __name__ == '__main__':
    menu_principal()
else:
    raise Exception('Este arquivo não deve ser importado, apenas executado')
