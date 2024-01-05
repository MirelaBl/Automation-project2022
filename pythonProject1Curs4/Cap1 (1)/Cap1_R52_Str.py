# R152 Stringuri
# Secvente de evadare
# PF - 2020-04-13 v4

# pylint: disable=invalid-name
# pylint: disable=trailing-whitespace
# pylint: disable=pointless-string-statement

"""
 Creati un program care sa foloseasaca secventele de evadare in spiritul cerintelor din enunt:
 Ti-a facut tema? (cu bip inainte si dupa text)
 Nu, nu am avut timp. (Identat cu un tab)
 Promit ca o fac pana joi. (Identat cu 2 tab-uri)
 Printati caracterul  '\'
 Printati urmatoarele trei linii asa cum apar: 
 Datele mele sunt:
     numar de telefon ... # fara date reale
 	 email ...
 Printati trei linii goale. 
 Am terminat!
""" #

print("\a Ti-a facut tema?\a")

print("\tNu, nu am avut timp.")

print("\t\tPromit ca o fac pana joi.")

print("Acum scriu caracterul '\\'")

print('Datele mele sunt:\n\tnumar de telefon: 012456789\n\temail: paul@infoacademy.net')

print("Printez trei linii goale.\n\n\n\nAm terminat!")

input("\n\nApasa <enter> pt a iesi.")
