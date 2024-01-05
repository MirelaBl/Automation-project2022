"""
458
Crearea unei functii simple
PF 16.12.2020 v4
"""  #

import sys

# pylint: disable=invalid-name
# pylint: disable=unidiomatic-typecheck

enunt = """Sa se realizeze un program cu o functie care sa caute
cuvinte in fisierul dat de utilizator cu ajutorul (try-except)
Functia trebuie sa afiseze linia unde gaseste cuvantul respectiv."""

def cauta_cuv(fisier, cuvant):
    """Cauta cuvinte"""
    try:
        file = open(fisier)
    except FileNotFoundError:
        print('Eroare:', sys.exc_info()[0])
        print('Mesaj:', sys.exc_info()[1])
        print("Nu se poate deschide fisierul ", str(fisier))
    else:
        print("Fisierul urmator a fost dechis: ", str(fisier))
        text = file.readlines()
        if type(cuvant) == str:
            for line in text:
                if line.find(cuvant) != -1:
                    print(line)
        else:
            print("Cuvant nu este sir de caractere")
        file.close()
    print("\n")

cauta_cuv("c:/_wt/guta.txt", "Guta")
cauta_cuv("c:/_wt/guta.txt", "gagauta")
cauta_cuv("c:/_wt/guta.txt", "si")

input("\n\nApasa enter pt. a iesi")
