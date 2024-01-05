class People:
    """Atribut clasa / atribut obiect - continuare"""

    an_studiu = {'Anul 1', 'Anul 2', 'Anul 3', 'Anul 4', 'Anul 5'}
    facultate = {'Inginerie', 'Drept', 'Finante', 'Geografie'}

    def __init__(self,nume, anul, facultatea):
        if anul in People.an_studiu:
            self.anul = anul
        else:
            raise NameError ( 'An incorect')
        if facultatea in People.facultate:
            self.facultatea = facultatea
        else:
            raise NameError ( 'Fac incorecta')
        self.nume = nume


    def __str__(self):
        result = self.nume + " este in "+ self.anul+" anul la facultatea de "+ self.facultatea + "."
        return result


student1= People("vaisile popa","Anul 5", "Drept")
print(student1)