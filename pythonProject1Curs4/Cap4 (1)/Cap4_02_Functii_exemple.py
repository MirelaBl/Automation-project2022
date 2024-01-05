"""
402 Functii
Functii utile
PF - 22.05.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=no-else-return
# pylint: disable=inconsistent-return-statements
# pylint: disable=wrong-import-position
# pylint: disable=unused-variable


# 	Aria triunghiului
def aria_tri(baza: float, inaltime: float) -> float:  # tip de date impus si return impus
    """
    :param baza:
    :param inaltime:
    :return:
    """
    return baza * inaltime * .5

aria_tri(5, 7)

# Calificative
def calificativ(score: float):    # tip de date impus
    """Calculeaza calificativul obtinut pe baza notei"""

    if score > 10.0 or score < 0.0:
        result = 'Bad score'
    elif score >= 9.0:
        result = 'A'
    elif score >= 8.0:
        result = 'B'
    elif score >= 7.0:
        result = 'C'
    elif score >= 6.0:
        result = 'D'
    else:
        result = 'F'
    return result

calificativ(5)

# Transforma celsius in fahrenheit si invers
def cel_fahr(temp, tip):
    """Transforma c->f sau f->c.
    Tip este c sau f corespunzator temp introduse"""
    if tip.upper() == 'C':
        result = temp * 9 / 5 + 32
    elif tip.upper() == 'F':
        result = 5 / 9 * (temp - 32)
    else:
        result = 'Parametrii incorecti'
    return result

cel_fahr(0, 'c')
cel_fahr(100, 'f')

def fahr_kelvin(fahr):
    """
    Transforma fahrenheit in kelvin
    """  #
    cel = cel_fahr(fahr, 'F')
    kel = cel  + 273.15
    return kel

fahr_kelvin(32)

# An bisect - calculam daca anul este bisect si verificam daca este intre 1-9999
def bisect(an):
    """Returneaza 1 daca e an bisect, 0 daca nu este"""  #
    if 1 <= an <= 9999:
        if an % 400 == 0:
            bis = 1
        elif an % 100 == 0:
            bis = 0
        elif an % 4 == 0:
            bis = 1
        else:
            bis = 0
        return bis
    else:
        print('In afara intevalului')

print(bisect.__doc__)           # returneaza docstringul functiei
bisect(2400)                    # apelam functia

# numarul maxim/minim
def maxmin():
    """Returneaza maximul si minimul pentru numerele introduse. Tasteaza done pentru a iesi"""
    largest = None
    smallest = None
    while True:
        numar = input("Enter a number (enter pentru a iesi): ")
        if numar == "":  # iese din bucla daca tastam ENTER
            break

        numar = int(numar)

        if largest is None:
            largest = numar
            if smallest is None:
                smallest = numar
        else:
            if numar < smallest:
                smallest = numar
            if numar > largest:
                largest = numar
    print("Maximum is", largest, '\nMinimum is', smallest)

maxmin()


input('Apasa <enter> pentru a iesi.')
