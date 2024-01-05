class Test1:
    def metoda1(self):
        self.unu = 'unu'

class Test2(Test1):
    var = 'soare'
    def metoda2(self):
        self.doi ='doi'

obj = Test1()
print(obj.var)
