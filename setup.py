from setuptools import setup, find_packages

setup(
    name='ILoveCoffee',
    version='1.0.0',
    author='Eric de Lima',
    author_email='eric.vinlima@gmail.com',
    packages=find_packages(),
    description='Um simples conjunto de mini-jogos, e mini-projetos',
    long_description='Nele podemos jogar alguns clássicos como Jogo da Velha, '
                     + 'Pedra Papel Tesoura, Jogo da Forca entre outros jogos. '
                     + 'Também temos um Sistema de Ranking integrado, e o objetivo '
                     + 'principal é ganhar pontos jogando os jogos, para comprar '
                     + 'ingredientes e dinheiro para fazer cafés.',
    url='https://github.com/ericxlima/ILoveCoffee',
    project_urls={
        'Código fonte': 'https://github.com/ericxlima/ILoveCoffee',
        'Download': 'https://github.com/ericxlima/ILoveCoffee/archives/1.0.0.zip'
    },
    license='MIT',
    keywords='ILoveCoffee EricdeLima EuAmoCafé Coffee Café Game Jogo',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment',
        'Topic :: Terminals'
    ]
)
