"""
805 Module
Modulul ftplib - exemple
PF - 29.06.2021 v6
"""  #


import sys
sys.path.append("C:\\Users\\admin\\Documents\\__PyThOn\\0 PyP\\_module")  # pt pftp
import ftplib
import pftp  # pftp e modul propriu

# Conectare
host = 'ftp.infoacademy.net'
ftp = ftplib.FTP(host)
ftp.login ('paul@infoacademy.net', pftp.parol)

# lista fisiere/directoare existente in directorul principal
ftp.retrlines('LIST')

# sterge directorul
ftp.rmd('Info-test')

# sterge fisierul
ftp.delete('text11.txt')

# creaza directorul
ftp.mkd('Info-test')

# returneaza dir curent
ftp.pwd()

# schimba directorul
ftp.cwd('/Info-test')
ftp.retrlines('LIST')
ftp.cwd('/')

# upload fisier
file = 'text1.txt'
ftp.storbinary('STOR ' + 'text11.txt', open(file, 'rb'))

# download fisier
ftp.retrbinary('RETR text11.txt', open('c:/_wt1/abc/t12.csv', 'wb').write)

# iesire
ftp.quit()
