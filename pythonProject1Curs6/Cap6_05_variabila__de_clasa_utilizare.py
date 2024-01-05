"""
605 OOP VS
Variabila de clasa --> utilizare
PF - 08.06.2021 v5
"""  #

class Auto:
	"""Atribut clasa / atribut obiect - continuare"""
	culoare = 'Alb'
	model = 'Berlina'

	# in interiorul clasei putem folosi atat self cat si numele clasei
	def __str__(self):
		result = 'Autorurismul are culoarea ' + self.culoare + ', si modelul ' + Auto.model
		return result

# instantiem
masina_mea = Auto()
print(masina_mea)

# in exterior putem apela VS atat cu NumeClasa.VS cat si cu NumeInstanta.VS
print(Auto.culoare )
print(masina_mea.culoare)
print(masina_mea.__dict__)
