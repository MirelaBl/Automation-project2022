"""
401 Functii
Functii
PF 22.05.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=redefined-builtin
# pylint: disable=missing-function-docstring
# pylint: disable=function-redefined
# pylint: disable=too-many-function-args
# pylint: disable=not-callable
# pylint: disable=unidiomatic-typecheck
# pylint: disable=no-value-for-parameter
# pylint: disable=assignment-from-no-return
# pylint: disable=undefined-variable
# pylint: disable=redefined-outer-name
# pylint: disable=global-statement
# pylint: disable=global-variable-undefined


# Numele functiei
# o functie predefinita poate fi suprascrisa - nu vom avea acces la ea decat la restart

def len():
    print('am suprascris functia predefinita len')

# un exemplu de suprascriere a altei functii


def aria(a, b):
    """Calculeaza aria dreptunghiului
    primind ca argumente valorile laturilor"""
    return a * b


print(aria(7, 50))


def aria(raza):  # rescriem functia
    """Calculeaza aria cercului (primeste ca parametru raza)""" #
    return 3.14159 * raza ** 2


print(aria(7, 8))  # daca incercam s-o apelam asa cum o stiam - eroare
print(aria(5))  # apelarea actuala

print(aria.__doc__)
help(aria)

# NU dati un nume identic cu al unei variabile globale

var_glob = 50

print(var_glob)

def var_glob():
    print('A suprascris variabila. Variabila dispare, ramane functia')

print(var_glob)
var_glob()  # e OK, functia este executata
var_glob = 100  # schimbam valoarea variabilei
var_glob()  # NU mai functioneaza dupa ce am modificat valoarea variabilei


# nume incorect
# def 2_numere(a, b):


# Parametrii functiei
# Functie fara parametri
def test():
    print('Test')

test()


# functie cu parametri pozitionali
def test_parametri(nume, varsta):
    if type(nume) is str and type(int(varsta)) is int:
        print(nume, 'are', varsta, 'ani!')
    else:
        print('Parametrii incorecti!')


test_parametri('Maria', 34)  # apelare corecta a functiei
test_parametri(34, 'Maria')  # parametrii inversati, tipuri de date diferite
test_parametri('Maria')  # numar incorect de parametrii

test_parametri(varsta='34', nume='Ion')
d = {'nume' : 'Catalina', 'varsta' : 19}
l = ['Marin', 28]
test_parametri(**d)  # va fi detaliat in exercitiile urmatoare
test_parametri(*l)  # va fi detaliat in exercitiile urmatoare


# functie cu parametri care au valori default
def vremea(ploua='', ger=''):
    if ger:
        print('Imbraca-te gros!')

    if ploua:
        print('Ia-ti umbrela!')
    else:
        print('Zambeste!')

vremea()
vremea('ploua')
vremea(ploua='da')
vremea('ger')
vremea(ger='da')
vremea(ger='da', ploua='da')


# Fara return
def aduna(p1, p2):
    print(p1 + p2)

x = aduna(5, 7)  # nu stocheaza rezultatul intors de functie. Nu este o atribuire de valoare
x += 100  # testare

print(type(x))

# Cu return. Return poate fi urmat de o expresie. Rezultatul va fi printat automat
# fara sa mai fie nevoie de o variabila suplimentara
def aduna(p1, p2):
    suma = p1 + p2
    return suma


x = aduna(5, 7)
x += 100
print(x)


# Atentie la o functie care are print in rezultat
def salut(nume):
    print('Hello', nume)

print(salut('Vasile'))  # Apelare cu print rezultat denaturat
salut('Ioana')  # Apelare doar cu nume functie rezultat corect


# Variabila globala / variabila locala / namespace
var_x = 10  # variabila globala
print(var_x)

def test(numar):
    if numar < 25:
        var_x = 25  # variabila locala
    return var_x

print(test(15))  # functia apeleaza var globala si transmite rezultatul variabilei locale
# cu acelasi nume

print(var_x)  # variabila globala nu-si modifica valoarea

# Variabila globala - asa da - modificare
z = 1
def test_global(numar):
    global z
    z = numar * 2
    return z * numar

test_global(19)
print(z)

# Variabila globala - asa nu - modificare
def test_global1(numar):
    global var
    var = numar * 3
    return var * numar

print(var)
test_global1(25)
print(var)


# alt exemplu
glo = 100  # definim o var globala

def test_glo():  # scriem o functie care foloseste variabila globala
    print(glo)

test_glo()

def test_loc():  # scriem o functie care foloseste o var locala cu nume identic cu al celei globale
    glo = 5  # variabila locala are prioritate fata de cea globala, daca n-a fost definita global
    print(glo)

test_loc()

print(glo)  # valoarea var globale ramane neschimbata


# Incapsulare / return

def calculeaza(a, b, c):
    result = (a + b) * c  # d este variabila locala, nu este vizibila in afara functiei
    return result  # la fel si parametrii a, b, c

calculeaza(1, 2, 3)
print(result)  # NU sunt vizibili in afara functiei
print(a, b, c)


input('Apasa <enter> pentru a iesi.')
