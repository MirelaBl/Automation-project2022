"""
824 Module
Modulul pymysql - SELECT
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

# DELETE
cursor.execute("Delete from autor where id = 1")

con.commit()

cursor.close()
