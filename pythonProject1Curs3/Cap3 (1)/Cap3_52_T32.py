"""
Cap 3 Tema 2
Introduce elem in lista, o sorteaza
Paul Fratila - 18.07.2020 v4
"""  #

# pylint: disable=pointless-string-statement

"""
 Creati un program cu o lista de cumparaturi utilizand dictionare in loc de liste.
 Programul va imita lista de cumparaturi prezentata in curs ca si facilitati (Ex. 306)
 (adaugare, stergere, afisare, iesire din program).
 Folositi chei numerice incepand de la 1
 Valoarea intrarii trebuie sa fie introdusa de utilizator de la tastatura din meniul adaugare.
 Afisarea dictionarului se va face de forma: key => Value
 """ #
d_1 = {}
print(d_1)
for k, v in enumerate(['oua', 'apa', 'lapte', 'sare'], start=1):
    print(k , v)
    d_1[k] = v
print(d_1)


print("*" * 45)
for k, v in d_1.items():
 print(k, '>', v)