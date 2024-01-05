class Academie():
    def examen(self):
        print('Admis')

class Studenti(Academie):
    pass

obj = Studenti()
obj.examen()
