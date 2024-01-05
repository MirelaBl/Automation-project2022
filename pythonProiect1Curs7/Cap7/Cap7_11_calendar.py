"""
711 Module
Modulul calendar
PF - 15.06.2021 v6
"""  #


import calendar


print(calendar.mdays)  # returneaza numarul de zile al lunilor anului
calendar.weekday(2021, 5, 6)  # numarul zilei (0 LUNI - 6)

print(calendar.day_name[1])	 # numele zilei
print(calendar.day_abbr[1])  # numele abreviat al zilei
print(calendar.month_name[3])  # numele lunii
print(calendar.month_abbr[3]) 	# numele abreviat al lunii

calendar.isleap(2100)  # testeaza an bisect
calendar.leapdays(2021, 2100)  # numarul de zile de 29 Feb in perioada (ani bisecti)

calendar.monthcalendar(2021, 3)  # liste cu zilele grupate pe saptamani

print(calendar.month(2023, 3))  # calendarul desfasurat luna
print(calendar.prcal(2023))  # calendarul desfasurat an
calendar.setfirstweekday(0)  # weekday(0 is Monday, 6 is Sunday) - schmba prima zi

luni = {x: calendar.month_name[x] for x in range(1, 13)}  # dictionar cu lunile anului
print(luni)

saptamana = {x: calendar.day_name[x] for x in range(7)}  # dictionar cu zilele saptamanii
print(saptamana)

import calendar
from calendar import HTMLCalendar
cal = calendar.LocaleHTMLCalendar(locale='ro_RO')
cal.formatweekday(4)
cal.formatmonthname(2020,9,25)
