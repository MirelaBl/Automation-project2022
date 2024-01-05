class Test1:
    def metoda1(self):
        self.unu = 'unu'

class Test2(Test1):
    def metoda2(self):
        self.doi ='doi'

class Test3(Test2):
    def metoda3(self):
        self.doi = 'trei'

obj = Test3()
print(obj.metoda1())
print(obj.metoda2())
print(obj.metoda3())

