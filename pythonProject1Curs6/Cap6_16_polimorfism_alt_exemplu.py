"""
616 OOP  
Polimorfism - alt exemplu
PF - 08.06.2021 v5
"""  #


class Electronice:
    def __init__(self, name):
        self.name = name

    def camera(self, *caracteristici):
        raise NotImplementedError("Metoda abstracta - se defineste in subclasa")

    def ecran(self, *caracteristici):
        raise NotImplementedError("Metoda abstracta - se defineste in subclasa")

class Telefon(Electronice):
    def camera(self, mpixeli = 1, model = 'NoName', culoare = 'Negru'):
        self.mpixeli = mpixeli
        self.model = model
        self.culoare = culoare

    def ecran(self, diagonala = 4, tip = 'Cristal', model = 'None'):
        self.diagonala = diagonala
        self.tip = tip
        self.model = model

class Televizor(Electronice):
    def camera(self, mpixeli = 5, model = 'Leica', culoare = 'Alb'):
        self.mpixeli = mpixeli
        self.model = model
        self.culoare = culoare

    def ecran(self, diagonala = 51, tip = 'Led', model = 'Plat'):
        self.diagonala = diagonala
        self.tip = tip
        self.model = model

class Radio(Electronice):
    def camera(self):
        pass

    def ecran(self):
        pass

i7 = Telefon('Iphone_10')

i7.camera(13)
i7.ecran(5)

TV1 = Televizor('TV1')

TV1.camera(10)

TV1.ecran(101)

R1 = Radio('radio')

R1.camera()
R1.ecran()

def caracteristici(*lista):
    for elem in (lista):
        nume = elem.name
        if 'diagonala' in elem.__dict__:
            diagonala = elem.__dict__['diagonala']
        else:
            diagonala = '-'
        if 'model' in elem.__dict__:
            model = elem.__dict__['model']
        else:
            model = '-'
        if 'culoare' in elem.__dict__:
            culoare = elem.__dict__['culoare']
        else:
            culoare = '-'
        if 'tip' in elem.__dict__:
            tip = elem.__dict__['tip']
        else:
            tip = '-'
        if 'mpixeli' in elem.__dict__:
            mpixeli = elem.__dict__['mpixeli']
        else:
            mpixeli = '-'
        print('Nume: {0} \nCamera: {1} \nTip: {3} \nModel: {4} \nEcran {2}'.format
            (nume, mpixeli, diagonala, tip, model ))
        print(type(elem))

caracteristici(TV1, i7, R1)

for elem in (TV1, i7, R1):
    for i in elem.__dict__:
        print(i + ' : ' + str(elem.__dict__[i]))
    print(type(elem))