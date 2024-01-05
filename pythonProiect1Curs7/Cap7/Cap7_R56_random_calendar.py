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

from random import randint, randrange
from calendar import isleap, mdays, weekday, day_name
from json import load, dump
from datetime import datetime
from time import strptime

def dataAleatoriu():
    an = randint(2021, 2025)
    luna = randint(1, 12)
    if isleap(an) and luna == 2:
        zi = randint( 1, 29)
    else:
        zi = randint(1, mdays[luna])
    result = [an, luna, zi]
    return result

# punctele 1, 2
data1 = dataAleatoriu()
print("Data 1 aleasa este anul: {0}, luna: {1}, ziua: {2}".format(*data1))
zi_sap1 = weekday(*data1)
print("Ziua saptamanii pt. data aleasa este ", day_name[zi_sap1])

data2 = dataAleatoriu()
print("\nData 2 aleasa este anul: {0}, luna: {1}, ziua: {2}".format(*data2))
zi_sap2 = weekday(*data2)
print("Ziua saptamanii pt. data aleasa este ", day_name[zi_sap2])

data3 = dataAleatoriu()
print("\nData 3 aleasa este anul: {0}, luna: {1}, ziua: {2}".format(*data3))
zi_sap3 = weekday(*data3)
print("Ziua saptamanii pt. data aleasa este ", day_name[zi_sap3])

# punctul 3
fisier = "fisier.json"
with open(fisier, "w") as handle:
    dump([data1, data2, data3], handle)
with open(fisier, "r") as handle:
    date_restaurate = load(handle)
print("\nDate restaurate din fisierul json: ",date_restaurate)

# punctul 4
print("\nStructura datetime: ", datetime.strptime(str(data3), '[%Y, %m, %d]'))
print("\nStructura time: ", strptime(str(data3), '[%Y, %m, %d]'))
