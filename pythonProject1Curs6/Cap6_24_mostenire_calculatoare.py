"""
624 Clase avansat  
Mosteniree - calculatoare
PF - 08.06.2021 v5
"""  #

from datetime import datetime

fabricat = str(datetime.now().strftime('%Y-%m'))


class Calculatoare():

    def __init__(self, den_prod, fabricat=str(datetime.now().strftime('%Y-%m')),
                 culoare = 'negru'):
        #super().__init__()
        self.den_prod = den_prod
        self.culoare = culoare
        self.data_fabricatiei = fabricat

    def componente(self, *lista_comp):
        raise NotImplementedError

    def __str__(self):
        x = 'Modelul {0} are urmatoarele caracteristici: '.format(self.den_prod)

        for i in self.__dict__:
            x += '\n' + str(i).ljust(20) + ':' + str(self.__dict__[i])
        return x

class Laptopuri(Calculatoare):

    def __init__(self, den_prod, fabricat = str(datetime.now().strftime('%Y-%m')),
                 culoare = 'negru', procesor = 'i7', ram = 'ddr4', placa = 'asus', diag = '17',
                 *lista_accesorii):
        super().__init__(den_prod, fabricat, culoare = 'negru')
        self.procesor = procesor
        self.ram = ram
        self.placa = placa
        self.diagonala = diag
        for i in lista_accesorii:
            pass

    def modifica_placa(self, noua_placa):
        self.placa = noua_placa

    def modifica_procesor(self, noul_proc):
        self.procesor = noul_proc

    def modifica_alte(self):
        ce_modifici = input('Ce doresti sa modifici (diagonala sau ram)?')
        if ce_modifici.lower() == 'ram':
            noul_ram = input('intro noul ram')
            self.ram = noul_ram
        elif ce_modifici.lower() == 'diagonala':
            noua_diag = input('intro diag')
            self.diagonala = noua_diag
        else:
            print('Nu poti modifica {0}'.format(ce_modifici))



abc001 = Laptopuri('001')

abc001.modifica_alte()

print(abc001)