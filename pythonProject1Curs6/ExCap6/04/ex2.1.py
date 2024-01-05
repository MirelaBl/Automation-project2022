class Test1:
    def metoda1(self):
        self.unu = 'unu'

class Test2(Test1):
    def metoda2(self):
        self.doi ='doi'

class Test3(Test2):
    def metoda3(self):
        self.doi = 'doi'



ob =Test3()
print(ob.doi)