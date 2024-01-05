"""
429
Exercitii - Credit cu rate fixe
PF 18.09.2020 v4
"""  #

# pylint: disable=invalid-name

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
