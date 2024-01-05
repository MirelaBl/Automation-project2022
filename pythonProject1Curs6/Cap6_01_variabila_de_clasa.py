"""
601 OOP VS
Variabila de clasa
PF - 08.06.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods


class Clasa:
    """Aceasta clasa are variabile de clasa"""

    nr_magic = 7
    nr_instante = 0  # variabila de clasa (statica). Numara instantele create

    def __init__(self):
        Clasa.nr_instante += 1  # apelare! nume_clasa.variabila

obj1 = Clasa()

print(obj1.__dict__)
print('____________')

# apelarea variabilei se poate face prin nume clasa sau nume instanta
print(Clasa.nr_magic)
print('**************')

print(Clasa.nr_instante)
print('::::::::::::::::')

print(obj1.nr_magic)
print(obj1.nr_instante)

# modificare atribut de clasa
Clasa.nr_magic = 6

obj2 = Clasa()

print(obj2.nr_instante)
print(obj1.nr_instante)
print(Clasa.nr_instante)
print(obj1.nr_magic)
print(obj2.nr_magic)

print(obj2.__dict__)

input("Apasa ENTER pentru a iesi: ")
