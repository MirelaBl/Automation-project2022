"""
625 Clase avansat  
Mostenire - Persoana
PF - 13.06.2021 v5
"""  #


class Adrese():

    def atr_adresa(self, oras, judet, strada, nr):
        self.adresa = {'oras': oras, 'judet': judet, 'strada': strada, 'nr': nr}

    def are_email(self, email):
        self.email = email


class Persoana(Adrese):

    def __init__(self, nume, varsta, sex):
        self.nume = nume
        self.varsta = varsta
        self.sex = sex


class Student(Persoana):

    def __init__(self, facultate, an, **parent):
        super().__init__(**parent)
        self.facultate = facultate
        self.an = an

    def atr_specializare(self, specializare):
        self.specializare = specializare

    def catalog(self):
        self.note = {}

    def pune_nota(self, materia, nota):
        self.note[materia] = nota


class Medic(Persoana):

    def tip_medic(self, tip):
        self.tip = tip

    def atr_specializare(self, specializare):
        self.specializare = specializare


class Rezident(Medic):

    def __init__(self, spital, **parent):
        self.spital = spital
        super().__init__(**parent)

# studenti
student1 = Student('Arte', 2, nume='Vasile', varsta=25, sex='m')

student1.atr_adresa('Cluj-Napoca', 'Cluj', 'Frumoasa', 5)
student1.are_email('vasile@ro.ro')
student1.atr_specializare('electrotehnica')
student1.catalog()
student1.pune_nota('Mate', 10)

print(student1.__dict__)

# medici
medic1 = Medic('Ana', 29, 'f')

medic1.tip_medic('primar')
medic1.atr_specializare('pediatrie')
medic1.are_email('Ana@medic.ro')

print(medic1.__dict__)

# rezidenti
rezident1 = Rezident('Universitar', nume='Mariana', varsta=27, sex='f')

print(rezident1.__dict__)
isinstance(rezident1, Persoana)

# adrese


class Firma(Adrese):

    def __init__(self, nume_firma, cui):
        self.nume = nume_firma
        self.cui = cui

firma1 = Firma('Alfa', 12345678)
print(firma1.__dict__)

firma1.atr_adresa('Oradea', 'Bihor', 'Galbena', 1)
firma1.are_email('office@alfa.ro')


# dupa refactoring

persoana1 = Persoana('Popa', 15, 'f')
print(persoana1.__dict__)
persoana1.atr_adresa('Zalau', 'Salaj', 'Vesela', 7)

student2 = Student('chimie', 3, nume='Cristina', varsta=25, sex='f')
student2.are_email("cristina@email.ro")
print(student2.__dict__)

firma2 = Firma('Beta', 89756421)
firma2.atr_adresa('Zimnice', 'Teleorman', 'Corabiei', 7)
firma2.are_email('beta@firma.ro')
firma2.__dict__