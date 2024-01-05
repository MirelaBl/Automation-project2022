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
dictN_s = {}
dictN_d = {}
dictD_vms = {}
dictD_nrm ={}
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
    ls = s.split(" ")
    nume = ls[0]
    salariu = int(ls[1])
    depart = ls[2]
    dictN_s[nume] = salariu
    dictN_d[nume] = depart
    if depart in dictD_nrm.keys():
        dictD_nrm[depart] += 1
        dictD_vms[depart] += salariu
    else:
        dictD_nrm[depart] = 1
        dictD_vms[depart] = salariu
    s = input()

del s, ls
print('dictN_s', end='')
print(dictN_s)
print('dictN_d', end='')
print(dictN_d)
print('dictD_nrm', end='')
print(dictD_nrm)
print('dictD_vms', end='')
print(dictD_vms)

for depart, salariu in dictD_vms.items():
    dictD_vms[depart] /= dictD_nrm[depart]

print('dictD_vms', end='')
print(dictD_vms)