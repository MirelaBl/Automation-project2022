from datetime import datetime
from prettytable import PrettyTable

class Stoc:
	"""Despre gestiunea produselor"""

	categorii = {}

	def __init__(self, denp, categ, um='kg', sold=0):
		"""metoda constructor"""
		self.denp = denp
		self.categ = categ
		self.um = um
		self.sold = sold
		self.do = {}
		if categ in Stoc.categorii:
			self.categorii[categ] += [denp]
		else:
			self.categorii[categ] = [denp]

	def gen_cheia(self):
		if self.do:
			cheia = max(self.do.keys()) + 1
		else:
			cheia = 1
		return cheia

	def intrari(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
		cheia = self.gen_cheia()
		self.do[cheia] = [data, cant, 0]
		self.sold += cant

	def iesiri(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
		cheia = self.gen_cheia()
		if self.sold < cant:
			cant = self.sold
		self.do[cheia] = [data, 0, cant]
		self.sold -= cant

	def fisap(self):
		print(f'Fisa produsului {self.denp} {self.um}')
		listeaza = PrettyTable()
		listeaza.field_names = ['Nrc', 'Data', 'Intrare', 'Iesire']
		for k, v in self.do.items():
			listeaza.add_row([k, v[0], v[1], v[2]])
		return str(listeaza)


alune = Stoc('alune', 'fructe', 'cutie')

alune.intrari(100)
alune.iesiri(83)

print(alune.fisap())



class DepozitCuca(Stoc):

	nume_depozit = "Cuca"


	def val_stoc(self, pret):
		return pret * self.sold


	def perisabilitati(self, procent):
		rulaj = 0
		for v in self.do.values():
			rulaj += v[1]
		scazaminte = rulaj * procent / 100
		self.iesiri(scazaminte)