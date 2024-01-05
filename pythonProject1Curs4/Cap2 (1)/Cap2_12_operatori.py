"""212 Operatori
Utilizarea operatorilor
PF - 08/05/2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=using-constant-test

# Operatori de comparare

if 'Am un cos plin' >= 'Am un cos gol':     # comparatia efectiva la primul caracter diferit
    print('E mai bine sa fie plin')
else:
    print('E mai bine sa fie gol')


if 'mere' == 'pere':
    print('Premiul Nobel')
else:
    print('Mai fa cercetari')


if '100' >= 100:          # genereaza o eroare, nu putem compara tipuri diferite
    print('Chiar asa?')


# Operatori Boolean

if 'Maria':                # nu ajunge niciodata pe ramura else
    print('Soare')
else:
    print('Nor')

# sau

if 'False':                   # nu intra pe if niciodata
    print('Soare')
else:
    print('Nor')

input('\n\nApasa <enter> pt a iesi.')

# bitwise operators.

# & (ampersand)       - AND
# | (bar)             - OR
# ^ (caret)           - XOR

print((7 < 5) & (5 > 3))
print((7 > 5) | (5 > 3))

print((7 < 5) | (5 > 3))

print((7 < 5) ^ (5 > 3))
print((7 > 5) ^ (5 > 3))

# shift

x = 101

print(x >> 1)  # echivalent    x // 2**1
print(x >> 2)  # echivalent    x // 2**2
print(x >> 3)  # echivalent    x // 2**3
print(x >> 4)  # echivalent    x // 2**4

print(x << 1)  # echivalent    x * 2**1
print(x << 2)  # echivalent    x * 2**2
print(x << 3)  # echivalent    x * 2**3
print(x << 4)  # echivalent    x * 2**4
