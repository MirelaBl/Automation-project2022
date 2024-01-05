"""
821 Module
Modulul pymysql - ddl
PF - 29.06.2021 v6
"""  #


import pymysql as mdb

# Credentiale conectare
host = "localhost"
passwd = "paul;Paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"
dbname = "test"

con = mdb.connect(host, user, passwd, dbname)
cursor = con.cursor()

# sterge bd
cursor.execute('DROP DATABASE IF EXISTS test_python')
# creaza bd
cursor.execute('CREATE DATABASE IF NOT EXISTS test_python')
# selecteaza bd
cursor.execute('use test_python')
# creaza tabela autor
cursor.execute("CREATE TABLE autor(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
