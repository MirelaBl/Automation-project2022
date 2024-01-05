"""
121
Op aritm / math in Python
PF - 2020-04-13 v4
"""  #

"""1.	Scrie o instructiune print care sa efectueze operatiunile: (7 + 3)(2)""" #
# scrie codul aici:
print(pow((7+3),2))

"""3.	Aria cercului este: pi * raza². Scrie un program in care raza  va fi introdusa de la 
tastatura cu input() si va afisa aria cercului. Atentie, pentru a putea utiliza constanta pi
rulati mai intai linia de cod: from math import pi, scrisa deja mai jos"""

# scrie codul aici:
from math import pi
print('introdu raza')
raza = int(input())
raza = pow(int(raza),2)
print('pi este: '+ str(pi))
print('raza este: '+str(raza))
a = pi * raza
print('aria este: '+str(a))


"""2.	Suma numerelor de la 1 la n este data de expresia:  n(n+1)/2 . Scrie un program in care
n va fi introdus de la tastatura cu input() si va afisa (print) suma numerelor de la 1 la n"""
# scrie codul aici:

n = int(input("Enter number"))
sum = 0
# loop from 1 to n
for num in range(0, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)



m = int(input('intordu numarul'))
suminit= 0
for b in range(1,int(m+1)):
    suminit = suminit+b

print("Sum of first ", m, "numbers is: ", suminit)

a=int(input("Enter number a: "))

b = a+1

c = int(a*b/2)
print("Sum of first ", a, "numbers is: ", c)

x = float(input('intordu numarul x'))
print(int(x*(x+1)/2))



