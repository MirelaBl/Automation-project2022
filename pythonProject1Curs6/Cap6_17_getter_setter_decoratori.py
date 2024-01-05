"""
617 OOP  
Getter/Setter - decoratori
PF - 08.06.2021 v5
"""  #


class GS:

    def __init__(self):
        self.__variabila = None

    @property                      # decorator
    def variabila(self):
        print("Get variabila")      # flag - sa vedem ce metoda apeleaza
        return self.__variabila

    @variabila.setter
    def variabila(self, value):
        print("Set variabila")      # flag - sa vedem ce metoda apeleaza
        self.__variabila = value

    @variabila.deleter
    def variabila(self):
        print("Delete variabila")   # flag - sa vedem ce metoda apeleaza
        del self.__variabila


obiect = GS()

print(obiect.__variabila)       # nu are atributul
print(obiect.variabila)        # apeleaza metoda "get", nu are atribut (None)

obiect.variabila = 100        # apeleaza metoda "set" - aloca valoare

print(obiect.variabila)        # apeleaza metoda "get"
print(obiect.__variabila)       # are atributul

print(obiect.__dict__)         # observam ca obiectul are doar atributul _variabila

del obiect.variabila           # apeleaza delete

print(obiect.__dict__)

obiect._GS__variabila