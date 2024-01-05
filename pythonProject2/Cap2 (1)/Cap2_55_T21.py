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
- Contine doar cifre     Daca sirul de caractere este format numai din cifre (isdigit)
- Contine doar litere        Daca sirul de caractere este format numai din litere (isalpha)
- Contine diferite caractere 	Daca sirul de caractere este format din diferite cractere
Puteti pune totul intr-o bucla while?
"""  #
print('introdu input')

while True:
        inp = input()

        if  inp.isdigit():
            print('is digit')
            break
        elif inp.isalpha():
            print('is alpha')
            break
        else :
            print('is alpha numeric')
            break

"""while True:
    lei = input('Introduceti suma sau ENTER pentru a iesi: ')

    if lei == '':
        print('Va multumim!')
        break
    elif lei.isdigit():
        lei = int(lei)
        print('Schimb efectuat. Ridicati suma de %.2f' % (lei / curs), 'GBP')
    else:
        print('Introduceti suma in format numar intreg!')
        """

