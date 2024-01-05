from datetime import datetime
from prettytable import PrettyTable

class Stoc:
	"""pentru gestiunea produselor""" #

	categorii = {}

	def __init__(self, produs, categ, um="kg", sold=0):
		self.produs = produs
		self.categorie = categ
		self.um = um
		self.sold = sold
		self.miscari = {}
		if categ in Stoc.categorii:
			Stoc.categorii[categ] += [produs]
		else:
			Stoc.categorii[categ] = [produs]


	def intrari(self, cant, data = str(datetime.now().strftime('%Y%m%d'))):
		cheia = self.set_cheie()
		self.miscari[cheia] = [data, cant, 0]
		self.sold += cant


	def iesiri(self, cant, data = str(datetime.now().strftime('%Y%m%d'))):
		cheia = self.set_cheie()
		if cant > self.sold:
			cant = self.sold
		self.miscari[cheia] = [data, 0, cant]
		self.sold -= cant


	def set_cheie(self):
		if self.miscari.keys():
			cheia = max(self.miscari.keys()) + 1
		else:
			cheia = 1
		return cheia


	def fisap(self):
		print(f'Fisa produsului {self.produs} in {self.um}')

		afiseaza = PrettyTable()
		afiseaza.field_names = ['Nrc', 'Data', 'Intrare', 'Iesire', 'Sold']

		sold = 0
		for k, v in self.miscari.items():
			sold += v[1] - v[2]
			afiseaza.add_row([k, v[0], v[1], v[2], sold])
		print(afiseaza)

enunt = '''


Adaugati o variabila de clasa categorii, care va fi un dictionar, in care:
 - cheia va fi categoria (se va actualiza la instantiere, in metoda init)
 - valoarea va fi o lista cu produsele categoriei (se va popula la instantiere)
Testati.
''' #

alune = Stoc('alune', 'rontait', 'punga')

alune.__dict__

alune.intrari(200, '20221230')
alune.iesiri(112, '20221231')
alune.intrari(150)
alune.iesiri(187)

#alune.fisap()

bere = Stoc('bere', 'aliment', 'sticla')

bere.intrari(100)
bere.iesiri(120)
# bere.fisap()


seminte = Stoc('seminte', 'rontait', 'punga')

seminte.intrari(10)
seminte.iesiri(8)

listap = [alune, bere, seminte]

for i in listap:
	i.fisap()

Stoc.categorii

alune.categorii

alune.__dict__