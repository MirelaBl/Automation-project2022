"""
712 Module
Modulul datetime
PF - 15.06.2021 v6
"""  #


import datetime

i = datetime.datetime.now()  # stocheaza momentul de timp curent
print(i)

print("Date and time in ISO format = {0}".format(i.isoformat()))
# extragem diferite componente din datetime
print("Current year = {0}".format(i.year))
print("Current month = {0}".format(i.month))
print("Current date (day) =  {0}".format(i.day))
print("dd/mm/yyyy format =  {0}/{1}/{2}".format(i.day, i.month, i.year))
print("Current hour = {0}".format(i.hour))
print("Current minute = {0}".format(i.minute))
print("Current second =  {0}".format(i.second))
print("hh:mm:ss format = {0}:{1:02d}:{2:02d}".format(i.hour, i.minute, i.second))

print("Current date & time = {0}".format(datetime.datetime.now()))

# Alternativ
from datetime import datetime

i = datetime.utcnow()  # gmt time
print(str(i))

# formatam momentul de timp in formatul dorit
print(i.strftime('%Y/%m/%d %H.%M.%S'))
print(datetime.now().strftime('%A %B %d %Y'))
print(datetime.now().strftime('%d/%b/%Y %H.%M.%S'))

# transformam din string in datetime
print(datetime.strptime('27-05/2021T11.59.59 PM', '%d-%m/%YT%I.%M.%S %p'))

# combinam cele doua metode precedente
print(datetime.strftime(datetime.strptime ('2017-18/01', '%Y-%d/%m'), '%d.%m.%Y'))


import datetime

# deltatime
b = datetime.datetime.utcnow()
a = datetime.datetime.now()

print(a - b)
print(a.replace(microsecond=0,) - (b.replace(microsecond=0)))

x = datetime.datetime(2000+20,12,10, 5, 35, 59, 1)  # parametrii an, luna, zi, ora, min, secunda, microsecunda
y = datetime.datetime(2020,1,1, 0, 0, 0, 0)  # parametrii sunt numere intregi, pot fi calculati cu expresii
print(x - y)

# class date(year, month, day)
datetime.date.fromtimestamp(1547658549.999999 + 86400 * 881)  # primeste nr_de_secunde intoarce localdate
datetime.date.isocalendar(datetime.date.today())  # ISO year, week number, and isoweekday (1-7)
datetime.date.isoformat(datetime.date.today())  # aaaa-ll-zz
datetime.date.timetuple(datetime.date(2021, 1, 15))  # ultimele trei argument datetime.date(an, luna, zi)
datetime.date.today()

# class datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
datetime.datetime.isoformat(datetime.datetime(2021,3,3))
datetime.datetime.isoformat(datetime.datetime(2021,3,3, 10))
datetime.datetime.isoformat(datetime.datetime(2021,3,3, 10, 15))
datetime.datetime.isoformat(datetime.datetime(2021,3,3, 10, 15, 59))
datetime.datetime.isoformat(datetime.datetime(2021,3,3, 23, 59, 59, 999999))


# class timedelta
referinta = datetime.timedelta(100, 36000, 101010)  # zile, secunde, microsecunde
datetime.timedelta.total_seconds(referinta)  # returneaza secunde
datetime.datetime.now() - referinta  # returneaza datetime din ziua de referinta
datetime.datetime(2021, 3, 7) + referinta   # datetime din urma cu referinta


# transforma in time.time() (timestamp)
datetime.datetime.timestamp(datetime.datetime(2021,1,16, 19, 9, 9, 999999))  # secunde de la 1.1.1970


# adauga la o data un numar de zile
datan = datetime.date(2021, 1, 1) + datetime.timedelta(165)

print(datan.year, datan.month, datan.day)

from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    result = abs((d2 - d1).days)
    return result

days_between('2021-06-15', '2021-01-01')
