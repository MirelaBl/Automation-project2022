"""
451
Exercitii - Genereaza username pentru persoanele dintr-un fisier
PF 04.12.2020 v4
"""  #

# pylint: disable=invalid-name


enunt = """Creati un program care sa primeasca date dintr-un fisier text (people1.txt) si
Sa genereze username astfel: 
 - sa contina doar litere mici, 
 - incepe cu prima litera din prenume 
 - continua cu maxim 7 litere din nume
Rezultatul sa fie scris intr-un alt fisier (useri.txt)
Cititi fisierul nou pentru verificare.
Pasi de urmat:
- deschidem fisierul din care luam datele;
- deschidem fisierul in care postam username;
- facem split in doua variabile, pentru nume si respectiv prenume;
- concatenam cele doua siruri (prima litera din prenume cu celelalte din nume - max 7);
- scriem username generat in fisierul destinat.Atentie, concatenam username cu '\n' 
pentru a sari la linia urmatoare.
"""

inp = open('c:/_wt/people.txt', 'r')  	# deschidem fisierul din care luam datele
out = open('c:/_wt/scrie.txt', 'w')  	# deschidem fisierul in care postam username

for line in inp:
    line = line.rstrip()
    prenume, nume = line.split(' ')  	# facem split in doua variabile
    usr = str(prenume).lower()[0] + str(nume).lower()[:7]  			# concatenam cele doua siruri
    out.write(usr + '\n')  				# scrie username generat in fisierul destinat
										# concatenarea cu '\n' este necesara pt a sari la linia urmatoare

inp.close()
out.close()

citeste = open('c:/_wt/scrie.txt', 'r')

print(citeste.read())

citeste.close()

input('Apasa <enter> pentru a iesi.')
