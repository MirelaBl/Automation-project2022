""" 2901 Ecuatia de gradul doi
 if
 PF - 15/06/2020 v1
"""  #

# pylint: disable=invalid-name

from math import sqrt


# ecuatia are forma ax² + bx + c = 0
# discriminantul    Δ  = b² - 4ac
# daca Δ  > 0 ecuatia are doua radacini distincte (-b + sqrt(Δ)) / 2a   si (-b - sqrt(Δ)) / 2a
# daca Δ  = 0 are doua radacini identice -b / 2a
# altfel nu are radacini reale

def ec_gr2(a, b, c):
    """
    Introduceti coeficientii ecuatiei:
        a - pentru x²
        b - pentru x
        c - intregul
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
    elif discriminant == 0:
        x1 = -b / (2 * a)
        x2 = x1
    else:
        print('Ecuatia nu are radacini reale')
        x1 = None
        x2 = None
    return [x1, x2]


# Ex 1  -   x² - x - 20 -  solutie:  5 si -4
print(ec_gr2(1, -1, -20))

# Ex 2  -   x² - 2x +1 -  solutie:  1 si 1
print(ec_gr2(1, -2, 1))

# Ex 3  -   4x² - 4x +1 -  solutie:  1 si 1
print(ec_gr2(4, 4, 12))

input("Apasa <enter> pt a iesi.")
