"""
429
Exercitii - Credit cu rate fixe
PF 18.09.2020 v4
"""  #

# pylint: disable=invalid-name

from prettytable import PrettyTable

enunt = '''
Contractati un credit. Aveti urmatorii parametrii de intrare:
- valoarea de achizitie:
- rata anuala a dobanzii - default 6%
- numarul de luni de rambursare (plati fixe)
Scrieti un program care să afișeze un tabel cu scadenta si platile pe durata de viață a împrumutului.
Fiecare rând al tabelului va contine:
- numărul lunii (începând cu 1)
- soldul total datorat
- dobânda datorată pentru luna in curs
- principalul datorat pentru luna in curs
- rata lunii in curs (principal plus dobanda)
- soldul ramas după efectuarea plății
- totaluri (dobanzi)
Valoarea dobanzii lunare va fi dobanda anuala / 12. Suma
principal pentru o lună este egală cu plata lunară minus dobânzile datorate.
# variabile posibile de utilizat (formule adecvate):
dobanda = rata_dobanzii/12/100
indice = 1 + dobanda
putere = indice ** numar_rate
plata_constanta = suma * dobanda / (1 - 1/putere)
'''  #



def credit(valoare, rata_dobanzii=6, numar_rate=120):
    """Credit rate fixe"""
    sold_init = valoare
    dobanda = rata_dobanzii / 12 / 100
    indice = 1 + dobanda
    putere = indice ** numar_rate
    plata_constanta = valoare * dobanda / (1 - 1 / putere)
    luna = 1
    total_dob_datorate = 0
    listeaza = PrettyTable()
    listeaza.field_names = ['Luna', 'Sold_i', 'Dob_lu', 'Prin_lu', 'Rata_lu', 'Sold_f']

    while sold_init > 0:
        dob_lun = sold_init * dobanda
        princ_lun = plata_constanta - dob_lun
        rata_lun = dob_lun + princ_lun
        sold_final = sold_init - princ_lun
        total_dob_datorate += dob_lun
        listeaza.add_row([luna,
                          '{:.2f}'.format(sold_init),
                          '{:.2f}'.format(dob_lun),
                          '{:.2f}'.format(princ_lun),
                          '{:.2f}'.format(rata_lun),
                          '{:.2f}'.format(sold_final)])
        luna += 1
        sold_init = sold_final

    listeaza.add_row(['Total', '---',
                      '', '', '',
                      '{:.2f}'.format(total_dob_datorate)])

    print(listeaza)
