"""
823 Module
Modulul pymysql - UPDATE
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

# UPDATE
cursor.execute("UPDATE Autor SET Name = %s WHERE Id = %s", ("Tudor Arghezi", '4'))

con.commit()

con.close()
