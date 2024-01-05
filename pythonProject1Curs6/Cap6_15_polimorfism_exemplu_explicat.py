"""
615 OOP  
Polimorfism - exemplu explicat
PF - 08.06.2021 v5
"""  #

class Electrocasnice:

    def __init__(self, nume):
        self.nume = nume

    def caracteristici(self, *lista):
        raise NotImplementedError("Metoda abstracta - se defineste in subclasa")

    def __str__(self):
        caracteristici_listate = ''
        for k, v in self.__dict__.items():
            caracteristici_listate += str(k).ljust(15) + ': ' + str(v) + '\n'
        return caracteristici_listate


class Aragaz(Electrocasnice):

    def caracteristici(self, combustibil='Gaz', numar_ochiuri=4, culoare='Negru', provenienta='Romania'):
        self.numar_ochiuri = numar_ochiuri
        self.culoare = culoare
        self.provenienta = provenienta
        self.combustibil = combustibil


class Televizor(Electrocasnice):

    def caracteristici(self, diagonala=101, ecran='led', tip_ecran='plat', culoare='Negru'):
        self.diagonala = diagonala
        self.culoare = culoare
        self.ecran = ecran
        self.tip_ecran = tip_ecran


class Sobe(Electrocasnice):

    def caracteristici(self, constructie='Metal', combustibil='Gaz', culoare='Maro'):
        self.culoare = culoare
        self.constructie = constructie
        self.combustibil = combustibil

class test(Electrocasnice):
    pass

a = Aragaz('Aragaz cu 4 ochiuri')
a.caracteristici()
a.__dict__


t = Televizor('Televizor diag 101')
t.caracteristici()

t1 = Televizor('lx_100')
t1.caracteristici(207, 'led_albastru', 'curbat', 'verde')

s = Sobe('Soba din teracota pe lemne')
s.caracteristici('teracota', 'lemn')

test_obj = test('test')
test_obj.caracteristici('ceva')

print(a)
print(t)
print(t1)
print(s)

for i in (a, t, t1, s):
    print(i)

