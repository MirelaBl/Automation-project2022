"""
822 Module
Modulul pymysql - INSERT
PF - 29.06.2021 v6
"""  #


import pymysql as mdb

# Credentiale conectare
host = "localhost"
passwd = "paul;Paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"
dbname = "test_python"

con = mdb.connect(host, user, passwd, dbname)
cursor = con.cursor()

# INSERT
cursor.execute("INSERT INTO autor(Name) VALUES('Marin Sorescu'),('Nichita Stanescu')")
cursor.execute("INSERT INTO autor(Name) VALUES('Lucian Blaga')")
cursor.execute("INSERT INTO autor(Name) VALUES('George Toparceanu')")
a = "'Mircea Cartarescu'"
y = "INSERT INTO Autor(Name) VALUES({0})".format(a)
cursor.execute(y)
x = "INSERT INTO Autor(Name) VALUES({0})".format('"Mihai Eminescu"')
cursor.execute(x)

con.commit()

con.close()
