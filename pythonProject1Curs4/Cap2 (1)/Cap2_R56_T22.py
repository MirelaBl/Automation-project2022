"""
256 Tema 22
for
PF - 08/05/2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement


"""
Scrieti un program care va numara cate caractere are un sir dat de utilizator
Aceata numarare sa se realizeze cu ajutorul unui for. La final afisati rezultatul
Similar sa numere cate cuvinte sunt in text
""" #

sir = input('Introduceti textul: ')

count_car = 0
count_cuv = 0

for car in sir:
    count_car += 1
print('Textul tau are', count_car, 'caractere.')

for cuv in sir.split():
    count_cuv += 1
print('Textul tau are', count_cuv, 'cuvinte.')

input('\n\nApasa <enter> pt a iesi.')
