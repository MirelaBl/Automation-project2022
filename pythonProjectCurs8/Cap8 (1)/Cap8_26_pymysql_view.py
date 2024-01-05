"""
826 Module
Modulul pymysql - VIEW
PF - 29.06.2021 v6
"""  #


import pymysql as mdb

# Credentiale conectare
host = "localhost"
passwd = "paul;Paul"
port = 3306  # normal portul e 3306. Daca e diferit trebuie mentionat acela
user = "root"
dbname = "orase"

con = mdb.connect(host, user, passwd, dbname)

curs2 = con.cursor()

# creare view
curs2.execute("""CREATE OR REPLACE VIEW OraseRomanesti(id, oras) AS
	SELECT CityID, City
	FROM cities JOIN countries USING(countryid)
	WHERE admin_code != 'SUB' AND country = 'Romania'""")

# utilizare
curs2.execute('SELECT * FROM oraseromanesti ORDER BY 2')

rezultat = curs2.fetchall()

'''afisare tabel'''
print('{:<20}'.format('id'), '{0}'.format('loc').ljust(20))
print('*'*35)
for row in rezultat:
	idl = row[0]
	loc = row[1]
	print('{:<20}'.format(idl), '{0}'.format(loc).ljust(20))
print('*'*35)

con.close()
