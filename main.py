from os import system, name

from etc.instrucoes import Descricoes
from scrips.banco import Banco
from scrips.jogo_da_forca import JodoDaForca
from scrips.jogo_da_velha import JogoDaVelha
from scrips.maquina_cafe import MaquinaDeCafe
from scrips.mercado import Mercado
from scrips.pedra_papel_tesoura import PedraPapelTesoura
from scrips.usuario import usuario
from etc.ranking import Rank


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
            print(Descricoes.jogo_da_forca_logo)
            JodoDaForca(login)
        elif user == '2':
            print(Descricoes.maquina_cafe_logo)
            MaquinaDeCafe(login)
        elif user == '3':
            print(Descricoes.mercado_logo)
            Mercado(login)
        elif user == '4':
            print(Descricoes.instrucoes_logo)
            Descricoes().instrucoes()
        elif user == '5':
            print(Descricoes.pedra_papel_tesoura_logo)
            PedraPapelTesoura(login)
        elif user == '6':
            print(Descricoes.jogo_da_velha_desc)
            JogoDaVelha(login)
        elif user == '7':
            print(Descricoes.banco_logo)
            Banco(login)
        elif user == '8':
            print(Descricoes.ranking_logo)
            Rank()
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
