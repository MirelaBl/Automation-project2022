"""
621 Clase avansat  
Stoc mostenit
PF - 08.06.2021 v5
"""  #

enunt = """
Programul creat la exercitiul 521 va fi considerat o superclasa (Stoc).
 Creati 2-3 subclase magazin1, 2, .... Fiecare subclasa va avea si 1-2 metode proprii
  
 Creati trei instante (produse). Pentru 2 din ele efecturati cate 4-5 operatiuni (intrari, iesiri)
 Apelati metoda fisa produsului pentru cele 2 produse.
 Apelati celelalte metode noi.
"""  #


from datetime import datetime
from prettytable import PrettyTable

class Stoc:
    """Despre gestiunea produselor"""

    categorii = {}

    def __init__(self, denp, categ, um='buc', sold=0):
        """metoda constructor"""
        self.denp = denp
        self.categ = categ
        self.um = um
        self.sold = sold
        self.do = {}
        if categ in Stoc.categorii:
            self.categorii[categ] += [denp]
        else:
            self.categorii[categ] = [denp]

    def gen_cheia(self):
        if self.do:
            cheia = max(self.do.keys()) + 1
        else:
            cheia = 1
        return cheia

    def intrari(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        cheia = self.gen_cheia()
        self.do[cheia] = [data, cant, 0]
        self.sold += cant

    def iesiri(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        cheia = self.gen_cheia()
        if self.sold < cant:
            cant = self.sold
        self.do[cheia] = [data, 0, cant]
        self.sold -= cant

    def fisap(self):
        print(f'Fisa produsului {self.denp} {self.um}')
        listeaza = PrettyTable()
        listeaza.field_names= ['Nrc', 'Data', 'Intrare', 'Iesire']
        for k, v in self.do.items():
            listeaza.add_row([k, v[0], v[1], v[2]])
        print(listeaza)
        print('Stoc final: ', self.sold)


class DepNou(Stoc):

    def perisabilitati(self, procent):
        rulaj = 0
        for i in self.do.values():
            rulaj += i[1]
        scazaminte = rulaj * procent / 100
        self.iesiri(scazaminte)

    def val_stoc(self, pret):
        valoare = self.sold * pret
        return valoare

cuie = DepNou('cuie', 'metal', 'kg')
print(cuie.__dict__)

cuie.intrari(100, '20210303')
cuie.iesiri(23, '20210305')
cuie.iesiri(41, '20210405')
cuie.intrari(50)
cuie.iesiri(57)

print(cuie.__dict__)

cuie.fisap()
print(cuie.categorii)

cuie.val_stoc(7)
cuie.perisabilitati(.5)