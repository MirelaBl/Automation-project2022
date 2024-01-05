""" 210 IF
Utilizarea if - alte exemple
PF - 20.07.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=unneeded-not

# Conditii multiple separate:

x = 10

if x == 10:
    print('Adevarat')

if x < 100:
    print('Adevarat')

# Conditii multiple if in if:

if x == 10:
    print('Adevarat')
    if x < 100:
        print(x ** x)
    print('Altceva')

# Conditii multiple simultane (and):

y = 20

if x >= 0 and y >= 0:
    print('x / y = : ', x / y)
    print('x * y = : ', x * y)

# Conditii multiple simultane (or):

if x >= 10 or y < 20:
    print(x - y)
    print(x + y)

# Operatorul ( not ) negarea conditiei ( inversarea valorii de adevar):

if not x > 10:
    print(' x este egal cu: ', x)

# Operatorul (is) compara doua stringuri (egalitate si spatiu de memorie ocupat):

x = 'ana danseaza'
y = 'ana danseaza'
z = x

print(x == y)
print(x is y)
print(x is z)
print(id(x))
print(id(y))
print(id(z))

x = 10
z = x
y = 10

if x is z:
    print('x is z')  # cu is egalitatea se refera si la aceeasi
    # zona de memorie ocupata p la 256 la numere

print(x is z)
id(x)
id(z)
id(y)

# Operatorul (in) teseteaza existenta, incluziunea:

sir = 'Astazi invatam despre if'

if 'invatam' in sir:
    print('Indexul este: ', sir.find('invatam'))

# ternary operator

nor = None # True

print('Soare' if nor is None else 'Nor')

# valoare_pt_adevarat if conditie else valoarepentru_false'


input('Apasa <enter> pt a iesi')
