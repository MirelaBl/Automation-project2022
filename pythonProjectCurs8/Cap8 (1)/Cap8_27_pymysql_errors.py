"""
827 Module
Modulul pymysql - erori
PF - 29.06.2021 v6
"""  #

import pymysql as mdb
import sys

# Credentiale conectare
host = "localhost"
passwd = "paul;Paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"
dbname = "world"

con = ''
output = ''

try:
    con = mdb.connect(host, user, passwd, dbname, port)
    cur = con.cursor()
    nr_rd = cur.execute("SELECT name FROM city WHERE countrycode = 'ROM'")
    output = cur.fetchall()

except mdb.Error as e:
    print(str(sys.exc_info()))
    print("Error {0}: {1}".format(e.args[0], e.args[1]))

else:
    print(nr_rd)
    print("Output : {0}".format(output))

finally:
    if output:
        for i in output:
            print(i[0])
