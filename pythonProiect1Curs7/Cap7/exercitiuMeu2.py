import random

print(random.choice('Astazi e ziua ta'))	# alege un caracter aleator dintr-un sir
print(random.choice([4, 7, 9, 8, 6, 2]))

import tempfile
t1 = tempfile.TemporaryFile()  # creaza un fisier temporar care va fi sters automat

t1.write(b'ana are cirese')
print(t1.__dict__["name"])

t2= tempfile.mkstemp()
