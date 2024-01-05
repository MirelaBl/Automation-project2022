
enunt = """sa se creeze o clasa Persoana cu atributele nume si varsta (__init__)
Va avea implementate metodele __str__, __del__ si o metoda de atribuire email
"""  #

class Persoana:

	def __init__(self, n, v):
		self.nume = n
		self.varsta = v

	def set_email(self, domeniu):
		self.email = self.nume + '@' + domeniu


	def __str__(self):
		return self.nume + " are varsta de " + str(self.varsta) + " ani "


	def __del__(self):
		print(self.nume + " a iesit la pensie")


george = Persoana('george', 38)
elena = Persoana('elena', 29)
cristi = Persoana('cristi', 33)
elisabeta = Persoana('elisabeta', 27)

george.__dict__
george.set_email('firma.ro')
george.email

persoane = [george, elena, cristi, elisabeta, Persoana('maria', 29)]

for i in persoane:
	i.set_email('gmail.com')

for i in persoane:
	print(i.email)

for i in persoane:
	print(i)