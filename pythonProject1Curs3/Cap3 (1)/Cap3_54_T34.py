"""
Sedinta 3
Tema 34
Paul Fratila 29.07.2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement

t1 = ("Bunica", "Mihai-Daniel", "primar", "reumatologie")
t2 = ("Donca", "Cornelia-Ana", "primar", "chirurgie")
t3 = ("Achiriloaie", "Lorand-Levente", "specialist", "neurologie")
t4 = ("Papuc", "Raducu-Liviu", "primar", "homeopatie")
t5 = ("Cucuiu", "Nutu", "primar", "ortopedie")
t6 = ("Buia", "Tache", "specialist", "ginecologie")
t7 = ("Dragomanu", "Mitrut", "specialist", "ecografie")
t8 = ("Ticu", "Simona", "specialist", "psihiatrie")
t9 = ("Ene", "Adrian-Stefan", "specialist", "pediatrie")
t10 = ("Copae", "Toma", "primar", "neurologie")
t11 = ("Hotoi", "Dragos Alin", "specialist", "pediatrie")
t12 = ("Ceafalau", "Vincenţiu Mihail", "primar", "pediatrie")
t13 = ("Briceag", "Anca Stefana", "primar", "imagistica")
t14 = ("Condrea", "Nutu", "primar", "fizioterapie")
t15 = ("Cruceru", "Ioana-Loredana", "primar", "dermatologie")

"""
Se dau tuplurile de mai sus. Se cere:
- o baza de date cu dictionare si/sau liste cu toate datele (scalabila!)
- lista cu numele si prenumele tuturor medicilor;
- lista cu medicii care au specialitatea pediatrie (toate datele)
- lista cu medicii care au specialitatile neurologie sau psihiatrie
    (nume, prenume, tip)?
- lista cu  medicii primari (nume si prenume)
- ce specialitate au medicii cu prenumele 'Mitrut' sau numele 'Cruceru'
    (nume, prenume, tip, specialitate)
"""
"""for i,j in enumerate(t2):
    print(i,j)
"""

l1 = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15]
print(l1)
d1={k: v for k,v in enumerate(l1,start=1)}
print(d1)
