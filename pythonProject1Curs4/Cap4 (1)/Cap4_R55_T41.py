"""
455
Exercitii - Crearea unei functii simple
PF 18.09.2020 v4
"""  #

# pylint: disable=invalid-name

enunt = """Creati un program cu o functie care returneaza numarul de cifre dintr-un sir
de caractere dat ca parametru de intrare. Aplicati functia pentru trei siruri
diferite introduse de la tastatura.
Creati o functie care numara literele, cifrele, spatiile si total caractere
"""

# Numara cifre
def numara_cifre(sir):
    """Returneaza numarul de cifre dintr-un string"""
    count = 0
    for e in sir:
        if e.isdigit():
            count += 1
    return count

print("Sirul 1 are {0} cifre".format(numara_cifre(input('Introdu sirul: '))))
print("Sirul 2 are", numara_cifre(input('Introdu sirul: ')), 'cifre')
print("Sirul 3 are %d cifre" % numara_cifre(input('Introdu sirul: ')))


# Numara toate
def numara_car(sir):
    """Numara cifere, litere, spatii intr-un string"""
    count1 = 0
    count2 = 0
    count3 = 0
    for e in sir:
        if e.isdigit():
            count1 += 1
        elif e.isalpha():
            count2 += 1
        elif e.isspace():
            count3 += 1
    print('Sirul tau are in total caractere: ' + str(count1 + count2 + count3) + '\n', \
          'cifre : ' + str(count1), '\nlitere: ' + str(count2), '\nspatii: ' + str(count3))


numara_car(input('Introdu sirul: '))
