def usuario():
    """ Checa se o usuário está ou não cadastrado no sistema, e o retorna"""

    cadastrado = input('Você já está cadastrado no sistema?[S/N]')
    if cadastrado == 'S':
        user_name = input('Qual o seu Nickname? ')
        user_senha = input('Qual a sua senha? ')
    else:
        user_name = input('Qual o seu nome? ')
        user_age = int(input('Qual sua data de nascimento? '))
        user_timer = None   #  O tempo que ele joga começará a contar a partir daqui
        user_nick = input('Qual o seu nick para o Jogo? [3 caracteres]')
        senha = input('Qual a senha? ')
        dados = [(user_nick, senha), {'user_name': user_name, 'user_age': user_age,
                                      'user_timer': user_timer, 'user_score': 0}]
        with open('../txt/user_info.txt', 'r+') as file:
            file.write(f'{dados}')


def checagem(nick, senha):
    with open('user_info', 'r+') as file:
        lines = file.readlines()
        for line in lines:
            if f'{nick}, {senha}' in line:
                return True
            else:
                return False
