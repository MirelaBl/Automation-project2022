class A():
    x = 'Test'
    def metoda1(self):
        return A.x.upper()


obj = A()
print(obj.metoda1())
print(A.x)
A.x = 'rezultat'
obj2 = A()
print(obj2.x)
