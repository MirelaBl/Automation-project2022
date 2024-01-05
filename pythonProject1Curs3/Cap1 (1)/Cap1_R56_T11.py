"""
R156
Tema 1 - print / secvente de evadare
PF - 2020-04-13 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=trailing-whitespace
# pylint: disable=pointless-string-statement
# pylint: disable=bad-continuation

"""
Creati un program care sa afiseze urmatoarele asa cum sunt vizualizate:

        Glossa - de Mihai Eminescu

Vreme trece, vreme vine, 
Toate-s vechi si noua toate; 
Ce e rau si ce e bine 
Tu te-ntreaba si socoate; 
Nu spera si nu ai teama, 
Ce e val ca valul trece; 
De te-ndeamna, de te cheama, 
Tu ramâi la toate rece. 

a.	Titlul sa fie indentat cu doua tab-uri si sa sune un beep la rulare, utilizand secvente 
    de evadare;
b.	Primele doua randuri sa fie printate utilizand ghilimelele triple (ghilimele);
c.	Al treilea rand sa fie printat folosind virgula intre cuvinte;
d.	Al patrulea rand sa fie printat ca o suma de siruri de caractere 
	fiecare cuvand devenind propriul sir de caractere;
e.	Randul 5 si randul 6 sa fie printate utilizand ghilimelele simple si secvente de evadare;
f.	Randul 7 sa fie printat ca o concatenare a doua siruri de caractere.
g.	Ultimul rand sa fie afisat printat utilizand ghilimelele triple(apostrof).
""" #

print("\t\t\aGlossa - de Mihai Eminescu\a\n")

print("""Vreme trece, vreme vine, 
Toate-s vechi si noua toate;""")

print("Ce",
		"e",
  		"rau",
  		"si",
  		"ce",
  		"e",
  		"bine")

print('Tu' + ' te-ntreaba ' + 'si' + ' socoate;')

print('Nu spera si nu ai teama, \nCe e val ca valul trece;')

print("De te-ndeamna, " + "de te cheama,")

# g. Ultimul rand sa fie afisat cu printat utilizand ghilimelele triple
print('''Tu ramâi la toate rece.''')

input("\n\nApasa <enter> pt a iesi.")
