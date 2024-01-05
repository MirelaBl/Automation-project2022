import json

enunt = """
 Creati un program care sa aiba o functie numita dataAleatorie care returneaza
   o lista din trei elemente.
       - Primul element al listei sa fie un an aleatoriu intre 2023 si 2025.
       - Al doilea element al listei sa fie o luna aleatorie returnata ca numar intre 1 si 12.
       - Al treilea element al listei sa fie o zi intre 1 si numarul de zile din luna aleasa
 1. Apelati de trei ori functia si stocati rezultatul in cate o variabila.
 2. Aflati numele zilei pentru datele returnate.
 3. Serializati cu json cele trei date obtinute.
 4. Folositi modulele datetime si time pentru a obtine structuri specifice plecand de la 
 rezultatul functiei noastre.
 """ #

from random import randint

from calendar import mdays, isleap, weekday, day_name
def dataa():
	anul = randint(2023, 2025)
	luna = randint(1, 12)
	ziua = randint(1, 29) if isleap(anul) and luna == 2 else randint(1, mdays[luna])

	return [anul, luna, ziua]

data1 = dataa()
print(data1)

nr_day = weekday(*data1)
print(nr_day)

name_of_day = day_name[nr_day]
print(name_of_day)

with open("json_test.json", "w") as handle:
	json.dump([data1, nr_day, name_of_day], handle)

with open("json_test.json") as handle:
	date_accesate = json.load(handle)

type(date_accesate)
date_accesate[2]