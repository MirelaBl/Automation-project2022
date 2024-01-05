'''
sa se defineasca o functie cu numele Operatii care primeste 2 parametrii cu numele x si y
acesta functie treb sa returneze un tuplu a carui prim membru este suma, al 2 lea membru este x-y
al 3 lea membru este x * y,al 4 lea este x / y

atentie y nu are voie sa fie 0

apoi sa se apeleze aceasta functie si sa se afize toti membrii tuplului rezultat'''
import math

def operatii(x,y):
    t1 = (x+y, x-y, x*y, x/y)
    return t1

print(operatii(2,4))

'''
-----------
o functie care primeste ca parametru un dictionar
input
acest dict are cheia niste val aleatori
si valorile sunt probabilitatile gen 0.6. --+1
in interiorul acestei functii sa se calculze media, media patratica, abaterea stand, err nornal, val sup si val inf
tuplu este format din 1. media 2. val inf si 3. val sup  --> 3 atribute in tuplu
'''
from math import sqrt

def functie(d1):
    n = len(d1.keys())
    media = 0
    for k in d1.keys():
        media += k * d1[k]
    medPat = 0
    for a,b in d1.items():
        medPat += (a**2)*b
    disp = medPat-(media**2)
    print("media:",media)
    print("medPat:",medPat)
    print("media**2:",media**2)
    print("disp:",disp)
    abatStand = math.sqrt(disp)
    errnormal = 3*abatStand/math.sqrt(n)
    valSup = media + errnormal
    valInf = media - errnormal
    t = (media, valInf, valSup)
    return t

d1 = {0:0.1, 1:0.1, 2:0.25 ,3:0.25, 4:0.2, 5:0.1 }
t = functie(d1)
print(t)




'''
---
set
se cit de la tastatura pe fiecare rand numele olipicilor la matematica gen george
apoi se vor citi si olipicii la informatica
sa se ofere ca premiu 1000 de euro pentru olipicii la o singura
si 3000 de euro pt olimpicii la 2 materii

care trebuie sa fie fondul de premii ( intersectii, reunii) 

'''