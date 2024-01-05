class Echipa():

    def __init__(self, nume, antrenor, sponsor, *nume_jucatori):
        self.nume = nume
        self.antrenor = antrenor
        self.sponsor = sponsor
        self.lista_jucatori = []
        self.goluri = {}
        for i in nume_jucatori:
            self.lista_jucatori.append(i)
            self.goluri[i] = 0
        self.nr_jucatori = len(self.lista_jucatori)

    def adauga_jucator(self, jucator_intrat):
        if jucator_intrat not  in self.lista_jucatori:
            self.lista_jucatori.append(jucator_intrat)
            self.nr_jucatori += 1
            self.goluri[jucator_intrat] = 0
        else:
            print('Jucatorul %s deja exista' % jucator_intrat)

    def elimina_jucatori(self, jucator_iesit):
        if jucator_iesit in self.lista_jucatori:
            self.lista_jucatori.remove(jucator_iesit)
            self.nr_jucatori -= 1
        else:
            print('Jucatorul %s nu exista in lista' % jucator_iesit)

    def marcheaza(self, jucatorul, nr_goluri = 1):
        if jucatorul in self.lista_jucatori:
            self.goluri[jucatorul] += nr_goluri
        else:
            print('Jucatorul %s nu este in echipa noastra' % jucatorul)

class Romania(Echipa):

    def statistici(self):
       self.suma_goluri = 0
       for i in self.goluri.values():
           self.suma_goluri += i
       self.media_goluri = self.suma_goluri/self.nr_jucatori
       self.maxim_goluri = max(self.goluri.values())

       for i in self.goluri:
            if self.goluri[i] == self.maxim_goluri:
                self.golgheter = i

    def __str__(self):
        self.statistici()

        return 'Total goluri marcate: {0} \nMedia de goluri: {1} \nGolgheter: {2}'.\
            format(self.suma_goluri, self.media_goluri, self.golgheter)


Steaua = Romania('SB', 'Piturca', 'City', 'Dumitrescu', 'Lacatus',
                 'Hagi', 'Belodedici', 'Ducadam', 'Balint', 'Barbulescu')

print(Steaua.nume)
print(Steaua.nr_jucatori)
print(Steaua.antrenor)
print(Steaua.lista_jucatori)
print(Steaua.goluri)
Steaua.adauga_jucator('Bumbescu')
Steaua.elimina_jucatori('Barbulescu')

Steaua.marcheaza('Balint', 5)
Steaua.marcheaza('Bumbescu')

print(Steaua)


Rapid = Romania('RB', 'Sumudica', 'CFR', 'Coman', 'Raducanu',
                 'Rada')

print(Rapid.nume)
print(Rapid.nr_jucatori)
print(Rapid.antrenor)
print(Rapid.lista_jucatori)
print(Rapid.goluri)
Rapid.adauga_jucator('Vasile')
Rapid.elimina_jucatori('Rada')

Rapid.marcheaza('Vasile', 7)
Rapid.marcheaza('Coman', 5)

print(Rapid)