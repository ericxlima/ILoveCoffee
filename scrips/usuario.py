import json


def usuario():
    """ Checa se o usuário está ou não cadastrado no sistema, e o retorna"""

    nick, senha = None, None
    while (nick, senha) == (None, None):
        cadastrado = input('\nVocê já está cadastrado no sistema?[S/N] ').upper()
        if cadastrado == 'S':
            user_nick = input('Insira seu Nickname: ')
            user_senha = input('Insira sua senha: ')
            if check(user_nick, user_senha):
                nick, senha = user_nick, user_senha
            else:
                print('Usuário e/ou senha incorreto')
        elif cadastrado == 'N':
            user_nick = input('Insira um NickName (não poderá ser alterado): ').strip()
            user_senha = input('Insira sua senha (não pdoerá ser alterada): ').strip()
            if check(user_nick):
                criar_usuario(user_nick, user_senha)
                nick, senha = user_nick, user_senha
            else:
                print('Nickname já cadastrado, escolha outro')
        else:
            print('Insira "S" caso esteja cadastrado ou "N" caso não esteja cadastrado e queira se cadastrar')
    return nick


def criar_usuario(nome, senha):
    novo_usuario = {'nome': nome,
                    'senha': senha,
                    'pontos': 0,
                    "rank": 0,
                    'recursos': {'agua': 600,
                                 'leite': 300,
                                 'cafe': 100,
                                 'copos': 9,
                                 'dinheiro': 0}}
    with open("etc/usuarios.json", 'r') as file:
        usuarios_json = json.load(file)
    usuarios_json['usuarios'].append(novo_usuario)
    usuarios_json = json.dumps(usuarios_json, indent=4)
    with open("etc/usuarios.json", 'w') as file:
        file.write(usuarios_json)


def check(nome, senha=None):
    """Retorna True se o nome/senha estiver correta"""

    with open("etc/usuarios.json", 'r+') as file:
        lines = json.load(file)
    if nome and senha:
        for pessoa in lines['usuarios']:
            if (pessoa['nome'], pessoa['senha']) == (nome, senha):
                return True
        return False
    elif nome:
        if nome not in [pessoa['nome'] for pessoa in lines['usuarios']]:
            return True
        return False
