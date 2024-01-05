class Carte:

    def __init__(self,titlu,autor, pagini):
        print(f"O noua carte cu titlu:{titlu}, scrisa de:{autor}")
        self.titlu= titlu
        self.autor = autor
        self.pagini = pagini

    def __len__(self):
        return self.pagini

poezii = Carte("Poezii","Mihai Eminescu",480)

print(len(poezii))
print('____________________')
d = {'k1':'v1', 'k2':'v2'}
if 'v2' in d:
    print('Adev')
else:
    print('False')

print('____________________')
a = '25'
if a.isdigit():
    print('numar')


print('____________________')

if 'ana are mere'>'ana nu are mere':
    print('Ia si tu doua mere')
else:
    print('Vreau si eu mere ')

    print('____________________')

    class A():
        x = 'Test'
        def metoda1(self):
            return A.x.upper()

obj = A()
print(obj.metoda1())
print('____________________')
class Academie1():
    __nota = 10

obj = Academie1()
obj._Academie1__nota
