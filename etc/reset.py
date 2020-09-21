from json import dumps


def resetar():
    """Reseta o arquivo etc/usuarios.json para os valores padrão"""
    reset = {"usuarios": [{
        "nome": "Eric",
        "senha": "1234",
        "pontos": 0,
        "rank": 0,
        "recursos": {"agua": 1600,
                     "leite": 1300,
                     "cafe": 1100,
                     "copos": 19,
                     "dinheiro": 1000}
    }]}

    with open('usuarios.json', 'w+') as file:
        reset_json_file = dumps(reset, indent=4)
        file.write(reset_json_file)


resetar()
