"""
602 OOP VS
Variabila de clasa --> atribut propriu dat de o metoda
PF - 08.06.2021 v5
"""  #

# pylint: disable=invalid-name
# pylint: disable=no-member


class Clasa:
    """Atribut clasa / atribut obiect"""

    atribut_clasa = 77

    def __init__(self, atribut_instanta=10):
        """atribut propriu"""
        self.atribut_instanta = atribut_instanta

    def modifica(self, valoare_noua):
        """utilizand self genereaza un atribut propriu, nu modifica atributul de clasa"""
        self.atribut_clasa = valoare_noua

    def modif_atribut_instanta(self, noua_val):
        """modifica (atribuie) atributul propriu"""
        self.atribut_instanta = noua_val


# definim un obiect cu valoarea default pentru atribut_instanta
obj1 = Clasa()
print(obj1.atribut_instanta)
print(obj1.atribut_clasa)
print(obj1.__dict__)

# Aplicam metode. Listam noile atribute
obj1.modif_atribut_instanta(20)  # atribuire de valori proprii instantelor
obj1.modifica(100)
print(obj1.atribut_instanta)
print(obj1.atribut_clasa)
print(Clasa.atribut_clasa)
print(obj1.__dict__)

# Avem acces la atributul instantei doar prin intermediul aceteia, nu si al clasei
print(Clasa.atribut_instanta)  # eroare

# definim un alt obiect, fara sa-i aplicam metode
obj2 = Clasa(5)
obj2.atribut_clasa

print(obj2.__dict__)
