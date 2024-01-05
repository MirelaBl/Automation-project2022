"""
704 Module
Modulul os
PF - 15.06.2021 v6
"""  #


import os


os.system('ping 8.8.8.8')  # system comand
os.system('nslookup infoacademy.net')

os.getcwd()  # directorul de unde ruleaza programul
os.chdir('C:/_wt')  # schimba directorul
os.getcwd()
os.chdir('C:\\Users\\paul\\OneDrive\\Documents\\__PyThOn')

os.listdir('C:\\Users\\paul\\OneDrive\\Documents\\__PyThOn\\07_PyP')  # lista cu fisierele din director

for i in os.listdir('c:\\Python37\\lib\\pkg'):		# cautare fisier pe HDD
    if i == 'cub.py':
        from pkg.cub import cub
        print(cub(int(input('introduceti numarul'))))

print(os.linesep)  # returneaza separatorul de linie
print(os.sep)  # returneaza separatorul de directoare

os.mkdir("c:/aae/info")   # creaza directorul
os.mknod('test1.txt')  # creaza fisierul, doar in Linux
os.remove('c:/aae/info/ceva.txt')  # sterge fisierul
os.rmdir('c:/aae/info')      	# sterge directorul, DACA NU ARE FISIERE

# sau, cu comanda de windows:
os.system('rmdir /S /Q c:\\_wt\\test3') 	# sterge directorul CHIAR DACA ARE FISIERE

# new - optional
os.path.getsize('C:\\Users\\paul\\OneDrive\\Documents\\__PyThOn\\guta.txt')
os.path.getctime('guta.txt')  # parte a os.stat	os.stat('0001test.py').st_ctime (creat)
os.path.getmtime('guta.txt')  # modificat
os.path.getatime('guta.txt')  # acces

os.stat('guta.txt')

os.path.isabs('C:\\Users\\paul\\OneDrive\\Documents\\__PyThOn\\guta.txt')  # true daca e cale absoluta

os.path.isfile('C:\\Users\\paul\\OneDrive\\Documents\\__PyThOn\\guta.txt')  # true daca exista

caile = os.path.split('C:\\Users\\paul\\OneDrive\\Documents\\__PyThOn\\guta.txt')
print(caile)
os.path.splitext(caile[1])

for i in os.listdir('C:\\Users\\paul\\OneDrive\\Documents\\__PyThOn\\07_PyP'):
    if os.path.splitext(i)[1] == '.py':
        print(i)
