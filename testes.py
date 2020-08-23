'''
with open('recursos_maquina.txt', 'r+') as file:
    recursos = list(map(int, file.readlines()[0].split(', ')))
    print(recursos)

recursos_names = ['agua', 'leite', 'cafe', 'copos', 'dinheiro']
dictin = {}
for i, v in enumerate(recursos_names):
    dictin[v] = recursos[i]

print(dictin)

-----------
with open('txt/iventario.txt', 'r+') as file:
    recursos = list(map(int, file.readlines()[0].split(', ')))


def comparar(user_qtdd, fill_qtdd):
    return True if user_qtdd >= fill_qtdd else False

print(comparar(40, 30))

____________
400, 540, 120, 9, 0
EVL, 100, 100, 100, 10
------------
'''
user_name = 'EVL'
with open('txt/iventario.txt', 'r+') as file:
    all_lines = file.readlines()

    print(type(all_lines))
    print(type(all_lines[0]))