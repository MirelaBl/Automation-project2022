class Test:
    """Creaza clasa test"""
    color = "green"

object = Test()
print(object.color)
#green
#accesare variabila prin intermediu unui ob
print(Test.color)
#green
#accesare variabila prin intermediu unei clase
print('____________________________________________')
##atribut al clasei(blue)#

class Auto:
    """Creaza clasa auto"""
    color = "blue"

    def __init__(self):
        self.speed = 100

    def set_color(self, color):
        self.color = color

object = Auto()
print(object.color) #atribut al clasei(blue)

object.set_color("pink") # va crea un pink: atribut al instantei
print(object.color)# atribut al instantei
print(Auto.color)#atribut al clasei(blue)
print('____________________________________________')
from random import randint
class Banca:
    def __init__(self,nume_cont):
        """numele contului va fi de forma : Cont + 1 sau 2 sau3"""
        self.cont = nume_cont

    def creez_cont(self, nr_conturi):
        """creaza conturi multiple"""
        for i in range(nr_conturi):
            nume_cont = randint(0,10)
            nume_cont = "Cont"+ str( nume_cont)
            #cream instanta direct in globals
            globals()[nume_cont] = Banca(nume_cont)
            print(nume_cont)

Cont0123456789 = Banca("Cont0123456789")
Cont0123456789.creez_cont(3)

print('____________________________________________')
class Banca:
    nr_conturi=0
    conturi={}
    valute={'RON','USD','EUR'}

    def __init__(self,client, nume_cont):

        self.client= client
        self.nume_cont = nume_cont
        self.sold = 0
        Banca.nr_conturi +=1
        Banca.conturi[client] = nume_cont
    @classmethod
    def creez_cont(cls, nr_conturi, valuta, *persoane):
        for i in range(nr_conturi):
            persoana= persoane[i]
            nume_cont = randint(1,10)
            nume_cont = valuta + str(nume_cont)
            globals()[persoana]= Banca(persoana, nume_cont)

lista_persoane=('Mia','Dia','Tia')
Banca.creez_cont(len(lista_persoane),'EUR',*lista_persoane)
print('???????????????')