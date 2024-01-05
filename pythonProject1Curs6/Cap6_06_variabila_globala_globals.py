"""
606 OOP  
Variabila globala - globals()
PF - 08.06.2021 v5
"""  #

a = 100                     # Creare VG
b = 'caine'
c = ['a','x', 'ax']

globals()  # DICT cu VG la un moment dat

if 'c' in globals():
    print(c)  # verifica existenta VG

print(b)

globals()['b'] = 'pisica'  # atribuire valoare valoare noua VG direct in globals()

globals()['cimpanzeu'] = 'maimuta'  # o noua VG definita direct in globals()

globals()['Dacia'] = Auto()  # o instanta a unui obiect creata direct in globals()

# functia eval()
eval('Dacia.Culoare')
