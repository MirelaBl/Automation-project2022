""" 
102
Numere
PF - 2020-04-13 v4
"""  #

# Integer(int), float, numere complexe:

print(4 + 3)         # adunare

print(5 - 2)         # scadere

print(5 * 2)         # inmultire

print(8 / 2)         # impartire(exacta - rezultat float)

print(8 / 3)         # impartire(exacta - rezultat float)

print(8 // 3)        # impartire(doar catul impartirii)

print(10 % 3)        # modulo(doar restul impartirii)

print(((7 + 3) * 2) / 4)    # operatii cu mai multi operatori(doar paranteze rotunde)
                               # operatorul * se mentioneaza chiar daca sunt paranteze
print((2 + 2j) * (2 + 1j))       # operatii cu numere complexe

print(5 ** 4)                    # ridicarea la putere

# lucrul cu numere complexe
print(int((2 + 1j).real))
print((2 + 1j).imag)
print((2 + 1j).conjugate())

# Conversii de numere

print(int('1fa0', 16))     # transforma un string in numar din baza dorita in baza 10
                           # cat reprezinta "1fa0" din baza 16 in baza 10?

print(int('75'))           # transforma un string, care contine doar cifre, in numar int
                           # daca daza este 10 nu trebuie mentionata
print(int('2.5'))               # eroare, nu putem transforma direct in string daca are si zecimale

print(int(
        float('2.5')
        )
    )
                            # float face transformarea in numar, int elimina zecimalele

print(oct(63))               # functie pentru transformarea intr-un numar in baza 8

print(hex(255))             # functie pentru transformarea intr-un numar in baza 16

print(bin(0Xff))            # functie pentru transformarea intr-un numar in baza 2

print(str(157))

str(157)

input("Apasa <enter> pt a iesi.")
