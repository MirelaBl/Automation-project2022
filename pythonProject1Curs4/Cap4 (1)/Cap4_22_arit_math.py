"""
422
Op aritm / math in Python - Creaza functii care sa faca ...
PF 02.09.2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=unused-import

from math import sqrt, pi, sin, cos     # importa functiile mentionate din modulul math

enunt = '''
1.-----------------------------------------------------------------------------------
Teorema lui Pitagora. Calculeaza lungimea ipotenuzei intr-un triunghi dreptunghic
 - primeste dimensiunile catetelor
 - reeturneaza radacina patrata a sumei patratelor catetelor

2.-----------------------------------------------------------------------------------
Scrieti o functie ce primeste ca argument raza sferei. Va returna:
 - diametrul: D = 2r
 - circumferinta: C = 2πr
 - aria: A = 4πr²
 - volumul sferei: V = 4/3πr³ .
Fiecare din cele 4 informatii va fi printata pe cate un rand, cu 2 zecimale.
Apelati functia.

3.-----------------------------------------------------------------------------------
Cumparaturi online, costul de transport total are doua componente:
 - cost fix 5 lei
 - cost variabil 0.02 lei la fiecare 10 lei cost produs
Apelati functia

4.-----------------------------------------------------------------------------------
Pe un plan avem doua puncte a(x1, y1) si b(x2, y2). Scrieti un program care sa calculeze panta
intre a si b. Panta este (y2-y1) / (x2-x1)

5.-----------------------------------------------------------------------------------
Calculati distanta intre doua puncte in plan (radical din (x2-x1)² + (y2-y1)²)

6.-----------------------------------------------------------------------------------
Calculeaza suma a n numere, n introdus de utilizator

7.-----------------------------------------------------------------------------------
Calculeaza suma cuburilor a n numere, n introdus de utilizator

8.-----------------------------------------------------------------------------------
Creati un program care sa listeze puterile lui doi de la 1 la n

9.-----------------------------------------------------------------------------------
Leibniz a calculat valoarea lui π astfel:
π = 4( 1 – 1/3 + 1/5 – 1/7 + … )
Cu cat numarul de iteratii este mai mare, cu atat precizia este mai mare.
Scrieti un program, cu o functie, care sa primeasca numarul de iteratii si sa
returneze valoarea lui π.
''' #

input('Apasa <enter> pentru a iesi.')