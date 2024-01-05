"""
R122
Exercitii simple in Python
PF - 2020-04-13 v4
"""  #.

# pylint: disable=invalid-name
# pylint: disable=trailing-whitespace
# pylint: disable=pointless-string-statement

from math import sqrt       # importam functia sqrt

"""1. Scrieti un script cu ajutorul caruia sa completati adresa postala asa cum apare pe plic,
      pe linii separate, prin introducerea elementelor de la tastatura, astfel:
       destinatar 
       strada, numar 
       oras, judet 
       cod postal 
      Utilizati variabiile pentru fiecare componenta a adresei"""

dest = input('Introduceti dest:')
strada = input('Introduceti strada:')
nr = input('Introduceti numarul:')
oras = input('Introduceti orasul:')
jud = input('Introduceti judetul:')
cp = input('Introduceti codul postal:')

print('Destinatar: '+ dest+ '\nStrada:     ' + strada + ', Nr: ' + nr +'\nOrasul:     '\
      + oras + ', Judetul: ' + jud + '\nCod postal: ' + cp)

"""2.   Scrieti un program care sa primeasca de la tastatura dimensinile catetelor 'c1' si 'c2'.
    Ipotenuza este egala cu radical din suma patratelor catetelor. 
    Inaltimea pe ipotenuza este produsul catetelor supra ipotenuza.
    Programul va afisa: dimensiunea catetelor, a ipotenuzei si a inaltimii."""

c1 = int(input("Introduceti un numar intrg pentru cateta 1: \n"))
c2 = int(input("Introduceti un numar intrg pentru cateta 1: \n"))
ipo = sqrt(c1 ** 2 + c2 ** 2)
hi = c1 * c2 / ipo
print('Cateta 1:', c1, '\nCateta 2:', c2, '\nIpotenuza:', ipo, '\nInaltimea:', hi)

"""3.   Scrieti un program logistic avand in vedere urmatoarele:
    - aprovizionati trei produse:
        - biscuiti cu cioco, 125g / pachet, 48 pachete intr-o cutie, 32 cutii / metru cub;
        - biscuiti cu alune, 150g / pachet, 36 pachete intr-o cutie, 36 cutii / metru cub;
        - biscuiti   simpli, 200g / pachet, 24 pachete intr-o cutie, 40 cutii / metru cub;
    - introduceti de la tastatura cate pachete aprovizionati din fiecare(8000 cioco, 
    10000 alune, 6000 simpli);
    - printati cat cantaresc in total, cate cutii sunt necesare si cati metri cubi ocupa; 
    Folositi variabile, astfel incat daca modificam parametrii sa nu modificam programul
    (Rezultate: 3700 Kg, 694.44 cutii, 19.17 mc)"""

gr_c = .125         # greutatea unui pachet (pentru punctul 4 modifica 0.112 - doar la cioco)
gr_a = .150
gr_s = .200

pac_cut_c = 48      # cate pachete intra intr-o cutie (pentru punctul 4 modifica 52 - doar la cioco)
pac_cut_a = 36
pac_cut_s = 24

cut_mc_c = 32       # cate cutii intra intr-un metru cub
cut_mc_a = 36
cut_mc_s = 40

ca_c = int(input('Cate pachete de biscuiti cu cioco? '))    # cate pachete aprovizionam
ca_a = int(input('Cate pachete de biscuiti cu alune? '))
ca_s = int(input('Cate pachete de biscuiti simpli? '))

cioco = gr_c * ca_c                     # calculam greutatea aprovizionata pe sortimente si total
alune = gr_a * ca_a
simpli = gr_s * ca_s
cant_total = cioco + alune +simpli

nec_cutii_c = ca_c / pac_cut_c          # calculam necesarul de cutii pe sortimente si total
nec_cutii_a = ca_a / pac_cut_a
nec_cutii_s = ca_s / pac_cut_s
nec_cutii_total = nec_cutii_a + nec_cutii_c + nec_cutii_s

vol_c = nec_cutii_c / cut_mc_c          # calculam volumul ocupat pe sortimente si total
vol_a = nec_cutii_a / cut_mc_a
vol_s = nec_cutii_s / cut_mc_s
vol_total = vol_s + vol_a + vol_c

print('Marfa dv cantareste', cant_total,
      'kg, pentru care sunt necesare', nec_cutii_total, 'cutii si care ocupa un volum total de',
      vol_total, 'mc')

"""4.   Pentru biscuitii cu cioco se modifica datele astfel:
        - biscuiti cu cioco, 112g / pachet, 52 pachete intr-o cutie, 32 cutii / metru cub;
       Faceti modificarile minime necesare astfel incat programul dv sa functioneze
       (Rezultate: 3596 Kg, 681.62 cutii, 18.77 mc)"""

gramaj_cioco = .112
gramaj_alune = .150
gramaj_simpli = .2

pac_per_cutie_cioco = 52
pac_per_cutie_alune = 36
pac_per_cutie_simpli = 24

cutii_per_mc_cioco = 32
cutii_per_mc_alune = 36
cutii_per_mc_simpli = 40

cant_prov_cioco = int(input('Introduceti cantitatea pt ciocolata: '))
cant_prov_alune = int(input('Introduceti cantitatea pt alune: '))
cant_prov_simpli = int(input('Introduceti cantitatea pt simpli: '))

total_cantitate = gramaj_cioco * cant_prov_cioco + gramaj_alune * cant_prov_alune + \
                gramaj_simpli * cant_prov_simpli

necesar_cutii_cioco = cant_prov_cioco / pac_per_cutie_cioco
necesar_cutii_alune = cant_prov_alune / pac_per_cutie_alune
necesar_cutii_simpli = cant_prov_simpli / pac_per_cutie_simpli

total_cutii = necesar_cutii_alune + necesar_cutii_cioco + necesar_cutii_simpli

total_volum = necesar_cutii_cioco / cutii_per_mc_cioco + \
            necesar_cutii_alune / cutii_per_mc_alune + \
            necesar_cutii_simpli / cutii_per_mc_simpli

print('Cantitatea de aprovizionat: ', total_cantitate, '\nNecesarul de cutii: ',
      total_cutii, '\nVolum ocupat: ', total_volum)

input('Apasa ENTER pentru a iesi')
