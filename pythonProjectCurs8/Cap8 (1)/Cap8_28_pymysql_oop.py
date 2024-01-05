"""
828 Module
Modulul pymysql - oop - clasa db
PF - 29.06.2021 v6
"""  #


import pymysql as mydb

# Credentiale conectare
host = "localhost"
passwd = "paul;Paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"

connect = mydb.connect(passwd=passwd, user=user, host=host, port=port)
cursor = connect.cursor()


class Db:

    def select(self, baza_de_date, select_var='show tables'):
        '''Functia select primeste ca parametri:
            - baza de date
            - instructiunea select (poate primi si instructiuni SHOW...)
        si returneaza result set-ul corespunzator'''  #
        cursor.execute('Use ' + baza_de_date)
        cursor.execute(select_var)
        result = cursor.fetchall()
        return result

    def select_lista(self, baza_de_date, select_var='show tables'):
        '''selecteaza o coloana si returneaza o lista cu valorile'''  #
        cursor.execute('Use ' + baza_de_date)
        cursor.execute(select_var)
        result = cursor.fetchall()
        var1 = []
        for i in result:
            var1.append(i[0])
        return var1

    def query(self, baza_de_date, interogare):
        '''Functia delete primeste ca parametri:
            - baza de date
            - instructiunea deleet
        si sterge...'''  #
        cursor.execute('Use ' + baza_de_date)
        cursor.execute(interogare)
        connect.commit()

if __name__ == "__main__":
	pass