"""
756 Module
Utilizare module random si calendar
PF - 24.06.2021 v7
"""  #

enunt = """
 Creati un program care sa aiba o functie numita dataAleatorie care returneaza
   o lista din trei elemente.
       - Primul element al listei sa fie un an aleatoriu intre 2021 si 2025.
       - Al doilea element al listei sa fie o luna aleatorie returnata ca numar intre 1 si 12.
       - Al treilea element al listei sa fie o zi intre 1 si numarul de zile din luna aleasa
 1. Apelati de trei ori functia si stocati rezultatul in cate o variabila.
 2. Aflati numele zilei pentru datele returnate.
 3. Serializati cu json cele trei date obtinute.
 4. Folositi modulele datetime si time pentru a obtine structuri specifice plecand de la 
 rezultatul functiei noastre.
 """ #

from random import randint
from calendar import isleap, mdays, weekday, day_name
from json import dump, load
from datetime import datetime
from time import strptime

def dataAleatoriu():
    anul = randint(2021, 2025)
    luna = randint(1, 12)
    ziua = randint(1, 29)  if isleap(anul) and luna == 2 else randint(1, mdays[luna])
    rezultat = [anul, luna, ziua]
    return rezultat

# rezolvare pct 1
data1 = dataAleatoriu()
print('Data1:', data1)
data2 = dataAleatoriu()
print('Data2:', data2)
data3 = dataAleatoriu()
print('Data3:', data3)

# rezolvare pct 2
ziua1 = weekday(*data1)
print('\nZiua1:', day_name[ziua1])
ziua2 = weekday(*data2)
print('\nZiua2:', day_name[ziua2])
ziua3 = weekday(*data3)
print('\nZiua3:', day_name[ziua3])

# rezolvare pct 3
fisier = "fisier.json"
with open(fisier, 'w') as handle:
    dump([data1, data2, data3], handle)
with open(fisier) as handle:
    date_obtinute_json = load(handle)
print('\nDate json:', date_obtinute_json)

# rezolvare pct. 4
elem_datetime = datetime.strptime(str(data1), '[%Y, %m, %d]')
print(elem_datetime)

struct_time = strptime(str(data1), '[%Y, %m, %d]')
print(struct_time)