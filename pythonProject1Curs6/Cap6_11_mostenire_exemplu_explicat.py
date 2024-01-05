"""
611 OOP  
Mostenire - exemplu explicat
PF - 08.06.2021 v5
"""  #


class Banca:  						# creem clasa
	"""Institutie financiara"""

	nr_conturi = 0

	def __init__(self):  # metoda constructor - se mosteneste
		self.sold = 0 	# se aplica la crearea fiecarui obiect - se mosteneste
		Banca.nr_conturi += 1  # incrementeaza numarul de conturi disponibile - se mosteneste

	def alim_cont(self, suma): # metoda - aplicabila pentru fiecare obiect - se mosteneste
		self.sold += suma
		self.sold_nou ()

	def extr_cash(self, suma): # metoda - aplicabila pentru fiecare obiect - se mosteneste
		self.sold -= suma
		self.sold_nou()

	def sold_nou(self):  # metoda - aplicabila pentru fiecare obiect - se mosteneste
		print ('Noul sold este: {:.2f}'.format(self.sold ))

	def __del__(self):
		Banca.nr_conturi -= 1
		print('Am sters contul')


class CEC(Banca):

	def plata_op(self, suma):  # metoda proprie a subclasei
		self.sold -= suma
		self.sold_nou()

	def desc_cont(self, suma):  # metoda proprie a subclasei
		self.sold += suma
		self.sold_nou()

Cont_Germin = CEC()  # instanta noua subclasa
print(Cont_Germin.__dict__)
print(Cont_Germin.nr_conturi)

Cont_Germin.alim_cont(20000)  # metoda mostenita
Cont_Germin.plata_op(1800)  # metoda proprie
Cont_Germin.extr_cash(1950)  # metoda mostenita
Cont_Germin.sold_nou()  # metoda mostenita

Cont_Alina = Banca()  # instanta noua superclasa

Cont_Alina.sold_nou()
Cont_Alina.desc_cont(5000)  # o instanta a unei superclase nu poate accesa metode proprii subclaselor

print(Banca.nr_conturi)  # numar de conturi poate fi apelat de orice instanta, superclasa si subclasa

print(CEC.nr_conturi)

print(Cont_Alina.nr_conturi)

print(Cont_Germin.nr_conturi)

isinstance(Cont_Germin, Banca)
isinstance(Cont_Germin, CEC)

isinstance(Cont_Alina, Banca)

print(Cont_Germin)

issubclass(CEC, Banca)
issubclass(Banca, CEC)

