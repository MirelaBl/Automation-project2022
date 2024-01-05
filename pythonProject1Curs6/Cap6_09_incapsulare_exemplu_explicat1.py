"""
609 OOP  
Incapsulare - exemplu explicat
PF - 08.06.2021 v5
"""  #


class Masina:
    """Testam metoda privata si atributul privat"""

    def cul_pub(self):  # metoda publica
        """O metoda publica poate avea argumente publice si private"""
        self.culoare_public = 'publica'  # argument public - vizibil
        self.__culoare_privata = 'privata'  # argument privat - nu va fi vizibil

    def listeaza_culoare(self):
        """O metoda publica poate acceasa si argumente private"""
        print(self.__culoare_privata)

    def __listeazaCuloare(self):  # metoda privata, nu poate fi accesata de obiect direct
        """O metoda privata poate avea argumente publice si private"""
        print(self.culoare_public)  # argument public
        print(self.__culoare_privata)  # argument privat

    def apeleaza(self):
        """O metoda publica poate accesa una privata"""
        self.__listeazaCuloare()


obiect_1 = Masina()

print(obiect_1.__dict__)

# Apelam metoda listeaza_culoare
print(obiect_1.cul_pub())  # argumentul public este accesibil

print(obiect_1.__culoare_privata)  # argumentul privat nu este accesibil indiferent cum il apelam
print(obiect_1.culoare_public)

print(obiect_1.__dict__)

print(obiect_1._Masina__culoare_privata)   # putem totusi sa-l apelam cu _Clasa__atributprivat

# nume_instanta._NumeClasa__variabilaPrivata

# Apelam metoda listeaza_culoare

obiect_1.listeaza_culoare()     # atributul privat va fi listat

# Apelam metoda privata __listeazaCuloare

obiect_1.__listeazaCuloare()    # nu poate fi apelata

obiect_1._Masina__listeazaCuloare()     # o apelam prin constructia obiect._Clasa__metodaprivata


# Apelam metoda "apeleaza"

obiect_1.apeleaza() # metoda privata accesata printr-o metoda publica

print(obiect_1.__dict__)

dir(obiect_1)

print(Masina.__dict__)
