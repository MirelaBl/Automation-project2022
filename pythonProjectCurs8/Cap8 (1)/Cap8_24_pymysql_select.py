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

# SELECT
# interogare select
autor = 'select * from autor'
# executa instructiunea
cursor.execute(autor)
# obtine un tuplu cu rezultatul
rezultat = cursor.fetchall()
print(list(rezultat))

# obtine lista cu numele de coloane din tabela
descr = cursor.description
coloane = [descr[0][0], descr[1][0]]

# prelucreaza rezultatele
print (coloane[0], coloane[1])
for row in rezultat:
    print (str(row[0]), row[1])

# sau
for row in rezultat:
    print(coloane[0] + ': ' + str(row[0]), coloane[1] + ': ' + str(row[1]))

cursor.close()
