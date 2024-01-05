""" 207 IF
if ... elif
PF - 20.07.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement


from random import randint

nota = randint(1, 11)

if nota == 10:
    print('foarte bine')
elif nota == 5:
    print('am trecut si de data asta!')

input('Apasa <enter> pt a iesi')
