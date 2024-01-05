'''
Pe fiecare rand se afla un sir de caractere format dintr un singur cuvand si un numar natural, la un moment dat pe un rand
nu mai exista nimic
1. Sa se introduca aceste perechi intr un dictionar si apoi acestea sa se afiseze
2. fiecare numar natural devine de 10 ori mai mare si sa se afiseze dictionarul asa cum arata
3.cheile dictionarului sa se mute intr o lista
4. lista sa se ordoneze crescator dupa numarul de vocale

'''

def nrVocale(s):
    sv = 'aeiou'
    i = 0
    for c in s:
        if sv.find(c) > 0:
            i = i + 1
            #print(i)
    return i


dict1= {}
print('introdu input:')
s = input()
while len(s) > 1:
    lc = s.split(" ")
    if len(lc) != 2:
        continue
    k = lc[0]
    v = int(lc[1])
    dict1[k] = v
    s = input()

print(dict1)
for k,v in dict1.items():
    dict1[k] = 10*v

print(dict1)

listaKey = list(dict1.keys())
print(listaKey)

listaKey.sort(key=nrVocale)
print('noua lista: ',end = ' ')
print(listaKey)
for k in listaKey:
    print(k ,dict1[k], sep='-')

