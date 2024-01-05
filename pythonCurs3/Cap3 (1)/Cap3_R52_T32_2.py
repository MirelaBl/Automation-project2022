"""
 Creati un program cu o lista de cumparaturi utilizand dictionare in loc de liste.
 Programul va imita lista de cumparaturi prezentata in curs ca si facilitati (Ex. 3_06)
     (adaugare, stergere, afisare, iesire din program).
 Folositi chei numerice incepand de la 1
 Valoarea intrarii trebuie sa fie introdusa de utilizator de la tastatura din meniul adaugare.
 Afisarea dictionarului se va face de forma: key => Value
 """ #

# pylint: disable=invalid-name

dc = {}

while True:

    print('''
    1 elemente noi
    2 stergere
    3 listare
    9 iesire''')

    opt = int(input('Introduceti optiunea: '))

    if opt == 1:
        if dc.keys():
            cheie = max(dc.keys()) + 1
        else:
            cheie = 1

        val = input('Introduceti valoarea: ')

        dc[cheie] = val

    elif opt == 2:
        if dc.keys():
            sterge = input('Ce elem stergeti? ')
            l = []
            for k, v in dc. items():
                if v == dc.get(k):
                    if v == sterge:
                        l.append(k)

            for k in l:
                print('A fost sters elem cu cheia', k, 'si valoarea', dc[k])
                dc.pop(k)


        else:
            print('Dictionar gol')

    elif opt == 3:
        if dc.keys():
            for i, j in dc.items():
                print(i, '=->', j)
        else:
            print('Dictionar gol')

    elif opt == 9 or opt not in(1, 2, 3, 9):
        print('La revedere')
        break
