""" 209 IF
Utilizarea if
PF - 20.07.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement

enunt = """
Schimb valutar RON -> EUR sau EUR -> RON
- introducem valuta dorita si schimbam in caractere mari
- testeaza daca introducem corect numele valutei (caractele alpha)
- testeaza daca am introdus valuta corecta RON sau EUR
- introducem suma. Testeaza daca am introdus suma corect (cifre)
si o transforma in intreg- returneaza suma si valuta sau mesaj de eroare
"""  #


def scb_val():
    """Schimb valutar"""

    valuta = input('Introduceti RON pentru conversia Euro in Lei sau EUR pt. conversia  Lei in Euro: ').upper()

    curs = 4.93

    if valuta.isalpha():
        if valuta == 'RON':
            euro = input('Cati euro schimbati? ')
            if euro.isdigit():
                euro = int(euro)
                print('Ati primit', '%.2f' % float(euro * curs), 'RON')
            else:
                print('Nu ati introdus un numar intreg valid!')

        elif valuta == 'EUR':
            lei = input('Cati lei schimbati? ')
            if lei.isdigit():
                lei = int(lei)
                print('Ati primit', '%.2f' % float(lei / curs), 'EURO')
            else:
                print('Nu ati introdus un numar valid!')

        else:
            print('Valuta inexistenta!')
            scb_val()
    else:
        print('Valoarea introdusa poate fi RON sau EUR!')
        scb_val()

scb_val()

# putem pune totul intr-o functie si o apelam ori de cate ori avem nevoie

input('Apasa <enter> pt a iesi')
