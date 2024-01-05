"""
407 Functia lambda
Functia lambda
PF - 21.08.2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=no-else-return

aria_tri = lambda baza, inaltimea: baza * inaltimea * .5
celsius = lambda fahr: (5 / 9) * (fahr - 32)

concat = lambda a, b, c: a + b + c

ex = lambda x: [i for i in range(x) if i % 2 == 0]

aria_tri(10, 5)
aria_tri(3, 7)
celsius(32)
celsius(100)

concat([3], [4, 5], [1, 2])
concat('ana ', 'are ', 'mere')
concat(1, 1, 5)
concat('', 1, [])

lista_pare_100 = ex(100)

print(lista_pare_100)

input('Apasa <enter> pentru a iesi.')
