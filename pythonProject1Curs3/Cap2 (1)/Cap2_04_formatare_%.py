""" 204 Formatare
 %
 PF - 20.07.2021 v5
"""  #

# pylint: disable=invalid-name


# ## Alternativ utilizand pentru formatare metacaracterul "%" ## #

# %(procent) este "string formating operator" in exemplele de mai jos

print("Printeaza %d un numar decimal:  %s" % (1, "Vasile"))  # numar

print("Printeaza un numar float: %f" % 18.999)  # float cu sase zecimale(default)
print("Printeaza un numar float: %.2f" % 18.795)  # float cu numar fix de zecimale

print("Acesta este pentru: %s" % "sir de caractere")  # sir de caractere

print("Doar un caracter: %c-%c" % (32805, "z"))  # un singur caracter

print("Daca vrei hexazecimal: %#x" % 255)  # primmeste decimal returneaza hexa

print("Completeaza spatii la stanga: %5d" % 17)
print("Completeaza spatii la dreapta: %-10d!" % 17)
print("Completeaza zerouri la stanga:%05d" % 17)

print("R :%10r" % 17.8)

pers1 = "Viorel"
pers2 = "Marinica"
suma1 = 100
suma2 = 50
suma3 = 72.85

print("Salut %s. Cati bani trebuie sa-mi dai, %d sau %d de lei?"  % (pers1, suma1, suma2))
print("Salut %s. Am sa-ti dau exact %.2f lei." % (pers2, suma3))


input("Apasa <enter> pt a iesi.")
