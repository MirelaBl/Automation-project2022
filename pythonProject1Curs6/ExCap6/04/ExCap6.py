class Clasa:
    """clasa """
    atribut_clasa = 77

    def __init__(self, atribut_instanta = 10):
        self.atribut_instanta = atribut_instanta

    def modifica_atribut_clasa(self, valoare_noua):
        self.atribut_clasa= valoare_noua

    def modifica_atribut_instanta(self, val_noua):
        self.atribut_instanta = val_noua


obj1 = Clasa()
print("obj1.atribut_clasa")
print(obj1.atribut_clasa)
print("obj1.atribut_instanta")
print(obj1.atribut_instanta)
# Aplicam metode.
obj1.modifica_atribut_clasa(33)
obj1.modifica_atribut_instanta(55)
print("obj1.atribut_clasa")
print(obj1.atribut_clasa)
print("obj1.atribut_instanta")
print(obj1.atribut_instanta)
print("Clasa.atribut_clasa")
print(Clasa.atribut_clasa)