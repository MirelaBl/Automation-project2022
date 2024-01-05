"""
707 Module
Modulul pickle
PF - 15.06.2021 v6
"""  #


import pickle

var1 = {1: "Gina", 2: "Dragos", 3: "Alina", 4: "Marian"}
var2 = ["Popa", "Miulescu", "Vasile", "Coman"]
var3 = 100
var4 = 'lkjahflksdjfh'

# deschide fisier pentru scriere byti
fisier = open("pickle.txt", "wb")

# dump
pickle.dump(var1, fisier)
pickle.dump(var2, fisier)
pickle.dump(var3, fisier)
pickle.dump(var4, fisier)

fisier.close()

# deschide fisier pentru citire byti
accesare = open("pickle.txt", "rb")

# load
copy_var1 = pickle.load(accesare)
copy_var2 = pickle.load(accesare)
copy_var3 = pickle.load(accesare)
copy_var4 = pickle.load(accesare)

# Putem prelucra informatia
accesare.seek(0)
for i in range(1, 5):
	print(pickle.load(accesare))
