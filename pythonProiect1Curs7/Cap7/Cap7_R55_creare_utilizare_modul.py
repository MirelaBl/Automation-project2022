"""
755 Module
Creare si utilizare modul
PF - 15.06.2021 v6
"""  #


import sys

sys.path.append('c:/nume_folder')

enunt = """
Pasul 1
-------
Creati un modul care sa contina o functie la alegere. Nu uitati sa adaugati instructiunea:

if __name__ == "__main__":
    pass

Pasul 2
-------
Creati un alt fisier python cu:

import sys
sys.path.append('calea unde de afla modulul, fara numele fisierului')

a) - Testati daca sistemul de operare este windows (sys.platform = 'win32')
b) - daca da, importati modulul creat anterior
	b1) - rulati functia creata in modul
c) - daca nu afisati un mesaj si iesiti din program cu sys.exit()
""" #

def aduna(*x):
    suma = 0
    flag = ''
    for i in x:
        try:
            suma += i
        except TypeError as e:
            flag = 'incorect - ' + e
    if flag != 'incorect':
        return suma
    else:
        print('Parametri trebuie sa fie numerici')
        print(flag)

if __name__ == '__main__':
    print('primul meu modul')
