class A:
    def aduna(self,x,y,z):
        return self.x + self.y + self.z


obj = A()
obj.x = 2
obj.y = 3
obj.z = 5
print(obj.aduna(1,3,5))
