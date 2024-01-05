"""
623 Clase avansat  
Pizza - mostenire
PF - 08.06.2021 v5
"""  #


class Pizza():
    """ Superclasa """

    timp_coacere = 12

    lista_bauturi = {'apa': 5, 'cola': 8, 'suc_mere' : 12, 'limonada': 15}   # pret
    dimensiuni = {"mare": 1.5, "medie": 1.2, "mica": 1}  # coeficient pret pe dimensiuni
    blaturi = {"crocant": 6, "subtire": 5, "pufos": 7}  # pret
    pret_baza_toping = 2  # pret pentru o pizza mica, se aplica cof de dimensiune

    def __init__(self):
        self.ingrediente = list()
        self.bautura_comandata = []
        self.dimensiune = 'medie'
        self.blat = 'crocant'
        self.pret_blat = 0
        self.pret_ingrediente = 0
        self.pret_pizza = 0

    # schimba caracteristici
    def schimba_dimensiune(self):
        dim = input('Introduceti "mica", "medie" sau "mare"').lower()
        if dim in self.dimensiuni:
            self.dimensiune = dim

    def schimba_blat(self):
        blat = input('Introduceti "crocant", "subtire", "pufos"').lower()
        if blat in self.blaturi:
            self.blat = blat

    def adauga_ingrediente(self, *lista):
        self.ingrediente.extend(lista)

    def adauga_bautura(self):
        while True:
            bautura = input("'apa': 5 lei, 'cola': 8 lei, 'suc_mere' : 12 lei,'limonada': 15 lei")
            if bautura == '':
                break
            elif bautura in self.lista_bauturi:
                self.bautura_comandata.append(bautura)
            else:
                print(f'Nu avem {bautura}')

    # calculatii
    def pret_bauturi(self):
        self.pret_bautura = 0
        if self.bautura_comandata:
            for i in self.bautura_comandata:
                self.pret_bautura += self.lista_bauturi[i]

    def pret_baza_blat(self):
        self.pret_blat = self.blaturi[self.blat]

    def pret_baza_ingrediente(self):
        self.pret_ingrediente = len(self.ingrediente) * self.pret_baza_toping

    def pret_pizza_total(self):
        self.pret_baza_blat()
        self.pret_baza_ingrediente()
        self.pret_pizza = (self.pret_blat + self.pret_ingrediente) \
                          * self.dimensiuni[self.dimensiune]

    def calculeaza(self):
        self.pret_bauturi()
        self.pret_pizza_total()

    def __str__(self):
        self.calculeaza()
        result = f"""        Bautura: {self.pret_bautura}
        Pizza: {self.pret_pizza}
        --------------------------------
        Total: {self.pret_pizza + self.pret_bautura}
        """
        return result


class Pizza_vegan(Pizza):
    sos = 'dulce'
    timp_coacere = 15

    def __init__(self):
        super().__init__()
        self.ingrediente.extend(['rosii', 'masline', 'ciuperci'])


class Pizza_branzeturi(Pizza):

    sos = 'ceapa'

    def __init__(self):
        super().__init__()
        self.ingrediente.extend(['m','rb', 'rw'])


class Pizza_carnivora(Pizza):

    sos = 'mustar'

    def __init__(self):
        super().__init__()
        self.ingrediente.extend(['pui', 'bacon', 'vita'])

# instantiem
carniv1 = Pizza_carnivora()

print(carniv1.__dict__)
carniv1.adauga_bautura()
carniv1.adauga_bautura()

carniv1.adauga_ingrediente('carne', 'carne', 'ciuperci')
print(carniv1.ingrediente)

carniv1.schimba_dimensiune()
print(carniv1.dimensiune)

print(carniv1)

# instantiem
vegan = Pizza_vegan()
vegan.adauga_ingrediente('rozmarin', 'dovlecel')
vegan.schimba_dimensiune()
vegan.schimba_blat()
vegan.adauga_bautura()

print(vegan)

print(vegan.__dict__)

