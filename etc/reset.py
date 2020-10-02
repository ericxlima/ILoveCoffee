from json import dumps


'''Execute este Módulo para resetar pro padrão o arquivo etc/usuarios.json'''


def resetar():
    """Reseta o arquivo etc/usuarios.json para os valores padrão"""
    reset = {
        "usuarios": [
            {
                "nome": "Eric",
                "senha": "1234",
                "pontos": 2500,
                "rank": 500,
                "recursos": {
                    "agua": 700,
                    "leite": 1100,
                    "cafe": 1044,
                    "copos": 15,
                    "dinheiro": 1868
                }
            },
            {
                "nome": "Jorge",
                "senha": "fHdbpJUV2mIjJLY5Ym4g",
                "pontos": 450,
                "rank": 450,
                "recursos": {
                    "agua": 600,
                    "leite": 300,
                    "cafe": 100,
                    "copos": 9,
                    "dinheiro": 0
                }
            },
            {
                "nome": "Matt",
                "senha": "7yYwrsRzAudqnV06rJ5Y",
                "pontos": 425,
                "rank": 425,
                "recursos": {
                    "agua": 600,
                    "leite": 300,
                    "cafe": 100,
                    "copos": 9,
                    "dinheiro": 0
                }
            },
            {
                "nome": "Julin",
                "senha": "GdTROx9Cz7mlR4XJnaG8",
                "pontos": 400,
                "rank": 400,
                "recursos": {
                    "agua": 600,
                    "leite": 300,
                    "cafe": 100,
                    "copos": 9,
                    "dinheiro": 0
                }
            },
            {
                "nome": "Ivon",
                "senha": "Y0qsE2BMgp24dQ0Gc7Qz",
                "pontos": 0,
                "rank": 375,
                "recursos": {
                    "agua": 600,
                    "leite": 300,
                    "cafe": 100,
                    "copos": 9,
                    "dinheiro": 0
                }
            },
            {
                "nome": "Vava",
                "senha": "AyFmvC8WLLJ18g2LwzGH",
                "pontos": 1020,
                "rank": 350,
                "recursos": {
                    "agua": 604,
                    "leite": 304,
                    "cafe": 100,
                    "copos": 12,
                    "dinheiro": 0
                }
            }
        ]
    }

    with open('usuarios.json', 'w+') as file:
        reset_json_file = dumps(reset, indent=4)
        file.write(reset_json_file)


resetar()
