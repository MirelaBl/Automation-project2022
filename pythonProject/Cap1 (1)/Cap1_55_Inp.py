"""
155
Input
PF - 2020-04-13 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=trailing-whitespace
# pylint: disable=pointless-string-statement

""" Creati un program care sa va solicite numele de la tastatura (input) si sa returneze:
        Salut (nume)! O zi frumoasa!
""" #
print('introdu nume:')
nume = input()
print( 'Salut ' +nume+'!O zi frumoasa!')
""" Creati un program care in care sa introduceti de la tastatura doua numere n1, n2 
    si sa returneze media aritmetica (n1 + n2)/2"""
print('introdu n1:')
n1 = int(input())
print('introdu n2:')
n2 = int(input())
media = float((n1+n2)/2)
print( media)

input("\n\nApasa <enter> pt a iesi.")
