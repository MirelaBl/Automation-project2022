"""213 While
Utilizarea buclei while
PF - 08/05/2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=no-else-break

# Exemplu while
x = 100

while x > 0:
    print(x, end=', ')
    #print('ana are', x, 'mere')
    x -= 15     # decrementam valoarea lui x, ca sa asiguram iesirea din bucla.
                # Daca omitem aceasta instructiune bucla devine infinita

# Conversie repetata lei in lire sterline (apelare succesiva pana la conditia de iesire din bucla).

curs = float(input('Introduceti cursul lei/GBP: '))

while True:
    lei = input('Introduceti suma sau ENTER pentru a iesi: ')

    if lei == '':
        print('Va multumim!')
        break
    elif lei.isdigit():
        lei = int(lei)
        print('Schimb efectuat. Ridicati suma de %.2f' % (lei / curs), 'GBP')
    else:
        print('Introduceti suma in format numar intreg!')
