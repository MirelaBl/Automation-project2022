"""
603 OOP VS
Variabila de clasa --> modificare printr-o metoda
PF - 08.06.2021 v5
"""  #


class Clasa:
    """Atribut clasa / atribut obiect"""

    atribut_clasa = 77

    def __init__(self, atribut_instanta = 10):
        """atribut propriu"""
        self.atribut_instanta = atribut_instanta

    def modifica_atribut_clasa(self, valoare_noua):
        """utilizand nume clasa modifica atributul de clasa"""
        Clasa.atribut_clasa = valoare_noua

    def modif_atribut_instanta(self, noua_val):
        """modifica atributul propriu"""
        self.atribut_instanta = noua_val


# definim un obiect cu valoarea default pentru atribut_instanta
obj1 = Clasa()
print(obj1.atribut_instanta)
print(obj1.atribut_clasa)
print(obj1.__dict__)

# Aplicam metode. Listam noile atribute
obj1.modif_atribut_instanta(20)  # atribuire de valori proprii instantelor
obj1.modifica_atribut_clasa(100)
print(obj1.atribut_instanta)
print(obj1.atribut_clasa)
print(Clasa.atribut_clasa)
print(obj1.__dict__)
