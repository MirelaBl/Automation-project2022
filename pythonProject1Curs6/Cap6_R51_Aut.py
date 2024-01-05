"""
651 Clase avansat  
Mostenire - vehicule
PF - 08.06.2021 v5
"""  #

'''
Creati un program care sa cuprinda o superclasa Vehicule. Clasa atribuie marca la crearea instantei.
    Creati o subclasa a acesteia, Autoturisme, cu o metoda proprie care sa specifice nr de roti.
Creati o subclasa Berlina clasei Autoturisme cu o metode care sa dea urmatoarele atribute:
    motor, tractiune, siguranta, culoare.
O alta metoda va fi creata pentru a lista toate caracteristicile (__str__).
    Creati o instanta  in clasa Berlina si aplicati toate metodele posibile.
Creati alte doua clase pentru motociclete si autocamioane, fiecare cu cate cel putin doua metode proprii.
    Creati instante in cele doua noi clase si aplicati metodele posibile
'''#

class Vehicule:
    """Clasa vehicule"""

    def __init__(self, marca):
        self.marca = marca
        self.nr_roti = 4

    def dotari(self, motor, tractiune, siguranta, culoare):
        self.motor = motor
        self.tractiune = tractiune
        self.siguranta = siguranta
        self.culoare = culoare

    def __str__(self):
        x = ''
        for i in self.__dict__:
            x += str(i).ljust(20) + str(self.__dict__[i]) + '\n'
        return x


class Autoturisme(Vehicule):

    def roti(self, nr_roti):
        self.nr_roti = nr_roti

    def categoria(self, ctg = 'persoane'):
        self.ctg = ctg

class Berlina(Autoturisme):
    def dotari_berlina(self, motor, tractiune, siguranta, culoare):
        self.dotari(motor, tractiune, siguranta, culoare)

class Motociclete(Vehicule):

    def dotari_moto(self, cap_cil, frane):
        self.cap_cil = cap_cil
        self.frane = frane

class Autocamioane(Vehicule):

    def dotari_ac(self, viteze, suspensie):
        self.viteze = viteze
        self.suspensie = suspensie

    def roti(self, nr_roti):
        self.nr_roti = nr_roti

vv = Vehicule('Generic')

vv.dotari(1.4, 'spate', 'abs', 'alb')
print(vv)


ff = Autoturisme('Ford')

ff.roti(4)
ff.categoria()
ff.dotari(1.6,'fata','ABS','neagra')
print(ff)

Logan = Berlina('Dacia')    # Marca prin __init__ din Clasa parinte Vehicule
Logan.roti(4)               # Metoda din clasa parinte Autoturisme
Logan.dotari('1.4 benzina', 'Fata', '-', 'Albastru')  # Metoda proprie, care apeleaza metoda din Vehicule
#Logan.get_caracteristici()  # nu are metoda proprie, nici mostenita - eroare
print(Logan)

Yamaha = Motociclete('Yamaha')
Yamaha.nr_roti = 2
Yamaha.dotari_moto('500', 'disc')
Yamaha.dotari('2 timpi', 'spate', '-', 'albastra')
print(Yamaha)

print(Yamaha.marca)


man = Autocamioane('M.A.N.')

man.roti(6)
man.dotari('rolse royce', '6x6', 'abs', 'rosu')
man.dotari_ac(12, 'perna de aer')
print(man)