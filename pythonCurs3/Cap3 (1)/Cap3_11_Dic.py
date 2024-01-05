"""
311 Dictionare
Lucrul cu liste si dictionare
PF - 18.07.2020 v4
"""  #

# pylint: disable=invalid-name

# schimbare chei/valori
pasari = {'privighetoare': 5, 'pitigoi': 3, 'pitulice': 7, 'cioara': 5}
dict_invers = {x: y for y, x in pasari.items()}
print(dict_invers)


# - # - #   SORTARE DICTIONAR
dictionar = {'Radu': 18, 'Corina': 12, 'Matei': 22, 'Elvira': 25, 'Bianca': 27}

# sortare key
lista = sorted(dictionar.keys())

for element in lista:
    print("->  ".join((element.ljust(10), str(dictionar[element]))))

# sortare items
lista1 = sorted(dictionar.items())

for i, j in lista1:
    print("->  ".join((i.ljust(10), str(j))))