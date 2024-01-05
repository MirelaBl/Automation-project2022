class DictCuv:
	"""Gestioneaza dictionare de cuvinte de diferite genuri""" #


	def __init__(self):
		"""in dc cheia va fi cuvantul, valoarea va fi descrierea""" #
		self.dc = {}


	def adauga(self):
		"""adauga succesiv cuvinte inexistente!"""

		while True:
			cuvant = input("Introduceti cuvantul:").lower()
			if cuvant == "":
				break
			elif cuvant in self.dc.keys():
				print(f"Cuvantul {cuvant} se afla deja in dictionar!")
				continue
			else:
				descriere = input(f"Introduceti descrierea pentru {cuvant}:").lower()
				self.dc[cuvant] = descriere


	def modifica(self):
		"""modifica succesiv cuvinte!"""

		while True:
			if not self.dc.keys():
				print("Ne pare rau, dictionarul este gol (m)!")
				break
			else:
				cuvant = input("Introduceti cuvantul de modificat:").lower()
				if cuvant == "":
					break
				elif cuvant in self.dc.keys():
					descriere = input(f"Introduceti descrierea pentru {cuvant}:").lower()
					self.dc[cuvant] = descriere
				else:
					print(f"Cuvantul {cuvant} nu se afla in dictionar!")

	def cauta(self):
		"""cauta succesiv cuvinte!"""

		while True:
			if not self.dc.keys():
				print("Ne pare rau, dictionarul este gol (c)!")
				break
			else:
				cuvant = input("Introduceti cuvantul cautat:").lower()
				if cuvant == "":
					break
				elif cuvant in self.dc.keys():
					print(f"Cuvant: {cuvant}\nDescriere: {self.dc[cuvant]}")
				else:
					print(f"Cuvantul {cuvant} nu se afla in dictionar!")

	def sterge(self):
		"""sterge succesiv cuvinte!"""

		while True:
			if not self.dc.keys():
				print("Ne pare rau, dictionarul este gol (s)!")
				break
			else:
				cuvant = input("Introduceti cuvantul de sters:").lower()
				if cuvant == "":
					break
				elif cuvant in self.dc.keys():
					print(cuvant + " a fost sters")
					self.dc.pop(cuvant)
				else:
					print(f"Cuvantul {cuvant} nu se afla in dictionar!")


	def __str__(self):
		keys = sorted(self.dc.keys())
		result = ""
		for i in keys:
			result += f"\n {i}".ljust(25) + f"{self.dc[i]}"
		return result


dex = DictCuv()
dop = DictCuv()
dfe = DictCuv()

dir(dex)

print(dex)
dex.sterge()
dex.modifica()
dex.cauta()

dex.adauga()