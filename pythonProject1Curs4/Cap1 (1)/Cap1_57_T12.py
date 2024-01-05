"""
157
Tema 12
PF - 2020-04-13 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=trailing-whitespace
# pylint: disable=pointless-string-statement

'''
Creati un program care sa calculeze valoarea unei comenzi, pornind de la cant si pret,
doua variabile capturate de utilizator prin input, reprezentand:
 cant - cantitatea , 
 pret - pretul
Calculul se va face intr-o noua variabila, val. Afisati rezultatul''' #

cant = input('Introduceti cantitatea: ')
pret = input('Introduceti pretul: ')
valoare = float(cant) * float(pret)
print(valoare)
