"""
301 Indexarea sirurilor
Indexare
PF - 21.06.2020 v4
"""  #

# pylint: disable=consider-using-enumerate
# pylint: disable=invalid-name

# Concatenare + indexare
sir = 'Tele' + 'cinemateca'             # concatenare stringuri
print(sir)
lit = sir[2+2]
print(lit)
x = 7
y = sir[x + 3]                          # index calculat cu o expresie
print(y)

# Bucla while intr-un sir - returneaza index - litera
index = 0                               # initializare variabila
while index < len(sir):
    litera = sir[index]                    # parsare
    print(index, '-', litera)
    index += 1                          # incrementare

# Bucla for intr-un sir - returneaza index - litera
index = 0
for i in sir:
    print(index, '-', i)
    index += 1

for i in range(len(sir)):
    print(i, '-', sir[i])

# acelasi lucru si cu:

for i, j in enumerate(sir):
    print(i, j)

# Numararea aparitiilor unei litere
count = 0
for i in sir:
    if i == 'e':
        count += 1
print(count)


# Numara vocalele si alte tipuri de caractere
vocale = 0
consoane = 0
spatii = 0
alte_caractere = 0

abc = 'ana   are   mere  ;?'

for i in abc:
    if i.lower() in ('a', 'e', 'i', 'o', 'u'):
        vocale += 1
    elif i.isalpha():
        consoane += 1
    elif i.isspace():
        spatii += 1
    else:
        alte_caractere += 1

print('Vocale:'.ljust(19), vocale, '\nConsoane:'.ljust(20), consoane,
      '\nSpatii:'.ljust(20), spatii, '\nAlte caractere'.ljust(20), alte_caractere)

# Slicing
print(sir[0:4])  # incepe de la primul caracter, termina la al doilea argument fara sa-l includa

print(sir[-14:-10])

print(sir[4:8])  # incepe cu primul argument, termina la al doilea fara sa-l includa

print(sir[4:20])  # al doilea numar e mai mare decat len(string) se opreste la sfarsit

print(sir[:4])  # returneaza primele caractere fara sa includa argumentul final

print(sir[12:])  # returneaza toate caracterele incepand cu argumentul dinaintea ':'

print(sir[:])  # returneaza tot stringul

copy_sir = sir[:]  # facem o copie a stringului intr-o alta variabila

print(copy_sir)

print(sir is copy_sir)

# Inversam ordinea literelor intr-un sir
sir = input('Introduceti un sir: ')

print('Sirul tau este', sir)
sir_invers = ''
for var in sir:
    sir_invers = var + sir_invers
print(sir_invers)

# Acelasi lucru cu slicing:

print(sir[-1: -(len(sir) + 1): -1])
print(sir[:: - 1])

print('Sirul tau se scrie invers: ', sir_invers)

input('Apasa <enter> pt a iesi.')
