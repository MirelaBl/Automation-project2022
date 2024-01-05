'''de la tastura se citeste un rand care contine numere naturale separate de spatiu
1. sa se introduca in lista doar numerele pozitive
2. intr o multumime (set) sa se adauge numerele negative
3. sa se gaseasca si sa se afiseze minimul listei
4. sa se gaseasca si sa se afiseze maximul  multimii
5. sa se concateneze multimea in dreapta listei
6. sa se creeze o functie care primeste un numar natural si returneaza valoarea ultimei cifre
7. sa se sorteze lista dupa ultima cifre dar in prealabil toate numerele sa fie transformate in pozitive ( modulo)'''


def ultCif(n):
    return n%10

print('introdu input:')
s = input()
lc = s.split(" ")

print(s);
print(lc);

l = []
set1 = set()
for x in lc:
    n = int(x)
    if n >= 0:
        l.append(n)
    else:
        set1.add(n)


print(l);
print(set1);
print('minimul listei este:',end=' ')
print(min(l))
print('maximul setului este:',end=' ')
print(max(set1))
print(' se concateneaze multimea in dreapta listei')
l.extend(set1)
print(l)

for i in range(len(l)):
    l[i] = abs(l[i])

print(l)

l.sort(key=ultCif)
print('lista finala',end=' ')
print(l)