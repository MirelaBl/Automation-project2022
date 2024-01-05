"""
R352 Tema 2
Introduce elem in lista, o sorteaza
PF 11.08.2020 V4
"""  #

# pylint: disable=invalid-name

ENUNT = """
 Creati un program cu o lista de cumparaturi utilizand dictionare in loc de liste.                         
 Programul va imita lista de cumparaturi prezentata in curs ca si facilitati (Ex. 3_06)    
 (adaugare, stergere, afisae, iesire din program).                                        
 Folositi chei numerice incepand de la 1
 Valoarea intrarii trebuie sa fie introdusa de utilizator de la tastatura din meniul adaugare.                              
 Afisarea dictionarului se va face de forma: key => Value                                    
 """ #

dict_cump = {}

while True:
    print("""Introduceti:
a - Pentru adaugare elemente
l - Pentru afisare
s - Pentru stergerea unui element existent
x - Pentru stergerea dictionarului
q - Pentru iesire
""")
    optiune = input('Introduceti optiunea dorita: ')
    if optiune.lower() == 'a':  # adauga pana te plictisesti :)

        while True:

            if not dict_cump:    # daca dictionarul este gol
                cheie = 1
            else:
                cheie = max(dict_cump.keys()) + 1

            produs = input('Introduceti produsul sau xxx pentru a iesi: ')

            if produs == 'xxx':     # conditie de iesire din while
                break

            dict_cump[cheie] = produs   # adauga cheie-valoare in dictionar

    elif optiune.lower() == 'l':
        if dict_cump:
            for k in dict_cump:
                print(k, '==>', dict_cump[k])
        else:
            print('Dictionarul este gol')

    elif optiune.lower() == 's':
        if dict_cump:
            # sterge = int(input('Introduceti cheia elementului de sters: '))
            # if sterge in dict_cump.keys():
            #    dict_cump.pop(sterge)
            sterge = input('Introduceti elementul de sters: ')
            if sterge in dict_cump.values():
                for k, v in dict_cump.items():
                    if v == sterge:
                        dict_cump.pop(k)
                        break

            else:
                #print('Cheia aleasa inexistenta')
                print('Produsul {0} nu se afla in lista'.format(sterge))
        else:
            print('Dictionarul este gol')

    elif optiune.lower() == 'x':
        dict_cump = {}

    elif optiune.lower() == 'q':
        print('La revedere!')
        break

    else:
        print('Optiunea ta nu exista')

input('Apasa <enter> pentru a iesi.')
