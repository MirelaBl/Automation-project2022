"""
618 OOP  
Getter/Setter - property()
PF - 08.06.2021 v5
"""  #


class GS_alt:

    def __init__(self, atribut_initial):
        self.__set_atribut(atribut_initial)

    def __get_atribut(self):
        return self.__atribut

    def __set_atribut(self, atribut):
        self.__atribut = atribut

    atribut = property(__get_atribut, __set_atribut)

obiect_alt = GS_alt(5)

print(obiect_alt.atribut)

obiect_alt.atribut = 15

print(obiect_alt.__dict__)

obiect_alt.__setattr__('atribut', 100)

obiect_alt.__getattribute__('atribut')

dir(obiect_alt)