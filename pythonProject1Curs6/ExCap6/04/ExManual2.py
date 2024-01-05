class Persoana:

    def __init__(self,nume, prenume):
        self.nume = nume
        self.prenume = prenume

class Firma:

    def __init__(self, nume_firma, director:Persoana):
        self.nume_firma = nume_firma
        self.director = director

maria = Persoana('Pop','Maria')
alfa = Firma('Alfa',maria)

print(alfa.nume_firma)
print(alfa.director.nume)
print(alfa.director.prenume)
print('********************************')
maria = Persoana('Lena','Marin')

persoane = [maria, Persoana("Vasile","Vasilache"),Persoana("Nenitzescu","neni")]

for i in persoane:
    print(i.prenume)
    