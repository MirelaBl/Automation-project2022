"""
604 OOP VS
Validarea datelor de intrare
PF - 08.06.2021 v5
"""  #


class People:
	"""Atribut clasa / atribut obiect - continuare"""
	an_studiu = {'Anul 1', 'Anul 2', 'Anul 3', 'Anul 4', 'Anul 5'}  # ani de studiu
	facultate = {'Inginerie', 'Drept', 'Finante', 'Geografie'}  # specializari

	def __init__(self, nume, anul, facultatea):
		if anul in People.an_studiu:
			self.anul = anul
		else:
			raise NameError('Anul de studii este incorect')
		if facultatea in People.facultate:
			self.studii = facultatea
		else:
			raise NameError('Specialitate incorecta')
		self.nume = nume

	def __str__(self):
		result =  self.nume + " este in " + self.anul + ' la ' + self.studii + '.'
		return result

# student 1
Vasile = People( 'Vasile', 'Anul 2', 'Drept' )
print( Vasile )

# student 2
Carmen = People( 'Carmen', 'Anul 1', 'Geografie' )
print ( Carmen )
Carmen.__dict__

# student 3
Dorel = People( 'Dorel','Anul 3','Finante' )
print ( Dorel )

''' negative 
# student 3
Dorel = People( 'Dorel', 'Finante', 'Anul 3' )
print ( Dorel )
'''
