"""
303 Tuplu
Tuplu
PF - 20.06.2020 v4
"""  #


# pylint: disable=invalid-name
# pylint: disable=unsupported-assignment-operation
# pylint: disable=unidiomatic-typecheck

# Exemplu
a = 'Canta cucu\' ...'  		# variabila
x = (3, 'Acasa e soare', ('Si aici e soare', True, 7), False, a, 3, 3, a)  # tuplu
print(x[1])
print(x[2][0][3:10]) 			# un tuplu este indexabil
print(x[1][10])
x[0] =  5 	    # incercam sa atribuim valoarea 5 primului element (imutabil)

for items in x:
    print(items)     # for in tuplu

for items in x:
    print(items)
    if type(items) == str:
        print(items.split())

print(len(x))             # numara elementele tuplului
print(type(x))

# Comparatii intre tupluri
a = (1, 3, 4)
b = (1, 3, 5)
c = (2, 1, 1)
d = ('a', 'b', 'c')

print(a > b)                           # comparatia se face element cu element,
                    # deci la primele elemente diferite sau la final, daca sunt identice
print(b > a)
print(c > b)
print(c > d)

print(('abc', 1, 2) > ('aaa', 777, 'ssst..'))
print(('abc', 1, 2) > ('abc', 1, 'ssst..'))

# Metode si functii aplicabile
dir(x)

x.count(3)                   # numara aparitiile unui element in tuplu
x.count(False)
x.index(3, 6)                 # returneaza indexul unui element

len(x)

# Stoc
stoc = None

if not stoc:
    print('Stoc zero.')

stoc = ('Tigla', 'Tabla', 'Sitza')

print('Stocul cuprinde: ', stoc)

count = 0
for item in stoc:
    print('Index:', count, '- Element:', item)
    count += 1

for index, item in enumerate(stoc):
    print('Index:', index, '- Element:', item)

# alta fatza a tuplurilor

a = 'ana', 'are', 'multe', 'mere', 5   # creare tuplu
print(a)
print(type(a))

x, y, z, w, t = a   # 'spargerea' in variabile a uni tuplu

print(x, y, z, w)


input('Apasa <enter> pt a iesi.')

t = (5)  # incorect
print(type(t))

t1 = (5, )  # corect
print(type(t1))
