"""
421
Valoare viitoare
PF 02.09.2020 v4
"""  #

# pylint: disable=invalid-name

enunt = """
Scrie o functie care sa primeasca parametri de intrare 
  suma unica investita, 
  rata de dobanda fixa si  
  numarul de ani si 
     sa returneze 
  valoarea viitoare a investitiei: suma * (1 + i) ** ani 
  unde i este procentul de dobanda (0.05 pentru 5%)
Apeleaz-o 
"""

def finante(suma,i,nrani):
    return suma * (1 + i) ** nrani

print(finante(1000,0.05,4))
print('var2')
def dobinvfixa(suma, dobanda, ani):
    """Calculeaza suma viitoare returnata de o investitie curenta in suma unica"""  #
    s = suma
    d = dobanda/100
    for i in range(ani):
        s = s * (1 + d)
    s = '{:.2f}'.format(s)
    return 'Valoarea peste ' + str(i + 1) + ' ani este de: ' + str(s)

print(dobinvfixa(1000, 0.05, 4))
input('Apasa <enter> pentru a iesi.')



