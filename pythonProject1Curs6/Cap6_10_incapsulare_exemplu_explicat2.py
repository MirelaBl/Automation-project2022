"""
610 OOP  
Incapsulare - exemplu explicat 2
PF - 08.06.2021 v5
"""  #

class Car:

    def __init__(self):
        self.__maxspeed = 200
        # self.__name = "Supercar"

    def drive(self):
        print('driving with maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed


redcar = Car()
redcar.drive()
redcar._Car__maxspeed


redcar.__maxspeed = 350      # nu putem s-o schimbam direct, e privata
redcar.drive()


redcar.setMaxSpeed(320)     # ... doar prin intermediul unei metode
redcar.drive()

print(redcar.__maxspeed)

print(redcar._Car__maxspeed)

print(redcar.__dict__)

redcar._Car__maxspeed = 150
