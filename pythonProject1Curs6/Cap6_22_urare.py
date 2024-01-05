"""
622 Clase avansat  
Urare An Nou
PF - 08.06.2021 v5
"""  #


class An2021:
    '''Anul tau cel mai bun de pana acum
    cu sanatate, iubire si bani''' #

    def __init__(self, numar):
        self.sanatate = 'Maxima'    # default pentru tine
        self.iubire = 'Sublima'
        self.bani = numar

    def adauga_bani(self, suma):    # daca nu-ti ajung :)
        self.bani += suma

Tu = An2021(1000000)