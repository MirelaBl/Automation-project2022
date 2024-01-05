class Person:
    def __init__(self, nume, varsta):
       self.nume = nume
       self.varsta = varsta

    def __str__(self):
        return f'{self.nume} is {self.varsta} y o '

person1 = Person("Mary",27)
print(person1)