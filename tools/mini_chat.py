class MiniChat:

    def __init__(self):
        self.bot_name = 'Sentinela'
        self.bot_birth_year = '2020'
        self.name = None
        self.exe()

    def inicio(self):
        print(f'Olá! Meu nome é {self.bot_name}.')
        print(f'Eu fui criado em {self.bot_birth_year} by Eric de Lima.')
        self.name = input('Por favor, informe o seu nome: ')
        print(f'Você tem um ótimo nome, {self.name}!')

    def advinhar(self):
        print('O que faremos agora? Bem... Vamos advinhar a sua idade em alguns passos matemáticos')
        numero = int(input('Primeiro, insira um número qualquer entre 2 e 9: '))
        while numero not in range(2, 10):
            print('O número tem de estar entre 2 e 9')
            numero = input(int(input('Primeiro, insira um número qualquer entre 2 e 9: ')))
        print(f'Ao multiplicarmos {numero} por 2 temos {numero * 2}')
        print(f'Somando 5 ao resultado tempos {(numero * 2) + 5}')
        print(f'Agora multiplicamos isso tudo por 50, ficando com {(numero * 2 + 5) * 50}')
        idade = input('Você já completou aniversário este ano? [S/N]')
        while idade not in ['S', 'N']:
            if idade == 'S':
                numero = ((numero * 2 + 5) * 50) + 1769
                print(f'Então somamos ao resultado 1769 ficando com {numero}')
            else:
                numero = ((numero * 2 + 5) * 50) + 1768
                print(f'Então somamos ao resultado 1768 ficando com {numero}')
        nasc = int(input('Insira por favor o ano que você nasceu: '))
        print(f'Diminuindo {numero} (número final) por {nasc} (seu ano de nascimento) ficamos com {numero - nasc}')
        print(f'Se você prestar atenção neste número, o primeiro dígito é o número que você advinhou'
              f' e os outros dois últimos é justamente sua idade atual {self.name} :)')

    def count(self):
        print(f'Hey {self.name}Eu tenho a habilidade de contar até um número informado')
        num = int(input('Me informa um número para ver: '))
        curr = 0
        while curr <= num:
            print(curr, '!')
            curr = curr + 1

    def test(self):
        print("Por último, vamos fazer um pequeno teste, para saber suas competências acadêmicas hehehe")
        print('Qual país abaixo está localizado no continente conhecido como "Novo Mundo"?')
        print('1. China\n2. Australia\n3. Panama\n4. Etiópia\n5. UK ')
        answer = int(input().strip())
        while answer != 3:
            print('Você errou, tente novamente... :(')
            answer = int(input().strip())
        print(f'Parabéns {self.name}, Você conseguiu com sucesso passar pela trilha do mini-bot!')
        print('Espero que tenha gostado da experiência, att. Sentinela')

    def exe(self):
        self.inicio()
        self.advinhar()
        self.count()
        self.test()
        print('Parabéns mais uma vez e tenha um ótimo dia!')
