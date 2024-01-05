"""
103
Variabile
PF - 2020-04-13 v4
"""  #

# pylint: disable=invalid-name

# atribuirea valorii unei variabile
x = 5
print(x)

# atribuire de valoare mai multor variabile cu aceeasi instructiune
x, y, z, w = 'Ana', 'are', 'mere', '-*-'
print(x, y, z)
print(x + w + y + w + z)

# Inversarea valorilor a doua variabile prin metoda atribuirii multiple
a = "animal"
p = 'planta'
a, p = p, a
print(a)
print(p)

x = 100

x = x + 5  # atribuire de valoare printr-o expresie
print(x)

x += 5  # incrementare(augmentation)
print(x)

x -= 5  # decrementare
print(x)

x *= 7  # inmultire
print(x)

x /= 7  # impartire
print(x)

# se dau urmatoarele variabile
numele = 'Popa'
prenumele = 'Arabela'
data_nasterii = '1980-12-22'
locul_nasterii = 'Targoviste'
profesia = 'inginer'
salariul = 9999

from _datetime import datetime
datetime.strptime(data_nasterii, '%Y-%m-%d')

# putem completa un formular predefinit, utilizand aceste variabile:
print('Numele studentului: ' + numele + '\nPrenumele studentului: ' + prenumele +
      '\nNascut la data de: ' + data_nasterii + '\nIn localitatea: ' + locul_nasterii +
      '\nProfesia: ' + profesia + '\nSalariul net: ' + str(salariul))

# Concatenare

cifra1 = 4
cifra2 = '10.0'
nume = 'Bogdan '

print(nume + cifra1)
print(nume + str(cifra1))

print(cifra1 + cifra2)
print(cifra1 + float(cifra2))

input("Apasa <enter> pt a iesi.")
