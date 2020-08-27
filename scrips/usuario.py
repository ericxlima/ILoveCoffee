def usuario():
    """ Checa se o usuário está ou não cadastrado no sistema, e o retorna"""

    cadastrado = input('Você já está cadastrado no sistema?[S/N]').upper()
    if cadastrado == 'S':
        user_nick = input('Insira seu Nickname: ')
        user_senha = input('Insira sua senha: ')
    else:
        user_nick = input('Insira um NickName: ')
        user_senha = input('Qual a senha? ')
        criar_usuario(user_nick, user_senha)
    return user_nick, user_senha


def criar_usuario(nome, senha):
    novo_usuario = {
        'usuarios': [
            {'nome': nome,
             'senha': senha,
             'pontos': 0,
             'recursos': {'agua': 600,
                          'leite': 300,
                          'cafe': 100,
                          'dinheiro': 0}
             }
        ]
    }
    '''
        Falta aprender a trabalhar com arquivos json para abrir o arquivo etc.usuarios.json e add este usuário
    '''
    return
