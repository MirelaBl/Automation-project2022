'''
Vienna Bayern 2 1
Salzburg Dortmund 1 3
Bayern Salzburg 2 2
Dortmund Vienna 1 0
Vienna Salzburg 3 0
Dortmund Bayern 3 3
'''

import operator
dictPt ={}
dictGol={}
dictGolIn={}
print('introdu input: ')
s = input()
i = 0
while len(s) >= 1:
    ls = s.split(" ")
    gazda = ls[0]
    oaspeti = ls[1]
    mg = int(ls[2])
    mo = int(ls[3])
    if mg > mo :
        pg, po = 3, 0
    elif mg < mo:
        pg, po = 0, 3
    else:
        pg, po = 1, 1

    if gazda in dictPt.keys():
        dictPt[gazda] += pg
        dictGol[gazda] += mg
        dictGolIn[gazda] += mo
    else:
        dictPt[gazda] = pg
        dictGol[gazda] = mg
        dictGolIn[gazda] = mo

    if oaspeti in dictPt.keys():
        dictPt[oaspeti] += po
        dictGol[oaspeti] += mo
        dictGolIn[oaspeti] += mg
    else:
        dictPt[oaspeti] = po
        dictGol[oaspeti] = mo
        dictGolIn[oaspeti] = mg

    s = input()

print('dictPt', end='')
print(dictPt)
print('dictGol', end='')
print(dictGol)
print('dictGolIn', end='')
print(dictGolIn)

dictPt = dict(sorted(dictPt.items(), key=operator.itemgetter(1),reverse=True))

print('dictPt', end='')
print(dictPt)
i = 1
for k,v in dictPt.items():
    print(i,k,dictGol[k],"-", dictGolIn[k],v, sep= " ")
    i += 1