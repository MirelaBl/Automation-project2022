"""
310 Dictionare
Lucrul cu liste si dictionare
PF - 18.07.2020 v4
"""  #

# pylint: disable=invalid-name

from prettytable import PrettyTable            # tabulate -  de testat

lista_filme = list()  # lista contine dictionare cu filme. Un film, un dictionar
film = dict()

#     populam dictionarul pentru film1
film['Director'] = 'Alejandro G. Inarritu'
film['Title'] = 'The Revenant'
film['Release year'] = '2015'
film['Running Time'] = '156 minutes'
film['Rating'] = 'AG-15'
print(film)

# populam lista cu datele din dictionar
lista_filme.append(film)
print(lista_filme[0])
print(lista_filme[0]['Director'])
len(lista_filme)

film = {}

# populam dictionarul pentru film2
film['Director'] = 'Radu Jude'
film['Title'] = 'Aferim!'
film['Release year'] = '2015'
film['Running Time'] = '108 min'
film['Rating'] = 'AG-12'

# populam lista cu datele din dictionar
lista_filme.append(film)

# listam datele
for item in lista_filme:
    print(item)


# selectie elem convenabile din lista prin keys
keys = ['Title', 'Director', 'Release year']

for item in lista_filme:
    print("*" * 45)
    for k in keys:
        print(k.ljust(20), '->', item[k])
print(45 * "*")

for i in lista_filme:
    print("*" * 45)
    for k, v in i.items():
        print(k.ljust(20), '-->', v)

dict_comun = {}

for i in lista_filme:
    for k, v in i.items():
        if dict_comun.get(k):
            dict_comun[k] += [v]
        else:
            dict_comun[k] = [v]

listeaza = PrettyTable()

listeaza.field_names = lista_filme[0].keys()
for i in lista_filme:
    listeaza.add_row(i.values())

print(listeaza)
