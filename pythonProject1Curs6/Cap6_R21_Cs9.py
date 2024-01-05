"""
621 Clase avansat  
Stoc mostenit
PF - 08.06.2021 v5
"""  #

"""
 importati functia datetime din modulul datetime. Instructiune scrisa deja (vezi mai jos)          #
 Initializati o variabila 'cheie' care va da cheile unor dictionare, cu valoarea 1(vezi mai jos)   #
 Creati o clasa 'Stoc' care va avea:                                                               #
 - 2 variabile statice, care sa numere cate produse avem si cate categorii (doar pentru avansati)  #
 - o metoda constructor cu                                                                         #
 denumire produs                                                                                   #
 categoria                                                                                         #
 unitatea de masura default 'Buc'                                                                  #
 sold default 0                                                                                    #
 initializati trei dictionate, cu cheie comuna, pentru data op., intrari si iesiri din stoc        #
 - o metoda intrari cu                                                                             #
 cantitatea,                                                                                       #
 data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )                                             #
 definiti cheia ca variabila globala                                                               #
 testati daca cheia se gaseste in dictionarul cu data op. Daca exista stabileste cheia             #
 ca fiind maximul cheilor existente plus 1, altfel va fi egala cu 1                                #
 introduce in dict intrari cheie si cant                                                           #
 introduce in dict data cheie si data op                                                           #
 actualizeaza soldul                                                                               #
 - o metoda iesiri, similara cu precedenta. Diferente: populam dict iesiri                         #
 - o metoda fisa produsului cu urmatoarele specificatii:                                           #
 Sa printeze 'Fisa produsului "denumire_produs"' (sa stim si noi a cui e fisa)                     #
 Sa printeze ' Nrc ', '  Data  ', ' Intrare', ' Iesire' pentru toate tranzactiile produsului       #
 Sa printeze stocul actual al produsului                                                           #
 pentru avansati - aliniati coloanele                                                              #
 Creati trei instante (produse). Pentru 2 din ele efecturati cate 4-5 operatiuni (intrari, iesiri) #
 Apelati metoda fisa produsului pentru cele 2 produse                                              #
"""  #

from datetime import datetime

class Stoc:
    """Tine stocul unui depozit"""
    tot_categ = 0
    tot_prod = 0
    categorii = list()
    produse = list()
    categ_prod = {}

    def __init__(self, prod, categ, um='Buc', sold=0):
        self.prod = prod  # parametri cu valori default ii lasam la sfarsitul listei
        self.categ = categ  # fiecare instanta va fi creata obligatoriu cu primii trei param.
        self.sold = sold  # al patrulea e optional, soldul va fi zero
        self.um = um
        self.i = {}  # fiecare instanta va avea trei dictionare intrari, iesiri, data
        self.e = {}  # pentru mentinerea corelatiilor cheia operatiunii va fi unica
        self.d = {}
        Stoc.tot_prod += 1  # la fiecare instantiere se calculeaza numarul produselor si al categ
        Stoc.produse.append(prod)  # populam lista cu produse

        if categ not in Stoc.categorii:  # populam lista cu categorii, daca nu exista (unicitate)
            Stoc.tot_categ += 1
            Stoc.categorii.append(categ)
            Stoc.categ_prod[categ] = {prod}
        else:
            Stoc.categ_prod[categ].add(prod)

    def intr(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.sold += cant  # recalculam soldul dupa fiecare tranzactie
        if self.d.keys():  # dictionarul data are toate cheile (fiecare tranzactie are data)
            cheie = max(self.d.keys()) + 1
        else:
            cheie = 1
        self.i[cheie] = cant  # introducem valorile in dictionarele de intrari si data
        self.d[cheie] = data

    def iesi(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.sold -= cant
        if self.d.keys():
            cheie = max(self.d.keys()) + 1
        else:
            cheie = 1
        self.e[cheie] = cant  # similar, introducem datele in dictionarele iesiri si data
        self.d[cheie] = data

    def fisap(self):

        print('Fisa produsului ' + self.prod + ': ' + self.um)
        print('----------------------------')
        print(' Nrc ', '  Data ', 'Intrari', 'Iesiri')
        print('----------------------------')
        for v in self.d.keys():
            if v in self.i.keys():
                print(str(v).rjust(5), self.d[v], str(self.i[v]).rjust(6), str(0).rjust(6))
            else:
                print(str(v).rjust(5), self.d[v], str(0).rjust(6), str(self.e[v]).rjust(6))
        print('----------------------------')
        print('Stoc actual       ' + str(self.sold).rjust(10))
        print('----------------------------\n')


fragute = Stoc('fragute', 'fructe', 'kg')  # cream instantele clasei
lapte = Stoc('lapte', 'lactate', 'litru')
ceasuri = Stoc('ceasuri', 'ceasuri')

print(fragute.sold)  # ATRIBUTE
fragute.intr(100)
fragute.iesi(73)
fragute.intr(100)
fragute.iesi(85)
fragute.intr(100)
fragute.iesi(101)

print(fragute.d)  # dictinarele produsului cu informatii specializate
print(fragute.i)
print(fragute.e)

print(fragute.sold)
print(fragute.tot_categ)
print(fragute.categ)
print(fragute.prod)
print(fragute.tot_prod)
print(fragute.um)
print(fragute.categorii)
print(fragute.categ_prod)

fragute.fisap()

lapte.intr(1500)
lapte.iesi(975)
lapte.intr(1200)
lapte.iesi(1490)
lapte.intr(1000)
lapte.iesi(1200)

lapte.fisap()

for i in Stoc.produse:
    print(i)
    globals()[i].fisap()
    print(globals()[i])

# Mostenire

class Mag1(Stoc):
    """Subclasa a clasei Stoc"""

    def __init__(self, pro, cat, uni, x, y, z=7):
        self.x = x
        self.y = y
        super().__init__(pro, cat, uni)

    def perisabilitati(self, procent):
        """Calculeaza valoarea perisabilitatilor si o scade din sold (iesire)"""
        s = 0
        for k, v in self.i.items():
            s += v
        p = int(s * procent / 100 + .99)
        self.iesi(p)

    def valoare_stoc(self, pret):
        return pret * self.sold

    def cauta_tranzactii(self, data_start=str(datetime.now().strftime('%Y0101')),
                         data_final=str(datetime.now().strftime('%Y1231'))):
        if self.d != {}:
            print('Fisa produsului ' + self.prod + ': ' + self.um)
            print('----------------------------')
            print(' Nrc ', '  Data ', 'Intrari', 'Iesiri')
            print('----------------------------')
            for v in self.d.keys():
                if data_start <= self.d[v] and  data_final >= self.d[v]:
                    if v in self.i.keys():
                        print(str(v).rjust(5), self.d[v], str(self.i[v]).rjust(6), str(0).rjust(6))
                    else:
                        print(str(v).rjust(5), self.d[v], str(0).rjust(6), str(self.e[v]).rjust(6))
            print('----------------------------')
        else:
            print('Sold zero')


pepeni = Mag1('pepeni', 'fructe', 'kg', 'xpepeni', 'ypepeni')

print(pepeni.sold)

pepeni.intr(1000, '20170930')
pepeni.iesi(975, '20171230')
pepeni.intr(2500)
pepeni.intr(1800)
pepeni.iesi(3972)


pepeni.fisap()

print(pepeni.categ_prod)

for elem in Stoc.categ_prod:  # Listeaza categoriile si produsele aferente
    print('Produse in categoria: ' + elem)
    for count, val in enumerate(Stoc.categ_prod[elem]):
        print(count + 1, val)

print(fragute.categ_prod)

print(Stoc.categorii)
print(Stoc.tot_categ)
print(Stoc.tot_prod)
print(Stoc.categ_prod)

print(Mag1.produse)
print(Mag1.categorii)
print(Mag1.tot_categ)
print(Mag1.tot_prod)
print(Mag1.categ_prod)

tabla = Mag1('tabla', 'mat_constr', 'kg', 'x', 'y')

tabla.intr(1000, '20170501')
tabla.iesi(877, '20170502')
tabla.intr(1500, '20170505')
tabla.iesi(1001)
tabla.intr(500)
tabla.perisabilitati(.5)

tabla.fisap()

pepeni.fisap()

pepeni.perisabilitati(4)

fragute.fisap()

fragute.perisabilitati()

pepeni.valoare_stoc(1.2)

print(pepeni.sold)

pepeni.cauta_tranzactii()

def tranzactii(
    produs, data_start=str(datetime.now().strftime('%Y0101')),
                         data_final=str(datetime.now().strftime('%Y1231'))):
    res = globals()[produs].cauta_tranzactii(data_start, data_final)
    return res


for i in globals():
    if isinstance(globals()[i], Stoc):
        print(i)

lista = list(dicti.keys())
lista.sort()
lista.reverse()
sold = 413

pepeni.perisabilitati(2)

pepeni.cauta_tranzactii()