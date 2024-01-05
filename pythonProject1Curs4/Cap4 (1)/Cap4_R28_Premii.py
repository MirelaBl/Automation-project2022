"""
428
Exercitii - Premii
PF 03.12.2020 v4
"""  #

# pylint: disable=invalid-name

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


def premii(valoare, nr_participanti):
    """Calculeaza premiile si impozitele unui concurs"""
    lista = []
    if nr_participanti < 3:
        print('Concurs anulat!')
    elif nr_participanti < 11:
        lista = [50, 35, 15]
    elif nr_participanti < 31:
        lista = [40, 30, 10, 10, 10]
    else:
        lista = [30, 20, 15, 5, 5, 5, 5, 5, 5, 5]

    if lista:
        total_impozit = 0
        for i, j in enumerate(lista, start=1):
            premiu_brut = valoare * j / 100
            premiu_net = premiu_brut
            if premiu_brut > 10000:
                premiu_net = premiu_brut * .9
                total_impozit += premiu_brut * .1
            print('Premiul {:2d}:'.format(i), premiu_net)
        print(total_impozit)


premii(100000, 35)
