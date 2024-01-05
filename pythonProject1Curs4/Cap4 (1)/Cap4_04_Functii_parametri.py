"""
404 Functii
Functii - argumente multiple
PF 	22.05.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=unidiomatic-typecheck
# pylint: disable=no-value-for-parameter


# 01 crearea unei functii cu numar variabil de parametri *args   si   **kwargs
def exemplu(*args):  				# *args - permite un numar variabil de parametri
    """Functia aduna mai multe numere primite ca argument.
	Returneaza suma si lista numerelor"""
    print(type(args))
    suma = 0
    lista = []
    for i in args:
        if type(i) == int:
            suma += i
            lista.append(i)
    if lista:
        result = 'Suma numerelor : ' + str(lista) + ' este ' + str(suma)
    else:
        result = 'Nu ai introdus numere'
    return result


exemplu(1, 2, 5, 6, 8)
exemplu('a', 'b', 'c')
exemplu(1, 'a', '9', 100)
tn = (5, 10, 25, 117)
ln = [1, 5, 9, 25, 4587, 58569, 387]
sn = {4, 6, 9}

exemplu(4, 5, 9, *sn, *tn, *ln, ln, 1, 5, 9)

# 02 Exemplul 2

def fructe(*f):
    """Docstring!"""  #
    for count, fruct in enumerate(f, start=1):  			# enumerate aloca index incepand cu zero
        print(count, '-->', fruct)		# count va fi dat de enumerate, fruct de parametri

fructe('alune', 'caise', 'coacaze', 'prune')

lf = ('alune', 'caise', 'coacaze', 'prune', 'mere', 'piersici')

fructe(*lf, 'capsuni', 'struguri')

# 3 Exemplul 3

def pers(nume, *args, a=2, **kwargs):  		# *args - parametri multipli  -->  tuplu, lista
    """Docstring!"""  #
    print((nume + ' ') * a)  					# **kwargs - paramatri multipli de tip key = values --> dict
    print('-' * 30)
    if args:  							# daca avem argumente multiple tip tuplu
        print(args)
    print('-' * 30)
    if kwargs:  						# daca avem argumente multiple key = value
        print(kwargs)

# Apelare doar cu nume
pers("Vasile")

# Apelare cu nume si argumente tuplu
pers("Georgiana", "alt fruct", 'fata blonda', 'ochi albastri', 'necasatorita')

# Apelare cu parametri de toate tipurile
pers("Marcel", 5, 'ochi negri', 'necasatorit', salariu=100000, masini=3, case=2)

l = ['bruneta', 'ochi negri', 'necasatorita']
d = {'salariu':100000, 'masini':3}

print(d)

pers('Corina', 'h', *l, (1, 3, 6), 'abc', *'abc', 15, varsta=29, **d)

pers('Corina', *d.values())
