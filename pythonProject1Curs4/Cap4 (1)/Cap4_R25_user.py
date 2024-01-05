"""
425
Genereaza username
PF 06.10.2020 v4
"""  #

# pylint: disable=invalid-name

enunt = """
# Creati o functie care sa genereze username format din prima litera a prenumelui si max 7 litere din nume#
# Numele si prenumele se introduc de la tastatura. Userul va fi format doar din litere mici               #
"""  #

def username():
    """Genereaza username pe baza prenumelui (primul caracter)
    si numelui (max 7 caractere) - (lowercase)"""  #
    p = input('Introduceti prenumele : ').lower()  # introducem first and last name
    n = input('Introduceti numele : ').lower()
    u = p[0] + n[:7]  # concatenam cele doua siruri
    print('Username este: ', u)  # returneaza username generat

username()

### - sau - ###

def uname(n, p):
    """primeste nume si prenume, returneaza username"""  #
    p1 = p[0].lower()
    n1 = n[0:7].lower()
    u = p1+n1
    return u

uname('Coman', 'Paraschiva')

### - sau - ###

def gen_user():
    """Alta varianta"""  #
    nume = input('Introduceti numele: \n').lower()
    prenume = input('Introduceti prenumele: \n').lower()
    if len(nume) == 6:
        user = prenume[0] + nume
    elif len(nume) > 6:
        user = prenume[0] + nume[:6]
    else:
        adauga = ''
        for i in range(6 - len(nume)):
            adauga += str(i)
        user = prenume[0] + nume + adauga
    return user

input('Apasa <enter> pentru a iesi.')
