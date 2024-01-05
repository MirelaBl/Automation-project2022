from datetime import datetime
from prettytable import PrettyTable

class Stoc():

    lista_prod = []

    def __init__(self, denp, categ, um = 'kg', sold = 0):
        self.denp = denp
        self.categ = categ
        self.um = um
        self.sold = sold
        self.dict_op = {}
        self.lista_prod.append(denp)

    def genereaza_cheia(self):
        if self.dict_op:
            cheie = max(self.dict_op.keys()) + 1
        else:
            cheie = 1
        return cheie


    def input(self, cant, data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )):
        cheia = self.genereaza_cheia()
        self.dict_op[cheia] = [data, cant, 0]
        self.sold += cant

    def output(self, cant, data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )):
        cheia = self.genereaza_cheia()
        self.dict_op[cheia] = [data, 0, cant]
        self.sold -= cant

    def fisap(self):
        print('Fisa produsului {0}, {1}'.format(self.denp, self.um))
        listeaza = PrettyTable()
        listeaza.field_names = ['Nrc', 'Data', 'Intrare', 'Iesire']
        for k, v in self.dict_op.items():
            listeaza.add_row([k, v[0], v[1], v[2]])
        listeaza.add_row(['Stoc', 'actual', '', self.sold])

        print(listeaza)

miere = Stoc('miere', 'alimente')
miere.input(100, '20191223')
miere.output(72, '20191228')
miere.input(150)
miere.output(113)

miere.fisap()

miere.__dict__


gem = Stoc('gem', 'alimente')

gem.input(156)
gem.output(117)

gem.fisap()

for i in Stoc.lista_prod:
    eval(i).fisap()