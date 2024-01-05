class Test1:
    def metoda1(self, x):
        self.x = x

class Test2(Test1):
    def metoda1(self, y):
        self.y =y

ob1 = Test1()
ob2 = Test2()

print(ob1.metoda1(22))
print(ob2.metoda1(33))