class Test():
    def testeaza(self,x):
        self.x  = x
        self.y = 357

ob= Test()
ob.y= 555

print(ob.y)

ob2=Test()
ob.testeaza(10)
print(ob.y)

"""
class Test:
    def metoda(self,x):
        global a
        a = x

obj = Test()
print(obj.metoda(100))

''''''''''''''''''
class A:
    def aduna(self,x,y,z):
        return self.x + self.y + self.__sizeof__()

obj = A()
obj.aduna(1,3,5)
"""

class Test:
    def __init__(self, a = 10, b=20):
        print(a+b)

ob2= Test(5,7)


class Test1():
    def __init__(self):
        self.p = 888


Test1.p=888
print(Test1.p)