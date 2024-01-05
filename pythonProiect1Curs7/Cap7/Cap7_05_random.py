"""
705 Module
Modulul ramdom
PF - 15.06.2021 v6
"""  #
import random
from random import randint

random.choice('Astazi e ziua ta')  	# alege un caracter aleator dintr-un sir
random.choice([4, 7, 9, 8, 6, 2])

# - sau, alege un element aleator dintr-o lista
random.choice(['alina', 'danseaza', 'cu', 'tine', 'sau', 'cu', 'cine', 'vrea', 'ea'])

d = dict(enumerate(['alina', 'danseaza', 'cu', 'tine', 'sau', 'cu', 'cine', 'vrea', 'ea'], start= 1))
random.choice(d)        # alege o valoare aleatoare dintr-un dictionar

random.randrange(100)  		            # numar aleator intreg intre [0-100)

random.randrange(9,100)                 # numar aleator intreg intre [9-100)

random.randrange (3, 1000, 5)  			# numar aleator intreg intre [0-1000), pass 5

random.random() * 100  				    # numar aleator intre [0.0-1.0)

# inmultit cu un numar schimba plaja de numere [0.0-100.0)

random.randint(999,1000)        # numar aleator intreg intre 999 - 1000, inclusiv

#help(random)
print(random)
