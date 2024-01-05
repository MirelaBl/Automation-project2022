"""
Cap 3 tema 1
Introduce elem in lista, o sorteaza
PF - 18.07.2020 v4
"""  #

# pylint: disable=pointless-string-statement

"""
Creati un program ce are ca scop sortarea a x elemente, introduse de utilizator de la
tastatura (input) printr-o bucla while, intr-o lista.
Elementele vor fi inserate pe rand in lista prin capturare de text.
Inserati la inceputul programului numarul de elemente dorit (x) - in afara buclei.
Atentie la conditia de iesire din bucla (cand au fost introduse x elemente).
Afisati lista sortata la final.
    Pasi de urmat:
1. input - cate elemente dorim sa inseram?
2. initializam o lista;
3. bucla while cu input pentru introducere elemente noi --> adaugare in lista
4. sortare lista (metoda) si printare"""  #


count = 5
count1= 0
lista = []
while True:


    if(count > 0 & count <= 5):
        count -= 1
        count1 += 1
        print('introdu text:')
        text = input()
        lista.append(text)
        continue
    elif(count == 0):
        print('ai introdus nr max de elem  ' +str(count1))
        break


print(lista)
input('Apasa <enter> pt a iesi.')