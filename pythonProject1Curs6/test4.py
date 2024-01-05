class Autoturism():
    nr_roti = 4

    def __init__(self, marca, model, comb, jenti, culoare = 'Alb'):
        self.marca = marca
        self.model = model
        self.comb = comb
        self.jenti = jenti
        self.culoare = culoare

    def siguranta(self, abs = 1, esp = 0):
        self.abs =abs
        self.esp = esp

    def optionale(self, **optionale):
        for i,j in optionale.items():
            self.__dict__[i] = j

    def modifica_nr_roti(self, nr):
        self.nr_roti = nr


Logan = Autoturism('Dacia', 'Logan', 'Hibryd', 'Otel', 'Verde')

Logan.siguranta()

Logan.optionale( **{'aercond' : 1, 'navigatie' : 0} )

Logan.__dict__
