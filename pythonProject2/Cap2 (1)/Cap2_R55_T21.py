"""
255 Tema 21
if, while, metode pentru siruri de caractere
PF - 08/05/2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement
# pylint: disable=no-else-break


"""
 Creati un progam care sa verifice daca sirul introdus de un utilizator de la tastatura (input)
 contine cifre, litere sau alte combinatii de caractere:
 Utilizati if, elif, else. Trebuie sa afisati urmatoarele mesaje:
 	Contine doar cifre          Daca sirul de caractere este format numai din cifre (isdigit)
	Contine doar litere         Daca sirul de caractere este format numai din litere (isalpha)
	Contine diferite caractere 	Daca sirul de caractere este format din diferite cractere
Puteti pune totul intr-o bucla while?
""" #

x = 3

while x > 0:
    text = input('Introduceti textul: ')

    if text.isdigit():
        print('Contine doar cifre')
    elif text.isalpha():
        print('Contine doar litere')
    else:
        print('Contine diferite caractere')
    x -= 1
