"""
104
Input - Captarea unui text de la tastatura
PF - 2020-04-13 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

# captarea unui text de la tastatura cu input (raw_input in versiunea 2.x)
    # o functie simpla
def salut():                                    # header: def + nume functie + (parametri) + :
    numele = input('Introduceti numele: ')      # blocul de instructiuni este indentat
    orasul = input('Introduceti orasul: ')      # identarea cu 4 spatii (general acceptat)
    varsta = input('Introduceti varsta: ')

    return  'Salut, sunt ' +  numele + '\n' + \
            'locuiesc in ' + orasul + \
            '\nsi am ' + varsta + ' ani'        # ca sa utilizeze \n este utilizata concatenarea,
                                                # iar apelarea se face cu print(nume_functie())

print(salut())

def salut1(nume, oras, varsta):
    return 'Salut!\n' + \
           'Sunt ' + nume + \
           '\ndin ' + oras + \
           '\nAm ' + str(varsta) + ' ani'

print(salut1('George', 'Iasi', 15))


def aduna(a, b):
    suma = a + b
    return suma

len('ceva')                 # returneaza numarul de caractere al sirului de caractere

# transformarea stringului captat in float sau int

ore_lucrate = input('Introduceti numarul de ore: ')     # mesajul este pentru utilizator
tarif_orar = input('Introduceti tariful orar: ')     # input introduce siruri de caractere

print('Ai de incasat: ', float(ore_lucrate) * float(tarif_orar))

# sau transformare direct la input
ore_lucrate = float(input('Introduceti numarul de ore: '))
tarif_orar = float(input('Introduceti tariful orar: '))

print('Salariul tau este:', ore_lucrate * tarif_orar)

input("Apasa <enter> pt a iesi.")

ore_lucrate = input('Introduceti numarul de ore: ')     # mesajul este pentru utilizator
ore_lucrate = float(ore_lucrate)
tarif_orar = input('Introduceti tariful orar: ')     # input introduce siruri de caractere
tarif_orar = float(tarif_orar)

print('Salariul tau este:', ore_lucrate * tarif_orar)