from random import choice

categorias = {'animais': ['coelho', 'cavalo', 'coruja', 'gaivota', 'porco', 'galinha',
                          'macaco', 'baleia', 'golfinho', 'morcego', 'girafa', 'elefante',
                          'castor', 'calango', 'flamingo', 'guepardo', 'hamster', 'serpente'],
              'alimentos': ['pepino', 'graviola', 'espaguete', 'manteiga', 'feijoada', 'lasanha',
                            'palmito', 'ervilha', 'repolho', 'pamonha', 'caramelo', 'chiclete',
                            'gengibre', 'gelatina', 'lentilha', 'pimenta', 'sorvete'],
              'geral': ['paraquedas', 'lombada', 'ventilador', 'caminhonete', 'violino', 'despertador',
                        'camisola', 'banheira', 'choveiro', 'mochila', 'computador', 'fotografia',
                        'brinquedo', 'revolver', 'esquadro', 'monitor', 'pincel', 'vasilhame']
              }


class Jogo:

    def __init__(self):
        print('Seja Bem Vindo(a) ao Jogo da Forca')
        self.exe()

    def jogar(self, categoria):
        palavra = None
        for i, key in enumerate(categorias.keys()):
            if i == categoria:
                palavra = choice(categorias[key])
        word_hifens = ['-' * len(palavra)]
        lifes = 8
        list_letters = []
        while lifes > 0:
            print('\n'+''.join(word_hifens))
            letter = input('Insira uma letra:')
            # Possíveis erros
            if letter in list_letters:
                print('Você já digitou esta letra')
            elif len(letter) != 1:
                print('Você deve inserir uma única letra')
            elif not letter.islower() or not letter.isalpha():
                print('Você deve inserir uma letra minúscula')
            else:
                if letter not in palavra:
                    print('Não existe esta letra na palavra')
                    lifes -= 1
                    print(f'Vidas: {lifes}')
                else:
                    position = [number for number in range(len(palavra)) if palavra[number] == letter]
                    for x in position:
                        word_hifens[x] = letter
                    if '-' not in word_hifens:
                        print('\n{}\nVocê adivinhou a palavra\nVocê Sobreviveu XD !'.format(palavra))
                        lifes = 0
                list_letters.append(letter)
        else:
            print(f'A palavra era {palavra}')
            print('Você foi enforcado!')

    def exe(self):
        user_choice = input('\nEscolha "jogar" ou "sair":')
        while user_choice == 'jogar':
            categoria = int(
                input('Que categoria você vai querer jogar?\n"1"- Animais\n"2" - Alimentos\n"3" - Geral\n'))
            self.jogar(categoria)
            user_choice = input('\nEscolha "jogar" ou "sair":')


eric = Jogo()
