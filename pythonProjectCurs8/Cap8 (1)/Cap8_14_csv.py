"""
814 Module
Modulul csv - exemple
PF - 29.06.2021 v6
"""  #

# https://docs.python.org/3.9/library/csv.html      #module-csv - documentatie


import csv

# csv.reader(csvfile, dialect='excel', **fmtparams)

# listeaza fiecare rand cu separatorul ";" intre valorile campurilor
with open('c:/_wt/medici.csv', newline='', encoding='utf-8') as csvfile:
    medici_reader = csv.reader(csvfile)
    print(type(medici_reader))
    for row in medici_reader:
        print('; '.join(row))

# listeaza pentr fiecare rand o lista cu valorile campurilor
with open('c:/_wt/medici.csv', newline='', encoding='utf8') as csvfile:
    medici_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in medici_reader:
        print(row)

# Prelucreaza informatiile pentru fiecare rand
with open('c:/_wt/medici.csv', newline='', encoding='utf8') as csvfile:
              medici_reader = csv.reader(csvfile, delimiter=',', quotechar=None)
              for row in medici_reader:
                  print('Nume: '.ljust(14), row[0])
                  print('Prenume: '.ljust(14), row[1])
                  print('Tip: '.ljust(14), row[2])
                  print('Specialitate: '.ljust(14), row[3])
                  print('Fullname: '.ljust(14), row[0] + ' ' + row[1])
                  print('*' * 35)

# csv.writer(csvfile, dialect='excel', **fmtparams)¶

# scrie intr-un fisier .csv
with open('scrie_fisier.txt', 'w+', newline='') as handle:
    scrie_lucru = csv.writer(handle)
    scrie_lucru.writerow(['Corina','Popescu','1987-02-05'])
    scrie_lucru.writerow(['Ion','Coman','1989-05-05'])
    handle.seek(0)
    print(handle.readlines())