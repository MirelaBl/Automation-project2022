"""R153 Numere
Lucrul cu numere
PF - 2020-04-13 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=trailing-whitespace
# pylint: disable=pointless-string-statement

print("\n\tExercitii numere\n")

# Se dau 2 numere, 13 si 7. efectuati urmatoarele operatiuni:

#		adunare
print(13 + 7)
# 		scadere
print(13 - 7)
# 		inmultire
print(13 * 7)
# 		impartire int (exacta)
print(13 / 7)
# 		modulo
print(13 % 7)
#       ridicarea la putere
print(13 ** 7)

#   Calculati 5 + { 20 - [(14 - 6) x 2 - 7] }
print(5 + (20 - ((14 - 6) * 2 - 7)))

# 	Conversii de numere

# transforma '50' in numar in baza 10. Incearca si din baza 16
print(int('50'))
print(int('50', 16))

# transforma numarul 5e16 (notatie stiintifica) in int
int(5e16)

# transforma numarul din baza 16, 'fb1' in int
int('fb1', 16)

# transforma '10.7' in intreg
int(float('10.7'))

input("\n\nApasa <enter> pt a iesi.")
