"""
706 Module
Modulul tempfile
PF - 24.06.2021 v7
"""  #


import tempfile
import os

t1 = tempfile.TemporaryFile()  # creaza un fisier temporar care va fi sters automat

t1.write(b'ana are cirese')
t1.seek(0)
t1.read()

d1 = tempfile.TemporaryDirectory()  # creaza un director temporar care va fi sters automat

temp = tempfile.mkstemp()  # cream fisierul. temp stocheaza calea. Trebuie sters manual
print(temp)

fisier = open(temp[1], 'w+')
fisier.write('''Astazi 15 Iun e ziua ta, Zi frumoasa ca tine''')
fisier.close()

fisier = open(temp[1], 'r+')
fisier.seek(0)
fisier.read()
fisier.close()

print(tempfile.gettempdir())  # directorul in care se afla fis temporar )

nume_director = tempfile.mkdtemp()  # creeaza un director temporar. Trebuie sters manual
print(nume_director)

tempfile.tempdir = 'c:\\_wt1\\test1'     # schimba directorul default in care sunt create

os.remove(temp[1])
os.rmdir(nume_director)
