class Test1():
    def metoda(self):
        print('1')

class Test2(Test1):
    def metoda(self):
        print('2')


obj = Test2()
obj.metoda()

obj = Test1()
obj.metoda()

import os
#os.rmdir('C:/Users/Mirela/Desktop/t1') 
os.remove('C:/Users/Mirela/Desktop/t1/text.txt.txt')

