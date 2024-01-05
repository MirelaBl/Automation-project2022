"""
708 Module
Modulul collections
PF - 15.06.2021 v6
"""  #


from collections import ChainMap
from collections import namedtuple
from collections import Counter


# ChainMap
dict1 = {1: 'Ana', 2: 'Ema'}
dict2 = {3: 'Cris', 4: 'Ben'}
dict3 = {5: 'Vio', 6: 'Lia'}

colectie = ChainMap(dict1, dict2)  # creaza o colectie de dictionare

print(colectie)
print(list(colectie.keys()))
print(list(colectie.values()))
print(list(colectie.maps))

colectie.new_child(dict3)  # afiseaza colectia plus dictionarul nou inaintea celorlate. Nu modifica colectia


# namedtuple
# definim un model numetuple
Persoana = namedtuple('Persoana', ['nume', 'prenume', 'sex'])

# definim un obiect persoana
persoana1 = Persoana('Popa', 'Victor', 'm')

print(persoana1.nume)
print(persoana1.prenume)
print(persoana1[2])


# Counter
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 7, 7, 7]
dictionar = {"rosii": 5, "castraveti": 3, "piersici": 7}

print(Counter(lista))
print(Counter(dictionar))
print(Counter(ceva=10, altceva=5))
