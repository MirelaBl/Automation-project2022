"""
R154
Variabile
PF - 2020-04-13 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=trailing-whitespace
# pylint: disable=pointless-string-statement

#	atribuire de valoare unei variabile. Variabila i => InfoAcademy
i = 'InfoAcademy'

#	atribuire de valoare mai multor variabile. Variabilele p => Python , c => Cursul
p, c = 'Python', 'Cursul'

#	Concatenare. Variabila a => Cursul de Python se tine la InfoAcademy,
#	  utilizand variabilele precedente. Printati toate variabilele
print('i este pentru:', i, '\np este pentru:', p, '\nc este pentru:', c)
a = c + ' de ' + p + ' se tine la ' + i
print(a)

# 	Se dau variabilele x = 7, y = 3, z = 2.0. Utilizati-le (inclusiv printare)
# 		in operatiunile urmatoare:
x = 7
y = 3
z = 2.0

#	incrementare

x += y
print(x)

#	decrementare

x -= y
print(x)

#	inmultire

x *= y
print(x)

#	impartire

print((x + y)/z)

input("Apasa <enter> pt a iesi.")
