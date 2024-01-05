"""
613 OOP  
Mostenire init
PF - 08.06.2021 v5
"""  #

# mostenira obisnuita
class jucarii:

    def __init__(self, categorie, dimensiuni):
        self.categorie = categorie
        self.dimensiuni = dimensiuni

class valoare:

    def __init__(self, pret = 1000):
        self.pret = pret

    def ceva(self):
        print('ceva')

class papusi(jucarii, valoare):

    def __init__(self, nume = 'Barbie', **parent):
        self.nume = nume
        super().__init__(**parent)

parametri = {'categorie': '5-8 ani', 'dimensiuni': 50 }

p1 = papusi('Aradeanca', **parametri)
p2 = papusi(categorie='8-11 ani', dimensiuni=25)
print(p1.nume)
print(p1.categorie)
print(p1.pret)
p1.ceva()
print(p1.dimensiuni)
print(p2.__dict__)

isinstance(p1, valoare)
issubclass(papusi, jucarii)

















# exceptia, mostenire multipla init
class jucarii:
    def __init__(self, categorie = 'ceva'):
        super(jucarii, self).__init__()
        self.categorie = categorie

class valoare:
    def __init__(self, pret = 1000):
        super(valoare, self).__init__()
        self.pret = pret

class papusi(jucarii, valoare):
    def __init__(self, categorie, nume = 'Barbie'):
        super(papusi, self).__init__(categorie)
        self.nume = nume


p1 = papusi('10+')
print(p1.__dict__)
print(p1.nume)
print(p1.categorie)
print(p1.pret)
