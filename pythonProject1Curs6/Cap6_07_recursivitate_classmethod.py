"""
607 OOP  
Recursivitatea --> crearea de obiecte recursiv
PF - 08.06.2021 v5
"""  #

from random import randint  # importam functia randint care returneaza un numar intreg aleator dint-un interval


class Banca:
    """Institutie financiara"""
    nr_conturi = 0  # numara cate conturi saunt create la un moment dat
    conturi = {}  # incrementeaza numarul de conturi disponibile la fiecare instantiere
    valute = {'RON', 'EUR', 'USD', 'GBP', 'CHF'}

    def __init__(self, client, nume_cont):
        """Numele contului va fi de forma: valuta + 10 cifre,
            valuta fiind una din setul de valori"""  #
        if nume_cont[0: 3] in Banca.valute:
            if nume_cont[3:].isdigit():
                if not nume_cont in Banca.conturi:
                    self.nume_cont = nume_cont
        else:
            raise NameError('Nume incorect!')
        self.client = client
        self.sold = 0
        Banca.nr_conturi += 1
        Banca.conturi[client] = nume_cont

    @classmethod  # o metoda a clasei, poate fi apelata fara sa existe o instanta
    def creez_cont(cls, Cate, valuta, *persoane):
        """
        metoda care poate crea multiple instante apeland clasa
        :param Cate: cate conturi vor fi create
        :param valuta: poate fi una din setul de valori Banca.valute
        :return:
        """
        for i in range(Cate):
            persoana = persoane[i]
            x = randint(0, 10000000000)
            x = valuta + '%010d' % x
            globals()[persoana] = Banca(persoana, x)

# instanta obisnuita
Vasile = Banca('Vasile', 'RON1111111111')  # Cream un cont

# instantiere recursiva - apelarea unei metode a clasei poate fi facuta si de classa si de obiect
lista_persoane = ('Ana', 'Lia', 'Vio', 'Mary')
Banca.creez_cont(len(lista_persoane), 'EUR', *lista_persoane)

Vasile.creez_cont(2, 'GBP', 'Emil', 'George')

print(Banca.nr_conturi)
print(Banca.conturi)
print(Vasile.nr_conturi)
print(Vasile.conturi)

print(Vasile.__dict__)
print(Ana.__dict__)
