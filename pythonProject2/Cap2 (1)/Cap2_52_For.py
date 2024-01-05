"""
252 Bucle for
For / range
PF - 08/05/2020 v4
"""  #

# pylint: disable=invalid-name

print("Numara de la 0 la 5:")
# Utilizeaza o bucla for si functia range pentru a afisa numerele de la 0 la 5 inclusiv:
for x in range(0,6):
    print(x)

print("Numara din cinci in cinci pana la 50:")
# Utilizeaza o bucla for si functia range pentru a afisa numerele
# de la 0 la 50 inclusiv, cu pas de 5:
for x in range(0,51,5):
    print(x)



print("Numara invers de la 10 la 1:")
# Utilizeaza o bucla for si functia range pentru a afisa numerele de la 10 la 1:
for x in range(10,-1,-1):
    if x !=0:
        print(x)
        print('wait')
    else:
        print('boom!!!!!!!!!!')

input("Apasa <enter> pt a iesi.")
