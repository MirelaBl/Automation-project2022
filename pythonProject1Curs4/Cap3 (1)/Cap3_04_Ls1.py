"""
304 Lista
Lista - structura
PF - 26.06.2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=unnecessary-comprehension

# Exemple
print(["Prima", "mea", "lista"])
print([3, 7, 13])
print([True, False])
lx = [3, "Acasa e soare", ("Si aici e soare", 7), False, [1, 2, 3]]
la = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
len(la)
print(la[2])
print(la[-2])
print(la[12])  # eroare daca nu exista indexul
print(la[-13])

# Putem modifica cate un element al unei liste
la[2] = "Martie"
print(la)
la[-5] = "August"
print(la)

# Initializare lista
l = []  # sau

l = list((2, "d", "jhsgk"))

print(l)  # sau

# Comprehension - putem crea o lista si astfel
patrate = [x ** 2 for x in range(1, 101)]  # lista patratelor numerelor de la 1 - 100
print(patrate)

p = []
for i in range(1, 101):
    if i % 11 == 0:
        p.append(i ** 2)
print(p)

# sau
patrate_11 = [x ** 2 for x in range(1, 101) if x % 11 == 0]
print(patrate_11)  # lista patratelor de la 1 - 100, doar pentru numerele div cu 11

# sau
l_100 = [i for i in "Astazi ploua cu soare".split()]  # lista cuvinte
l_200 = [i for i in "Astazi ploua"]  # lista caractere

print(l_100)
print(l_200)

# Nested lists
print([[1, 2], [3, 4], [5, 6]])
print([["x", "y", "z"], ["a", "b", "c", ["Luni", "Marti", "Miercuri"]]])
lb = [[1, 2, 3], [4, 5, 6]]
print(lb[0][2])
print(lb[1][1])
print(len(lb))

# Slicing intr-o lista
print("Q1:", la[0:3])
print("Q2:", la[3:6])
print("S1", la[:6])
print(la[0 : len(la)])
print("S2", la[6:])
print("Lunile anului:", la[:])
print(la[2::3])  # slicing cu pas

# +---+---+---+---+---+
# | H | e | l | p | ! |
# +---+---+---+---+---+
# 0   1   2   3   4   5
# -5  -4  -3  -2  -1

# Range
print("Numerele de la 0 la 5:")
print(list(range(6)))
print("Numerele de la 7 la 10:")
print(list(range(7, 11)))
print("Numara cu pas de 5 pana la 50:")
print(list(range(3, 53, 5)))
print("Numere negativ:")
print(list(range(-5, 0)))
print("Numere negative cu pas de -3:")
print(list(range(0, -10, -3)))
print("Numara invers de la 10 la 1 cu pas de 1:")
print(list(range(10, 0, -1)))

# printarea elementelor listei
for i in range(2, len(la), 3):
    print(i + 1, la[i])

for i in la:
    print(i, end=", ")
    print("Luna cu soare")

    # elefantii / panza de paianjen
for i in range(1, 100):
    if i == 1:
        print("1 elefant, se legana, pe o panza de paianjen")
        print("Si pentru ca, nu se rupea, a mai chemat un elefant\n...")
    elif i >= 2:
        print("{0} elefanti, se leganau, pe o panza de paianjen".format(i))
        print("Si pentru ca, nu se rupea, a mai chemat un elefant\n...")

input("Apasa <enter> pt a iesi.")
