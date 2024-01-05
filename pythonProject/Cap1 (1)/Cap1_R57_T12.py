"""
R157
tema 2 - Input / conversie string - float
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


cant = float(input("Introduceti cantitatea: "))
pret = float(input("Introduceti pretul: "))

val = cant * pret
print("Valoarea comenzii este: ", val)
