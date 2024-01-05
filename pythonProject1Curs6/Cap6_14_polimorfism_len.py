"""
614 OOP  
Polimorfism - len
PF - 08.06.2021 v5
"""  #

class Carte:

    def __init__(self, titlu, autor, pagini):  # "constructor"
        print("O noua carte")
        self.titlu = titlu
        self.autor = autor
        self.pagini = pagini

    def __str__(self):  # printare
        return "Titlu: {0}, Autor: {1}, Pagini: {2} ".format(self.titlu, self.autor, self.pagini)

    def __del__(self):  # destructor
        print("Cartea {0} a fost casata".format(self.titlu))

    def __len__(self):
        return self.pagini


HdC = Carte("Hotul de Carti", "Markus Zusak", 573)

print(HdC)
len(HdC)
del HdC
