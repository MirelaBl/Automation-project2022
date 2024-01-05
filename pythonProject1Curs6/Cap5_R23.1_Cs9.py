# 523.1 Clase
# Clase -  aplicatie stoc marfa
# PF - 12/10/2017

'''
Rescrieti aplicatia de la Exercitiul 521 astfel:
    In loc de trei dictionare folositi doar un dictionar, care la valori va avea
    informatiile fiecarei tranzactii astfel
        Ex:  ds = {1: {'20170101', 100, 0}, 2: {'20170103', 0, 29} }
                      {data, intrare, iesire}
  - o metoda intrari cu
        - cantitatea,
        - data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )
        - testati daca exista chei in dictionarul cu data op. Daca exista stabileste cheia curenta
        ca fiind maximul cheilor existente plus 1, altfel va fi egala cu 1
        - introduce in dict datele operatiunii (va introduce zero la iesiri)
        - actualizeaza soldul

  - o metoda iesiri, similara cu precedenta. Diferente: (va introduce zero la intrari)

  - o metoda fisa produsului cu urmatoarele specificatii:
        - Sa printeze 'Fisa produsului "denumire_produs"' (sa stim si noi a cui e fisa)
        - Sa printeze ' Nrc ', '  Data  ', ' Intrare', ' Iesire' pentru toate tranzactiile produsului
        - Sa printeze stocul actual al produsului
        - pentru avansati - aliniati coloanele

Creati trei instante (produse). Pentru 2 din ele efectuati cate 4-5 operatiuni (intrari, iesiri)

Apelati metoda fisa produsului pentru cele 2 produse
''' #

from datetime import datetime
from prettytable import PrettyTable

class Stoc:

    def __init__(self, denp, categ, um = 'kg', sold = 0):
        self.denp = denp
        self.categ = categ
        self.um = um
        self.sold = sold
        self.dict_op = {}

    def genereaza_cheia(self):
        if self.dict_op:
           c = max(self.dict_op.keys()) + 1
        else:
            c = 1
        return c

    def intrari(self, cant, data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )):
        cheie = self.genereaza_cheia()
        self.dict_op[cheie] = [data, cant, 0]
        self.sold += cant

    def iesiri(self, cant, data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )):
        cheie = self.genereaza_cheia()
        self.dict_op[cheie] = [data, 0, cant]
        self.sold -= cant

    def fisap(self):
        print('Fisa produsului {0}, {1}'.format(self.denp, self.um))
        listeaza = PrettyTable()
        listeaza.field_names = ['Nrc', 'Data', 'Intrare', 'Iesire']
        for k, v in self.dict_op.items():
            listeaza.add_row([k, v[0], v[1], v[2]])
        listeaza.add_row(['------','----------','---------','--------'])
        listeaza.add_row(['Sold', 'final', self.denp, self.sold])
        print(listeaza)


bere = Stoc('bere', 'alimente', 'sticla')

bere.intrari(100, '20181225')
bere.iesiri(72, '20181231')
bere.intrari(150)
bere.iesiri(143)
bere.__dict__
bere.fisap()

alune = Stoc('alune','alune' )

alune.intrari(165, '20191010')
alune.iesiri(123)

alune.fisap()