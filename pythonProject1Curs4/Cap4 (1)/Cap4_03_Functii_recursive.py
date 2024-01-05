"""
403 Functie recursiva - recapitulare
Functii
PF - 22.05.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=wrong-import-position
# pylint: disable=unused-variable

# aduna recursiv
def adunaRecursiv(numar_minim, numar_maxim):
    """Aduna numerele cuprinse intre minim si maxim"""

    if numar_minim > numar_maxim:
        result = 0
    else:
        result = numar_minim + adunaRecursiv(numar_minim + 1, numar_maxim)
    return result

adunaRecursiv(8, 1500)


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
print(fib(35))
time_end = time()
print(time_end - time_start)

# sau, fara recursivitate
def fibo(numar):
    """
    Alta varianta mai rapida...
    """  #
    a, b = 0, 1
    for i in range(numar):
        a, b = b, a + b
    return a

print(fibo(1000))
len(str(fibo(1000)))
