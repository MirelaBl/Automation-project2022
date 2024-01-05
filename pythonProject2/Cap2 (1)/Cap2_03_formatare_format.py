""" 203 Formatare
 Metoda format
 PF - 20.07.2021 v5
"""  #

# pylint: disable=invalid-name

# nu conteaza ordinea placeholderelor
print("Textul tau este: {2}, {1}, {0}, {2}".format("x", "y", "z"))
# pozitiile                                         0    1    2


# putem utiliza variabile
x, y, z = 10, 20, 30
print("Utilizeaza variabilele anterioare: {2}, {2}, {0}, {1}, {0}".format(z, y, x))


# putem utiliza *string, stringul va fi transformat in caractere
print("{3},{1},{0}".format(*"gxyz"))  # face split la sir, echivalent cu
print("{3},{1},{0}".format("g", "x", "y", "z"))


# formatarea stringurilor, argumente cu identificatori (nume de variabile locale):
print("Produsul: {prod}, \ncantitate: {cant}, \npret: {pret}".format(cant=100 * 2, pret=5, prod="cirese"))


# formatarea stringurilor alinierea textului:
print("{0:*<15}".format("stanga"))  # completeaza spatii pana la 20 de caractere si aliniaza stanga
print("{:->20}".format("dreapta"))  # idem dreapta 20 de caractere
print("{:&^19}".format("centrat"))  # idem centrat 19 caractere
print("Textul este {:*^19}".format("centrat"))  # centrarea si inlocuirea completarea cu caracterul *


# formatarea stringurilor - float cu nr de zecimale implicit sau setat de utilizator
print("{: f}".format(17/29))  # nr de zecimale implicit
print("{:.2f}".format(8.555))  # “ .2 “ face ca numarul de zecimale returnat sa fie 2

# formatarea stringurilor - baze de numeratie
print("int: {0:d};  hex: {1:X};  oct: {2:o};  bin: {3:b}".format(99, 255, 8, 255))
# sau cu reprezentarea specifica
print("int: {0:d};  hex: {1:#x};  oct: {2:#o};  bin: {3:#b}".format(100, 255, 63, 4))


# formatarea stringurilor cu separator grupe de cifre:
print("{: ,}".format(35735735735))  # primeste ca parametru un numar, returneaza un sir de caractere


# formatarea stringurilor, procente:
raspunsuri_corecte = 17
intrebari_total = 21
print("Nota : {:.2%}".format(raspunsuri_corecte / intrebari_total))

# formatarea stringurilor, completarea cu zpatii sau zerouri:
print("{:5d}".format(15))  # completarea cu spatii, in stanga, pana la lungimea de 5 caractere
print("{:05d}".format(15))  # completarea cu zerouri, in stanga, pana la lungimea de 5 caractere

input("Apasa <enter> pt a iesi.")
