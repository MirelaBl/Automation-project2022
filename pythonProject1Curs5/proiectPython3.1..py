'''
Se citesc mai multe randuri pe care se afla 3 informatii ex: George 5000 Contabilitate
1. pe baza lor se creze 3 dictionare d1 care va fi George Contabilitate; d2 George 5000 ; si un alt dictionar in care
cheia va departamenul si valoarea este suma celorlalte valori si un alt dictionare care are departament si numar angajati
2. sa se afiseze in ordine descatoare departmantele dupa salariul mediu
exemplu :   George 5000 Contabilitate
            Ion 3000 Paza
            Vasile 4000 Marketing
            Diana 4500 Management
            Monica 3500 Marketing
            Sorin 3100 Paza
            Corina 5300 Contabilitate
            Lavinia 4900 Management
pentru verificarea daca exista cheia x in dictionar se foloseste x in dictionar.keys()
'''

dict1 = {}
print('introdu input:')
'''         
George 5000 Contabilitate
Ion 3000 Paza
Vasile 4000 Marketing
Diana 4500 Management
Monica 3500 Marketing
Sorin 3100 Paza
Corina 5300 Contabilitate
Lavinia 4900 Management
'''
s = input()
i = 0
while len(s) >= 1:
    ls1 = s.split(" ")
    k = ls1[0]
    v = ls1[1]
    dict1[k] = v
    i += 1
    s = input()

print('i', end='')
print(i)
print('dict1', end='')
print(dict1)
print('ls1', end='')
print(ls1)

print('mediaSalariilor', end='')
print(dict1.values());
lspec =[]
lspec= dict1.values()
print('listaspeciala', end='')
print(lspec)


dict2 = {}
print('introdu input dict2:')
s = input()
while len(s) >= 1:
    ls2 = s.split(" ")
    k = ls2[0]
    v = ls2[2]
    dict2[k] = v
    s = input()
print('dict2', end='')
print(dict2)



dict3 = {}
dict31 = {}
#cheia va departamenul si valoarea este suma celorlalte valori
print('introdu input dict3:')
s = input()
while len(s) >= 1:
    ls3 = s.split(" ")
    k = ls3[2]
    v = int(ls3[1])
    dict3[k] = v
    s = input()

print('dict3', end='')

a = len(ls3)
print('lungimea listei3 este: ', end='')
print(a)
sold = 0

for v in dict3.values():
    sold += int(v)
print(sold)
print(dict3)
valMed = sold/a
print(valMed)
'''lspec2 = []
lspec2 = dict3.values()
print(lspec2) '''
print(dict31)





dict4 = {}
print('dict4', end='')
print(dict4)