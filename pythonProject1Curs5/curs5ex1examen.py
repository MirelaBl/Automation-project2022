class Test():
    def __str__(self):
        self.x = 333
        return str(self.x)

    def a (self,x):
        print(str(self.z)+'a'+str(x))


    def b (self,y=''):
        print('b'+str(y))

a1 = Test()
#a1.a('papa')
a1.b('baba')
print('-----------')

a1.z = 5
a1.a('papa')


print('*********')


obj_test = Test()
print(obj_test)


obj = Test()
obj
print(obj)

print('*********')

