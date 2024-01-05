

class Academie():
    def __examen(self):
        print('Admis')
    def proba(self):
        self.__examen()

obj = Academie()
#obj.__examen()

obj.proba()
obj.__examen()