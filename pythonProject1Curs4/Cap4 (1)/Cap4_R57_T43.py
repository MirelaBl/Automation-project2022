"""
457
Crearea unei functii simple
PF 22.09.2020 v4
"""  #

# pylint: disable=invalid-name

enunt = """Creati un program cu o functie care sa poata cauta cuvinte intr-un text"""

def cauta_cuv(cuv, text):
    text_s = text.split(' ')
    for e in text_s:
        if e == cuv:
            return True

fisier = open("c:/_wt/guta.txt")

fisier.seek(0)
cauta_cuv('vorba', fisier.read())



fisier.close()

input("\n\nApasa enter pt. a iesi")
