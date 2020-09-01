import json


def geral():
    """ Checa se o usuário está ou não cadastrado no sistema, e o retorna"""

    cadastrado = input('Você já está cadastrado no sistema?[S/N]').upper()
    if cadastrado == 'S':
        user_nick = input('Insira seu Nickname: ')
        user_senha = input('Insira sua senha: ')
        if check(user_nick, user_senha):
            return user_nick, user_senha
        print('Usuário e/ou senha incorreto')
        return False
    else:
        user_nick = input('Insira um NickName (não poderá ser alterado): ')
        user_senha = input('Insira sua senha (não pdoerá ser alterada): ')
        criar_usuario(user_nick, user_senha)
        return user_nick, user_senha


def criar_usuario(nome, senha):
    novo_usuario = {'nome': nome,
                    'senha': senha,
                    'pontos': 0,
                    'recursos': {'agua': 600,
                                 'leite': 300,
                                 'cafe': 100,
                                 'copos': 9,
                                 'dinheiro': 0}}
    file = open("../etc/usuarios.json", 'r+')
    usuarios_json = json.load(file)
    usuarios_json['usuarios'].append(novo_usuario)
    usuarios_json = json.dumps(usuarios_json, indent=4)
    file.write(usuarios_json)
    file.close()


def check(nome, senha):
    """Checa se o nome e a senha foram inseridos de forma correta"""

    with open("../etc/usuarios.json", 'r+') as file:
        lines = json.load(file)
    for pessoa in lines['usuarios']:
        if pessoa['nome'] == nome and pessoa['senha'] == senha:
            return True
    return False


def usuario():
    while not geral():
        geral()
