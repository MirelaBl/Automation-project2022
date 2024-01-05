"""
710 Module
Modulul time
PF - 15.06.2021 v6
"""  #


import time

metacaractere = """
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour(24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour(12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        %w  Weekday as a decimal number [0(Sunday),6].
        %j  Day of the year as a decimal number [001,366].
"""

struct_time = """
      year(including century, e.g. 1998)                %Y
      month(1-12)                                       %m                              
      day(1-31)                                         %d
      hours(0-23)                                       %H
      minutes(0-59)                                     %M
      seconds(0-59)                                     %S
      weekday(0-6, Monday is 0)                         %w
      Julian day(day in the year, 1-366)                %j
      DST(Daylight Savings Time) flag(-1, 0 or 1)       --
"""


# struct_time
print(time.localtime())
print(time.gmtime())


# afisare sub forma de string  'Tue Jun 15 12:53:11 2021' (implicit din localtime)
print(time.asctime())
print(time.asctime(time.gmtime()))


# ... ia o pauza
time.sleep(5)
print('Pauza s-a sfarsit, apuca-te de treaba :)')  # suspenda executia timp de 5 secunde


# extrage din struct time elementele dorite (implicit din localtime)
time.strftime("%Y %A %d %b %H:%M:%S")
time.strftime("%Y %A %d %b %H:%M:%S", time.gmtime())
print(time.strftime("%I:%M:%S %p"))  # 12 hour format
print(time.strftime("%H.%M.%S"))  # 24 hour format
print(time.strftime("%d/%m/%Y", time.gmtime()))  # zi/luna/an
print(time.strftime("%Y-%m-%d"))  # aaaa-ll-zz


# transforma string in struct_time
time.strptime("30 11.00", "%d %m.%y")
time.strptime('Jan-1970 01 14.53.25', '%b-%Y %d %H.%M.%S')


# Diferenta dintre doua date(datetime)
a = time.time()   # current time in second (nr de secunde scurse de la 01.01.1970 00:00:00)
b = time.mktime((2000+20, 3+5, 2, 9, 54, 59, 3, 171, 1))  # acelasi lucru din cele 9 elemente componente

dif = float('{:f}'.format(a - b))  # cu 6 zecimale la secunda
print(dif)
print('{:.0f}'.format(dif))  # fara zecimale


# puteti reda diferenta cu o functie
def sec_to_time(time_in_second):
    ore = int(time_in_second // 3600)
    dif = int(time_in_second % 3600)
    min = int(dif // 60)
    sec = int(dif % 60)
    zile = int(ore // 24)
    rest_ore = int(ore % 24)
    return {"zile": zile, "ore": rest_ore, "minute": min, "secunde": sec}

sec_to_time(a-b)

# alte functii
time.ctime(a)  # transforma din secunde Epoch in string
time.gmtime(b)  # transforma din secunde Epoch in struct_time GMT
time.localtime(a)  # idem LOCAL


# scriere/citire din fisiere text
xx = time.strftime('%d.%m.%Y', time.localtime())
yy = open(xx + '.txt', 'w')
yy.write(f'Astazi ploua cu soare {time.strftime("%A %d %B")}')
yy.close()

zz = open(xx + '.txt', 'r')
zz.read()
zz.close()


# new - optional
def adauga_zile(data_referinta, zile_adaugate):
   noua_data = time.strftime("%Y-%m-%d",time.localtime(time.mktime(time.strptime
                    (data_referinta,"%Y-%m-%d"))+zile_adaugate*3600*24+3600))
   return noua_data

adauga_zile('2021-06-01', 14)
