""" 208 IF
if if ... else
PF - 20.07.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement


from random import randint

nota = randint(1, 11)

if nota >= 5:
    print('promovat')
else:
    print('nepromovat')

input('Apasa <enter> pt a iesi')
