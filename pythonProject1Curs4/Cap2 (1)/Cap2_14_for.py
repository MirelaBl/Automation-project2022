"""214 For
Utilizarea buclei for
PF - 08/05/2020 v4
"""  #

# pylint: disable=invalid-name

# Tipareste caracterele unui sir si le numara
sir = 'Ana nu mai are mere, are un cos cu cirese'
print('Sirul tau este: ', sir)

caracter = 12
print(caracter)

count = 0
for caracter in sir:
    print(caracter.upper())
    count += 1


print('\nSirul ales are: ', count, 'caractere!')

print(caracter)

len(sir)

# Numara apartiile unui caracter ... pana la un moment indicat
sir = 'Teleenciclopedia'
count = 0
len1 = -1
for i in sir:
    len1 += 1
    if i == 'e':
        count += 1				# numara apartitiile caracterului dat
    if count == 3:
        print('Indexul este: ', len1)  # daca, count ajunge la 3 returneaza
        break  # indexul caracterului si iese din bucla

print(count)

# Numara cuvintele dintr-un sir

sir1 = 'Ana nu mai are mere, are un cos; cu cirese!'
count = 0
var = sir1.replace(',', '').replace(';', '').replace('!', '').split()

for i in var:      # split transforma sirul intr-o lista de cuvinte
    count += 1
    print(i, end=', ')
print('\nAm gasit', count, 'cuvinte')

for i, j in enumerate(var, start=5):
    print("\nCuvant: ", j, "\nNumar:", i)

sir = 'mere,pere,alune,cirese,capsuni,gutui,castane'

for i, j in enumerate(sir.split(',')):
    print('Cineva are {0} {1}'.format(i, j))


input('\n\nApasa <enter> pt a iesi.')
