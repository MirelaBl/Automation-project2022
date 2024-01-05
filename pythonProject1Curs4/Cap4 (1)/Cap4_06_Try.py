"""
406 Try - except
Exemple
PF 22.05.2021 v5
"""  #

# pylint: disable=invalid-name

import sys

# sintaxa
try:
    print('Try:', 5 // 1)

except ZeroDivisionError as e:
    print("Exception: 'N-ai reusit \nConsecinta: else NU va rula'\n", type(e), e)

else:
    print('\nElse: Daca vezi asta inseamna ca: Ai reusit! \nConsecinta: ELSE a rulat')

finally:
    print('\nFinally: Ruleaza orice-ar fi:  Ai reusit - continua'
          '!\nN-ai reusit o luam de la capat!')


# try in try
try:
    a = float(input())
    b = float(input())
    x = a + b
    print('a + b: ', a + b)
    f = open('guta1.txt')
    try:
        c = int(input())
        y = x * c
        print(y)

    except ValueError  as valerr:
        print('valerr', valerr)
except ValueError  as valerr1:
    print('valerr1', valerr1)
except (FileNotFoundError, FloatingPointError) as fnf:
    print('fnf', fnf)


# exemplu explicat
dict_data_ang = {}  # dict cu data angajarii
dict_varsta = {}  # dict cu varsta
dict_comun = {}

def salariat(nume, varsta, an_ang):
    """Populeaza doua dictionare cu datele angajatilor, nume-varsta, nume-anul angajarii"""
    try:
        if type(nume) is str:  # daca nume nu e string --> except. Daca e strig cu numere--> else
            if 18 <= varsta <= 100:  # varsta in afara intervalului --> mesaj
                if an_ang in range(1950, 2021):  # daca anul ang nu e in interval --> mesaj
                    dict_data_ang[nume] = an_ang
                    dict_varsta[nume] = varsta
                    dict_comun[nume] = [an_ang, varsta]
                else:
                    print('Anul angajarii incorect!')
            else:
                print('Varsta incorecta! tre sa fie intre 18 si 100')
        else:
            print('Nume incorect!')
    except (TypeError, ZeroDivisionError) as e:
        print('Eroare: %s' % e)
        print('cod eroare', sys.exc_info()[0])            # pentru captarea tipului de eroare
        print('mesaj eroare', sys.exc_info()[1])
    except IOError as e:
        print('Eroare: %s' % e)
        print('cod eroare', sys.exc_info()[0])            # pentru captarea tipului de eroare
        print('mesaj eroare', sys.exc_info()[1])
    except (NameError) as e:
        print('Eroare: %s' % e)
        print('cod eroare', sys.exc_info()[0])            # pentru captarea tipului de eroare
        print('mesaj eroare', sys.exc_info()[1])

salariat('Paul', 25, 2001)  # corect
salariat('George', 21, 2011)  # corect
salariat('22', 2011, 19)  # parametri inversati, nume incorect
salariat(22, 'Marin', 2011)  # nume incorect
salariat('Marin', 'kjashd', 22)  # parametri inversati, varsta incorecta
salariat('Alina', 23, 'klkd')
salariat(varsta=29, an_ang=2020, nume='Corina')

print(dict_data_ang)
print(dict_varsta)
print(dict_comun)

# parametrii cu valori standard

personal = dict()

def angajat(nume='Georgel', anul_ang=2021):
    """Completeaza datele angajatilor in 'personal' """
    personal[nume] = anul_ang

angajat('Mitica', 2001)
angajat('Corina')
angajat()
print(personal)
angajat(2005)  # numele va fi considera ca fiind 2005, anul default 2019
angajat(nume='Micsunica', anul_ang=2009)
angajat(anul_ang=2011)  # Numele va fi default 'Nume'
angajat(nume='Ion')  # anul va fi cel default 2020
angajat(anul_ang=2002, nume='Constanta')  # nu conteaza ordinea, daca atribuim valori tururor p v s
print(personal)
