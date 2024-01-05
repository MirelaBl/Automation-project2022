"""
- Person: first_name, last_name, dob
	metode: set_email, set_tel

- Student(Person): catalog - dict cu cheia materia, val un dictionar cu cheia nota si o lista de note
	metoda: pune_nota

- Medic(Person): specialitate

- Rezident(Medic): spital

- Firma: name, director: Person  
	metode: set_email, set_tel
""" #

import re


class Address:

	def set_email(self, email):
		self.email = email

	def set_telephone(self, tel):
		if re.findall("^[0-9]{10}$", tel):
			self.telephone = tel

class Person(Address):
	"""Clasa Person""" #


	def __init__(self, fn, ln, dob):
		self.first_name = fn
		self.last_name = ln
		self.date_of_birth = dob



class Student(Person):


	def __init__(self, *parent):
		self.catalog = {}
		super().__init__(*parent)


	def put_note(self, object, note):

		if self.catalog:
			if object in self.catalog:
				self.catalog[object] += [note]
			else:
				self.catalog[object] = [note]
		else:
			self.catalog[object] = [note]

class Doctor(Person):


	def __init__(self, specialitate, **parent):
		self.specialitate = specialitate
		super().__init__(**parent)


class Resident(Doctor):


	def __init__(self, spital, **parent):
		self.spital = spital
		super().__init__(**parent)



class Firm(Address):


	def __init__(self, name, director: Person):
		self.name = name
		self.director = director





pers1 = Person('Maria', 'Popescu', '2001-01-01')
pers2 = Person('Cristi', 'Georgescu', '1987-02-02')

pers1.last_name
pers2.first_name
#pers1.email
pers2.set_email('cristi@gmail.com')
pers2.email
pers2.__dict__
pers1.set_telephone("074354323")

pers1.__dict__

stud1 = Student('Simina', 'Stoica', '2003-09-05')

stud1.set_email('simina@yahoo.com')

stud1.put_note('mate', 7)
stud1.put_note('mate', 10)

stud1.put_note('phisics', 10)

stud1.__dict__

medic1 = Doctor('chirurgie', fn='Mircea', ln='Mircescu', dob="1991-09-03")

medic1.__dict__

rezident = Resident('Colentina', specialitate='orl', fn='Ana', ln='Aanitei', dob='1996-09-27')

rezident.__dict__

firm1 = Firm('Alfa', stud1)

firm1.name

firm1.director.email




firm1.set_email('alfa@alfa.ro')

firm1.email