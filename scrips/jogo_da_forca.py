from random import choice
import json


class JodoDaForca:

    def __init__(self, nick):

        self.categorias = {'animais': ['coelho', 'cavalo', 'coruja', 'gaivota', 'porco', 'galinha',
                                       'macaco', 'baleia', 'golfinho', 'morcego', 'girafa', 'elefante',
                                       'castor', 'calango', 'flamingo', 'guepardo', 'hamster', 'serpente'],
                           'alimentos': ['pepino', 'graviola', 'espaguete', 'manteiga', 'feijoada', 'lasanha',
                                         'palmito', 'ervilha', 'repolho', 'pamonha', 'caramelo', 'chiclete',
                                         'gengibre', 'gelatina', 'lentilha', 'pimenta', 'sorvete'],
                           'geral': ['paraquedas', 'lombada', 'ventilador', 'caminhonete', 'violino', 'despertador',
                                     'camisola', 'banheira', 'choveiro', 'mochila', 'computador', 'fotografia',
                                     'brinquedo', 'revolver', 'esquadro', 'monitor', 'pincel', 'vasilhame']
                           }
        self.nick = nick
        self.pontuacao = 0
        self.exe()

    def jogar(self, categoria):
        palavra = choice(self.categorias[categoria])
        word_hifens = ['-' for _ in palavra]

        lifes = 8
        list_letters = []
        while lifes > 0:
            print('\n' + ''.join(word_hifens))
            letter = input('Insira uma letra: ')
            # Possíveis enganos
            if letter in list_letters:
                print('Você já digitou esta letra')
            elif len(letter) != 1:
                print('Você deve inserir uma única letra')
            elif not letter.islower() or not letter.isalpha():
                print('Você deve inserir uma letra minúscula')
            else:
                if letter not in palavra:
                    lifes -= 1
                    print('Não existe esta letra na palavra')
                    print(f'Vidas: {lifes}')
                    if lifes == 0:
                        print(f'A palavra era {palavra}')
                        print('Você foi enforcado! :(')
                else:
                    position = [number for number in range(len(palavra)) if palavra[number] == letter]
                    for x in position:
                        word_hifens[x] = letter
                    if '-' not in word_hifens:
                        print(f'\nParabéns {self.nick}\nVocê adivinhou a palavra {palavra}\nVocê Sobreviveu XD !')
                        self.pontuacao += 100 * lifes
                        lifes = 0
                list_letters.append(letter)

    def salvar(self):
        with open('etc/usuarios.json', 'r') as file:
            geral = json.load(file)
            for idx, pessoa in enumerate(geral['usuarios']):
                if pessoa['nome'] == self.nick:
                    line, user = (idx, geral['usuarios'][idx])
                    user['pontos'] += self.pontuacao
                    geral['usuarios'][idx] = user
        with open('etc/usuarios.json', 'w') as file2:
            geral = json.dumps(geral, indent=4)
            file2.write(geral)

    def exe(self):
        print(f'Seja Bem Vindo(a) {self.nick} ao Jogo da Forca')
        user_choice = input('\nEscolha "jogar" ou "sair": ')
        while user_choice != 'sair':
            cat = input('Escolha uma categoria:\n- Animais\n- Alimentos\n- Geral\n').lower()
            if cat in self.categorias.keys():
                self.jogar(cat)
            else:
                print('Categoria não encontrada :(')
            user_choice = input('\nEscolha "jogar" ou "sair":')
        else:
            self.salvar()
