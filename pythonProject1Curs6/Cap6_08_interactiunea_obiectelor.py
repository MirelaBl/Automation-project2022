"""
608 OOP  
Interactiunea obiectelor din clase diferite
PF - 08.06.2021 v5
"""  #

class A:

    def aduna(self, *diferiti_parametri):
        suma = sum(diferiti_parametri)
        return suma

class B:

    def inmulteste(self, x, y):
        return x * y

b = B()
a = A()

print(b.inmulteste(a.aduna(3, 7, 2, 105, 987), b.inmulteste(15,28)))

a.aduna(b.inmulteste(15,28), 5,)


# alt exemplu
class Persoana:
    """Clasa persoana"""

    def __init__(self, nume, prenume):
        """Atribute persoana"""
        self.nume = nume
        self.prenume = prenume


class Firma:
    """Clasa firma"""

    def __init__(self, nume, director: Persoana):
        """Atribute firma
        Diectorul este un obiect de tip persoana
        """
        self.nume = nume
        self.director = director

cristina = Persoana('Dobrin', 'Cristina')
alfa = Firma('Alfa', cristina)

print(alfa.nume)
print(alfa.director.nume)
print(alfa.director.prenume)
print(alfa.__dict__)
print(alfa.director.__dict__)
