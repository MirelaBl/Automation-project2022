class Test1:
    def metoda1(self):
        self.unu = 'unu'

class Test2(Test1):
    var = '100'
    def metoda2(self):
        self.doi ='doi'

obj = Test2()
print(obj.var)