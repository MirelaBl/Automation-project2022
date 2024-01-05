"""
307 Lista
Lista - metode aplicabile
PF - 26.06.2020 v4
"""  #

# pylint: disable=invalid-name

# Metode aplicabile unei liste
week = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri']
print(week)
week.append('Sambata')
print(week)
week.extend(['Duminica', 'New_Day'])
print(week)
week.count('Luni')
print(week)
week.remove('New_Day')
print(week)
week.index('Joi')
week.index('Vineri')
week.pop(5)
week.insert(5, 'Sambata')
print(week)
week.reverse()
print(week)

print(week[6])

# cream o lista identica pentru a o sorta (nu schimbam ordinea in lista initiala)
week1 = week.copy()

print(week1)
week1.sort()
print(week1)
week1.reverse()

week1 = list(week)

del week1[6]  # nu este o metoda, este o functie
del week1  # ambele forme prezentate sunt utilizabile pentru del

print(max(week))
print(min(week))
lista1 = [3, 7, 13]
print(sum(lista1))  						# doar pentru elem numerice
print(sum(lista1) / len(lista1))  		    # media aritmetica


# Dublu split intr-un text
x = 'From   paul@infoacademy.net Tue May  24 22:22:22 2016'   # sirul dat

lista_cuv = x.split()           # splituim sirul in cuvinte (default dupa spatiu)
                                # rezultatul : o lista cu cuvintele (subsirurile)
print(lista_cuv)

email = lista_cuv[1]            # identificam email-ul dupa pozitia in lista
print(email)

comp = email.split('@',)        # splituim email-ul dupa "@", rezulta o alta lista
print(comp)

print('Host:', comp[0])
print('Domeniu:', 'https://www.' + comp[1])


# Enumerate - genereaza numere, cronologic, de la 0 la n-1, n fiind numarul de elemente
    # al listei primita ca parametru

for numar, luna in enumerate(['ian', 'feb', 'mar', 'apr', 'may',
	                      'iun', 'iul', 'aug', 'sep', 'oct', 'nov', 'dec'], start = 1):
    print('{:2d}'.format(numar), luna)


