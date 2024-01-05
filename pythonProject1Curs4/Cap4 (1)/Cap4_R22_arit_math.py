"""
422
Op aritm / math in Python - Creaza functii care sa faca ...
PF 02.09.2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=unused-import
# pylint: disable=pointless-string-statement
# pylint: disable=missing-function-docstring

from math import sqrt, pi  # importa functiile mentionate din modulul math

"""
1.-----------------------------------------------------------------------------------
Teorema lui Pitagora. Calculeaza lungimea ipotenuzei intr-un triunghi dreptunghic
 - primeste dimensiunile catetelor
 - reeturneaza radacina patrata a sumei patratelor catetelor
 """

def pitag(a, b):
    """Primeste ca argumente lungimea celor doua catete si returneaza lungimea ipotenuzei"""
    ipotenuza = sqrt(a ** 2 + b ** 2)
    print('Ipotenuza este: ' + str(ipotenuza))

pitag(3, 4)

"""
2.-----------------------------------------------------------------------------------
Scrieti o functie ce primeste ca argument raza sferei. Va returna:
 - diametrul: D = 2r
 - circumferinta: C = 2πr
 - aria: A = 4πr²
 - volumul sferei: V = 4/3πr³ .
Fiecare din cele 4 informatii va fi printata pe cate un rand, cu 2 zecimale.
Apelati functia.
"""

def sfera(raza):
    d = 2 * raza
    c = pi * (raza ** 2)
    s = 4 * pi * (raza ** 2)
    v = (4 / 3) * pi * (raza ** 3)
    return 'Diametrul: {0:.2f}\nCircumferinta: {1:.2f}\nAria: {2:.2f}\nVolumul: {3:.2f}'.\
        format(d, c, s, v)

sfera(5)

"""
3.-----------------------------------------------------------------------------------
Cumparaturi online, costul de transport total are doua componente:
 - cost fix 5 lei
 - cost variabil 0.02 lei la fiecare 10 lei cost produs
Apelati functia
"""

def shiping_cost(cos_cump):
    sc = cos_cump / 10.0 * .2 + 5
    return sc

print(shiping_cost(568))

"""
4.-----------------------------------------------------------------------------------
Pe un plan avem doua puncte a(x1, y1) si b(x2, y2). Scrieti un program care sa calculeze panta
intre a si b. Panta este (y2-y1) / (x2-x1)
"""

def panta(x1, y1, x2, y2):
    """Calculeaza panta intre doua puncte situate pe un plan"""
    return (y2 - y1) / (x2 - x1)

panta(1, 2, 5, 5)

"""
5.-----------------------------------------------------------------------------------
Calculati distanta intre doua puncte in plan (radical din (x2-x1)² + (y2-y1)²)
"""

def distp(x1, y1, x2, y2):
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

print(distp(1, 2, 5, 5))

"""
6.-----------------------------------------------------------------------------------
Calculeaza suma a n numere, n introdus de utilizator
"""

def suma_n(n):
    """Calculeaza suma a n numere"""
    aduna = 0
    for i in range(n + 1):
        aduna += i
    print(aduna)

suma_n(10)

"""
7.-----------------------------------------------------------------------------------
Calculeaza suma cuburilor a n numere, n introdus de utilizator
"""

def suma_cub(n):
    """Calculeaza suma cubului a n numere"""
    aduna = 0
    for i in range(n + 1):
        aduna = aduna + i ** 3
    print(aduna)

suma_cub(10)

"""
8.-----------------------------------------------------------------------------------
Creati un program care sa listeze puterile lui doi de la 1 la n
"""

def two_to_n(n):
    x = 1
    for i in range(n + 1):
        x = 2 ** i
        print(i, x)

two_to_n(32)

"""
9.-----------------------------------------------------------------------------------
Leibniz a calculat valoarea lui π astfel:
π = 4(1 – 1/3 + 1/5 – 1/7 + … )
Cu cat numarul de iteratii este mai mare, cu atat precizia este mai mare.
Scrieti un program, cu o functie, care sa primeasca numarul de iteratii si sa
returneze valoarea lui π.
"""

def calc_pin(n):
    suma = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            suma += 1 / (i * 2 - 1)
        else:
            suma -= 1 / (i * 2 - 1)
    return 4 * suma

input('Apasa <enter> pentru a iesi.')
