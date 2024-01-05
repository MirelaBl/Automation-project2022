# 571 Clase
# Clase
# PF - 10/08/2016

import pygal
import os
import sys
#sys.path.append("C:\\Users\\Default\\Documents\\__PyThOn\\0 PyP\\_module")    # pt pftp
#import pftp
import smtplib
import re

class Stoc:
    """Tine stocul unui depozit"""

    def __init__(self, prod, categ,pret, um='Buc'):
        self.prod = prod			# parametri cu valori default ii lasam la sfarsitul listei
        self.categ = categ       # fiecare instanta va fi creata obligatoriu cu primii trei param.
        self.pret = pret         # adaugat pret
        self.um = um


        self.DatoriiLaFurnizor = 180

    def __str__(self):
        """afiseaza """
        return "pretul pe kg de {0} este de {1} lei".format(
                str(self.prod),
                str(self.pret))


visine = Stoc('visine', 'fructe', 'kg')       # cream instantele clasei

dictintrari = {0: 20, 1: 30, 2: 55}
dictiesiri={0: 10, 1: 28, 2: 60}



print(40 * '-')
visine.prod
print('In aplicatia Stoc produsul este: '+visine.prod)
print('punctul1'+20 * '-')
print('atentie trebuie sa inchideti graficul!!')

'''1. Adaugati o metoda in clasa Stoc care sa ofere o proiectie grafica a intrarilor si iesirilor intr-o
anumita perioada, pentru un anumit produs;	--pygal--'''
#exemplu  pygal.Bar
ob_chart = pygal.Bar()  # creare obiect - grafic cu bare verticale alaturate
#ob_chart.add('Grafic12', (print(fragute.i.values())))  # adaugare date nepermisa de functia add
#ob_chart.add('Grafic12', (print(fragute.e.values())))  # adaugare date nepermisa de functia add

ob_chart.add('Stoc produs', [

 {'value': 73, 'color': 'red'},
 {'value': 100, 'color': 'rgba(0,128,0, .6)'},
 {'value': 85, 'color': 'red'},
 {'value': 100, 'color': 'rgba(0,128,0, .6)'},
{'value': 101, 'color': 'red'},
{'value': 100, 'color': 'rgba(0,128,0, .6)'},
])

ob_chart.render_to_file('grafic2023.svg')  # salvare fisier grafic

os.system('../grafic2023.svg')  # deschide fisierul
#os.system('grafic2023.svg').close() nu merge cu close

'''2. Adaugati o solutie in clasa Stoc care sa va avertizeze automat cand stocul unui produs este mai mic decat o 
limita minima, predefinita per produs. Limita sa poata fi variabila (per produs). Preferabil sa 
transmita automat un email de avertizare;'''
print(40 * '-')
print('punctul2'+20 * '-')
print('dictionar intrari visine: ')
print(dictintrari.values())
print('dictionar iesiri visine: ')
print(dictiesiri.values())
print('cantit min intrari visine: 25 kg')
min = 25
print('cantit max intrari visine:50 kg')
max =50
print(40 * '-')

for v in dictintrari.values():
        if v < min:
            print('cantitate intrari visine:')
            print(v)
            print(' se trimite email')
        elif v > max:
            print('cantitate intrari visine:')
            print(v)
            print(' se trimite email')


for v in dictiesiri.values():
    if v < min:
        print('cantitate iesiri visine:')
        print(v)
        print(' se trimite email')
    elif v > max:
        print('cantitate iesiri visine:')
        print(v)
        print(' se trimite email')

print('punctul3'+20 * '-')

'''3. Adaugati o metoda in clasa Stoc care sa transmita prin email diferite informatii(
de exemplu fisa produsului) ; 	--SMTP--'''

expeditor = 'bmirela306@gmx.at'
destinatar = 'mirela.blaschke@gmail.com'
username = 'bmirela306@gmx.at'
subiect = 'ceva'
mesaj = """From: {0}
To: {1}
Subject: {2}
Content-type: text/html
<html>
Salut,
 	<head>
		<title></title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
		<link href="../../../default.css" rel="stylesheet" type="text/css" />
	</head>
	<body style="background:none;margin:0px">
 	    <h1 class=jobstitle>TEST test</h1>
	</body>
<p>Paul</p>
</html>
""".format(expeditor, destinatar, subiect)

parola= '123test123test123'
print(expeditor, destinatar, subiect);
try:
	smtp_ob = smtplib.SMTP('mail.gmx.com:587')
	smtp_ob.starttls()  						# protocol criptare
	smtp_ob.login(username, parola)
	for i in destinatar:
		smtp_ob.sendmail(expeditor, i, mesaj)
		print(f'Mesaj to {i} expediat cu succes!')
	smtp_ob.close()

except:
		print(f'Mesajul  expediat catre {expeditor} de catre {destinatar} nu a putut fi expediat!')
print(40 * '-')

'''4. Adaugati o metoda in clasa Stoc care sa utilizeze Regex pentru a cauta :
    - un produs introdus de utilizator;
    - o tranzactie cu o anumita valoare introdusa de utilizator;	--re--'''
print('punctul4'+20 * '-')
x = input('introdu o propozitie care sa contina urmatoarele produse mere, pere, ardei:')
print(x)
searchWithRe = re.findall('\S+er\S+', x)  # cauta toate aparitiile de forma 'er'
print('cauta toate aparitiile de forma "er":' )
print(searchWithRe)
print(20 * '-')
# cauta cuv cu 'er' in input dat
input = 'pretul pe kg de mere este de 8 lei'
searchWithRe = re.findall('\S+er\S+', input)  # cauta toate aparitiile de forma 'er'
print('cauta toate aparitiile de forma "er":' )
print(searchWithRe)
'''5. Completati aplicatia astfel incat sa permita introducerea pretului la fiecare intrare si iesire.
Pretul de iesire va fi pretul mediu ponderat (la fiecare tranzactie de intrare se va face o medie intre
pretul produselor din stoc si al celor intrate ceea ce va deveni noul pret al produselor stocate).
Pretul de iesire va fi pretul din acel moment; '''
print('punctul5'+20 * '-')
mere = Stoc('mere', 'fructe',8, 'kg')
print(mere.categ)
print(mere.prod)
print(mere.pret)
print(mere.__str__())

pere = Stoc('pere', 'fructe',12, 'kg')
print(pere.__str__())
'''6. Creati trei metode noi, diferite de cele facute la clasa, testati-le si asigurati-va ca functioneaza cu succes;'''
print('punctul6'+20 * '-')
def DatoriiLaFurnizor( DatoriiLaFurnizor):
    return DatoriiLaFurnizor

visine2 = Stoc('visine2', 'fructe', 'kg')
print('DatoriiLaFurnizorinBani:')
print(visine2.DatoriiLaFurnizor)







