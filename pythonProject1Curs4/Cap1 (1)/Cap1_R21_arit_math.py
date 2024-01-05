"""
R121
Op aritm / math in Python
PF - 2020-04-13 v4
"""#

# pylint: disable=invalid-name

from math import pi  # importa functia pi din modulul math

#1 Printeaza expresia: (7 + 3)(2) -  atentie la operatori obligatorii !

print((7 + 3) * 2)

#2. Printeaza expresia n (n-1) / 2 . n va fi introdus de la tastatura cu input()

n = float(input('Introduceti un numar: '))
print(n * (n - 1) / 2)

#3. pi * r² - aria cercului. raza  va fi introdusa de la tastatura cu input()

raza = float(input('Introduceti raza cercului: '))

print('Aria cercului este: ' + str(pi * raza ** 2))
