"""
806 Module
Modulul ftplib - exemple
PF - 29.06.2021 v6
"""  #


from ftplib import FTP

ftp = FTP('ftp.ubuntu.com')
ftp.login()

# change into "ubuntu" directory
ftp.cwd('ubuntu')
ftp.cwd('restricted')
ftp.cwd('/')

# Lista fisiere disponibile
ftp.retrlines ('LIST')

# download fisier - alta varianta
deschide = open ('c:/_wt1/project', 'wb' )

ftp.retrbinary('RETR ' + 'ubuntu', deschide.write )

ftp.quit()


# alt host public
host ="test.rebex.net"
ftp = FTP(host)
ftp.login("demo", "password")

# lista fisiere/directoare existente in directorul principal
ftp.retrlines('LIST')

# returneaza dir curent
ftp.pwd()

# schimba directorul
ftp.cwd('/pub/example')
ftp.retrlines('LIST')

# download fisier
ftp.retrbinary('RETR mime-explorer.png', open('c:/_wt1/abc/mm.png', 'wb').write)

# iesire
ftp.quit()
