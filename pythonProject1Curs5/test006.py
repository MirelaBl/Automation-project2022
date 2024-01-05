enunt = '''
Organizati un concurs, la care pot participa un numar variabil de concurenti.
- daca sunt mai putin de 3 participanti se anuleaza;
- intre 3-10 participanti - vor fi trei premianti 50, 35, 15 % din valoarea premiului;
- intre 11-30 participanti - 5 premianti cu 40, 30, 10, 10, 10 %
- peste 31 de participanti - 10 premianti cu 30, 20, 15, 5, 5, 5, 5, 5, 5, 5 %

Creati o functie care sa primeasca ca argument total premii si numarul de participanti
si sa returneze valoarea premiilor pentru fiecare castigator (locul 1, 2, etc.).

Creati o alta functie, care sa tina cont si de impozit, astfel incat premiile mai mari de
10000 de lei sa fie impozitate cu 10%.
'''  #

def premii(valoare, participanti):
	"""Calculeaza premiile in functie de numarul de participanti
	valoare: total premii
	participanti: numarul de participanti"""

	procente = []
	if participanti < 3:
		print("Concurs anulat!")
	elif participanti < 11:
		procente = [50, 35, 15]
	elif participanti < 31:
		procente = [40, 30, 10, 10, 10]
	else:
		procente = [30, 20, 15, 5, 5, 5, 5, 5, 5, 5]

	if procente:
		for i in range(len(procente)):
			premiu = valoare * procente[i] / 100
			print(f"Premiul {i + 1}: {premiu}")

premii(100000, 31)
