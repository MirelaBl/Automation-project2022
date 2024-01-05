"""
408 Lucrul cu fisiere
Citire si scriere, extragere de informatii
PF - 22.05.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=wrong-import-position

# Deschiderea  fisierului. Citirea intregului text, toate liniile

text = open("guta.txt", "r", encoding='utf-8', newline='\n')
x = text.read()  # citeste toate liniile intr-un sir de caractere
print(x)
text.close()

# Citeste doar caracterele dintr-o linie (readline)

text.seek(0)  # muta cursorul la inceputul fisierului (indexul 0)

print(text.readline())  # Prima linie
print(text.readline())  # A doua linie
print(text.readline())  # A treia linie

help(text)

# Citeste toate liniile si le adauga intr-o lista ( o linie un element )
text.seek(0)

linii = text.readlines()
print(linii)

# Bucla cu liniile unui text (Folosim lista de mai sus)

for linie in linii:
    linie = linie.rstrip()      # elimina liniile goale  ?!?!
    print(linie)
text.close()

text.seek(0)

count = 0
for linie in text.readlines():
    linie = linie.rstrip()      # elimina spatiile goale  ?!?!
    count += 1
    if 'vorba' in linie:
        print('Numarul liniei:', count)
        print(linie)

text.seek(0)

for linie in text.readlines():
    if 'vorba' in linie:
        print("numarul liniei:", linii.index(linie) + 1)           # linia
        print("numar car pe linie", linie.find('vorba') + 1)              # caracterul
        print("numar cuvant pe linie", linie.split().index('vorba') + 1)       # cuvantul
        print(linie)


# Scrie intr-un fisier nou creat / sau il suprascrie
text = open("scrie.txt", "w")
data = '22.05.2021'
text.write(f'Python si MySQL se inteleg de minune\nIn curand vom incerca\n\n{data}\n \
sa lucram cu\nbaze de date MySQL!')  # afiseaza numarul de caractere scrise
nr_car = text.write('\n\nAstazi este o zi frumoasa. ')  # stocheaza numarul de caractere scrise
print(f'Am scris un numar de {nr_car} caractere')
sir = 'Ana are cirese'
text.write(sir)  # daca nu mutam cursurul explicit (\n) scrie in continuare


text = open("scrie.txt", "r")
print(text.read())
text.close()

text = open("scrie.txt", "a+")
new_line = ' Inca o zi frumoasa!'  # va fi scrisa in continuarea ultimei linii din fisier
text.writelines([new_line, '\n\nvasile danseaza'])
text.write('\n\t\a Astazi este o zi frumoasa!')
text.write("""\nLinia unu
linia2
linia3
""")

print(text.read())  # incercare nereusita de citire, cursorul e la final
text.seek(0)
print(text.read())  # dupa mutarea cursorului citirea e posibila
text.seek(0)
text.readlines()

text.tell()  # returneaza pozitia curenta a cursorului

text.close()

# Try / except - creaza un dictionar cu cuvintele din text si numarul de aparitii pentru fiecare

try:
    text = open('guta.txt')

except(FileNotFoundError) as e:
    print('Fisierul nu poate fi deschis:')
    print('Eroarea aparuta: ', e)
    text = None

else:
    counts = dict()
    for line in text.readlines():
        words = line.replace(',', '').replace('.', '').replace('?', '').replace('!', '').split()
        # text linii split in cuvinte
        for word in words:
            if word not in counts:  # daca nu exista in dictionar il creaza
                counts[word] = 1
            else:
                counts[word] += 1   # daca exista in dictionar aduna 1
    print(counts)

finally:
    if text is not None:
        text.close()        # de vazut
        del text

max(counts.values())

for k, v in counts.items():
    if v == 10:
        print(k)

for i in counts:
    if counts.get(i) == 10:
        print(i)
        break


#   Avem un fisier text care contine date despre medici. Extragem informatii si populam un dictionar
#   Format [{'Nume': 'Popa', 'Prenume': 'Ion', 'Specialitate': 'orl', 'Tip': 'primar'},...]

fisier = open('c:/_wt/medici1.txt', 'r', encoding='utf-8', newline='\r\n')
lista = []   # lista in care vom introduce dictionare cu seturi de valori pt fiecare medic
dict1 = {}   # dictionarul care va introduce fiecare set de valori in lista

for line in fisier:
    line = line.rstrip()            # elimina spatiile dintre liniile returnate
    ls = line.split(',')            # creaza o lista cu cuvintele de pe o linie
    if ls[0] != 'Nume':             # nu vrem sa returneze si antetul din fisier
        dict1['Nume'] = ls[0]
        dict1['Prenume'] = ls[1]     # din aceasta lista populam un dictionar "temporar"
        dict1['Tip'] = ls[2]
        dict1['Specialitate'] = ls[3]
        lista.append(dict1)           # datele din dictionarul temporar sunt incarcate in lista
        dict1 = {}  # dictionarul este reinitializat pentru urmatoarea iteratie (linie)

print(lista)

# alternativ
for line in fisier:
    line = line.rstrip()            # elimina spatiile dintre liniile returnate
    ls = line.split(',')            # creaza o lista cu cuvintele de pe o linie
    if ls[0] != 'Nume':             # nu vrem sa returneze si antetul din fisier
        for i, n in enumerate(['Nume', 'Prenume', 'Tip', 'Specialitate']):
            dict1[n] = ls[i]
        lista.append(dict1)  # datele din dictionarul temporar sunt incarcate in lista
        dict1 = {}

lista_antet = []
lista2 = []

# sau cu zip
for line in fisier:
    line = line.rstrip()            # elimina spatiile dintre liniile returnate
    ls = line.split(',')            # creaza o lista cu cuvintele de pe o linie
    if ls[0] == 'Nume':             # nu vrem sa returneze si antetul din fisier
        lista_antet.extend([ls[0], ls[1], ls[2], ls[3]])
    else:
        lista2.append(dict(zip(lista_antet, ls)))


for i in lista:
    if i['Specialitate'] == 'pediatrie':
        print(i['Nume'], i['Prenume'], '-', i['Specialitate'])
        print('-' * 45)

# Avem o lista, care contine pentru fiecare medic un dictionar cu nume, prenume, tip si specialitate
# Putem extrage doar o parte din informatiile despre medici si sa le listam individual

medici = ['Nume', 'Prenume', 'Specialitate']  # stabilim ce informatii extragem din elem. listei
for item in lista:
    for key in medici:
        print(key.ljust(20), ': ', item[key])             # extragem informatia dorita
    print('Fullname'.ljust(20), ': ', item['Nume'] + ' ' + item['Prenume'] + '\n')
    print('-' * 40)

# Putem extrage doar informatiile care ne intereseza (ex: medici cu specialitatea cardiologie)

import time

def med_spec(Spec):
    """Afiseaza medicii cu specialitatea dorita""" #
    #global fisier1
    t1 = open('scrie_1.txt', 'w')
    t1.write('\n' + '-' * 20 + str(time.asctime(time.localtime())))
    for item in lista:
        if item['Specialitate'] == Spec:
            print(item)
            for key in medici:
                t1.write('\n' + str(key) + ' : ' + str(item[key]))  # extragem informatia dorita
            print('-' * 25)

med_spec('o.r.l.')
med_spec('chirurgie')

fisier2 = open('scrie_1.txt', 'r')
fisier2.seek(0)
print(fisier2.read())

fisier2.close()


input('Apasa <enter> pentru a iesi.')


from prettytable import PrettyTable

listeaza = PrettyTable()
listeaza.field_names = ['nume', 'prenume', 'tip', 'spec']

for i in lista:
    listeaza.add_row([i['Nume'], i['Prenume'], i['Tip'], i['Specialitate']])
    if i != lista[len(lista)-1]:
        listeaza.add_row(['-'*17, '-'*20, '-'*12, '-'*16])

print(listeaza)
