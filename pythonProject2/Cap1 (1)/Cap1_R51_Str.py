# R151 Stringuri
# Concatenarea si repetitia unui sir de caractere
# PF - 2020-04-13 v4

# pylint: disable=invalid-name
# pylint: disable=trailing-whitespace
# pylint: disable=pointless-string-statement

"""Creati un program care sa scrie numerele de telefon urmatoare folosind multiplicarea 
si concatenarea: 0744 123 123 ; 07 222 55 222; 07 88888888. 
Scrieti de 7 ori: Astazi este o zi frumoasa!
"""	#

print('07' + 2 * '4' + 2 * '123')

print("07" + 3 * "2" + 2 * "5" + 3 * "2")

print('07' + 8 * '8')

print(7 * 'Astazi este o zi frumoasa! ')

input("\n\nApasa <enter> pt a iesi.")
