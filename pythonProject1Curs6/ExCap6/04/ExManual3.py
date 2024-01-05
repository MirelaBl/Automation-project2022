#incapsularea #

class Demo:
    """Testeam metoda privata si atributul privat"""

    def set_public(self):
        """o met publica care poate avea arg public si private"""
        self.public = 'publica'
        self.__privat = 'privata'

    def get_public(self):
        """o metoda publica care poate acessa si arg private"""
        print(self.__privat)

    def __get_restrict(self):
        """o med privata care poate avea arg public"""
        print(self.public)   #argument public
        print(self.__privat) #argument privat

    def get_access(self):
        """o metoda publica care poate accessa una privata"""
        self.__get_restrict()

ob1 = Demo()

ob1.set_public()
print(ob1.public) #atribut public accesibil direct
print('§§§§§§§§§')
ob1.get_public()
print('*****************')
ob1.get_access()
print('!!!!!!!!')
