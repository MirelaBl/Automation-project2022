"""
306 Lista
Lista de cumparaturi
PF - 20.06.2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=unidiomatic-typecheck

lista = []								# Initializam lista

print('\t\t Bine ati venit la programul lista de cumparaturi')

while True:
    print("""Introduceti:
        0 - Pentru afisare lista actuala
        1 - Pentru introducerea unui element nou
        2 - Pentru stergerea unui element existent
        3 - Pentru stergerea intregii liste
        9 - Pentru iesire
        """)
    print('#' * 30)
    alegere = input('Introduceti optiunea - dintre cele enumerate:\n\t')
    print('#' * 30)

    if alegere == '0':
        if lista:  						# Daca lista nu e goala...
            lista1 = lista.copy()
            lista1.sort()
            print('Lista de cumparaturi este :\n')
            print('-' * 30)             # linie decorativa
            for elem in lista1:
                print('==>', elem)
            print('-' * 30)             # linie decorativa
        else:
            print('Lista este goala\n')
            print('#' * 30)             # linie decorativa

    elif alegere == '1':
        while True:
            el_nou = input('Introduceti noul elem (ENTER - daca doriti sa iesiti):\n\t').lower()
            if el_nou == '':
                break
            lista.append(el_nou)
            print('#' * 30)

    elif alegere == '2':
        if lista:
            sterge = input('Ce element doresti sa stergi? \n').lower()
            if sterge in lista:
                lista.remove(sterge)
                print('Elementul ', sterge, 'a fost sters\n')
                print('#' * 30)
            else:
                print(sterge, 'nu a fost gasit in lista\n')
                print('#' * 30)
        else:
            print('Lista este goala\n')
            print('#' * 30)

    elif alegere == '3':
        lista.clear()
        print('Lista a fost stearsa\n')
        print('#' * 30)

    elif alegere == '9':
        print('Va multumim ca ati ales acest program!\n')
        break

input('Apasa <enter> pt a iesi.')
