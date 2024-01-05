"""
405 Functii
Functie care poate sa returneze rezultate diferite in functie de numarul parametrilor
PF 20.08.2020 v4
"""  #

# pylint: disable=invalid-name


def numere(*parametrii):
    """Docstring!"""  #
    # returneaza numarul
    if len(parametrii) == 1:
        result = parametrii[0]
    # inmulteste doua numere
    elif len(parametrii) == 2:
        result = parametrii[0] * parametrii[1]
    # aduna multe numere
    elif len(parametrii) > 2:
        suma = 0
        for i in parametrii:
            suma += i
        result = suma
    else:
        result = False
    return result


print(numere(5, 7, 8))

print(numere(5))

print(numere(5, 10))

print(numere())
