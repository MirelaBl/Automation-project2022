# aduna recursiv
def adunaRecursiv(numar_minim, numar_maxim):
    """Aduna numerele cuprinse intre minim si maxim"""

    if numar_minim > numar_maxim:
        result = 0
    else:
        result = numar_minim + adunaRecursiv(numar_minim + 1, numar_maxim-1)
    return result

adunaRecursiv(8, 15)

# fibonacci recursiv
def fib(numar):
    """
    Lista lui Fibonacci - o functie care se apeleaza pe sine - recursiva
    """  #
    if numar == 0:
        result = 0
    elif numar == 1:
        result = 1
    else:
        result = fib(numar - 1) + fib(numar - 2)
    return result

from time import time

time_start = time()
print('fibonacci: ')
print(fib(10))

# 01 crearea unei functii cu numar variabil de parametri *args   si   **kwargs
def exemplu(*args):  				# *args - permite un numar variabil de parametri
    """Functia aduna mai multe numere primite ca argument.
	Returneaza suma si lista numerelor"""
    print(type(args))
    suma = 0
    lista = []
    for i in args:
        if type(i) == int:
            suma += i
            lista.append(i)
    if lista:
        result = 'Suma numerelor : ' + str(lista) + ' este ' + str(suma)
    else:
        result = 'Nu ai introdus numere'
    return result

exemplu(1, 2, 5, 6, 8)

aria_tri = lambda baza, inaltimea: baza * inaltimea * .5
print(aria_tri(10, 5))
