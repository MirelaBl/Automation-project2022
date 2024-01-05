"""
423
Formatarea stringurilor
PF 04.09.2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=global-statement

enunt = """
# ------------------------------------------------------------------------------------------#
# Creati o aplicatie bancara, pentru incasari si plati in contul clientilor						    #
# clientii n-ar fi incantati sa primeasca/plateasca o suma aproximativa generata de float,  #
# asa ca banca tine evidenta conturilor in subunitati monetare (bani -> 1 leu = 100 bani)   #
# asta inseamna ca putem utiliza numere intregi in tranzactii, iar cand dorim sa afisam     #
# impartim rezultatul suma / 100 					                                        #
# ------------------------------------------------------------------------------------------#"""

sold = 0

def bank(valoare, tip_operatiune='incasare'):
    """
    valoare: suma incasata sau platita
    tip_operatiune: incasare, plata
    """  #
    global sold
    if tip_operatiune == 'incasare':
        sold += valoare
        print('Ati incasat {:.2f} lei'.format(valoare/100))  # formatare cu .format
    elif tip_operatiune == 'plata':
        sold -= valoare
        print('Ati achitat {:.2f} lei'.format(valoare/100))  # formatare cu .format
    else:
        print('Operatiune imposibila!')
    print(f'Soldul dv este de {sold/100 :.2f}')  # formtare cu fprint

bank(100125, 'incasare')
bank(99753, 'plata')

input('Apasa <enter> pentru a iesi.')
