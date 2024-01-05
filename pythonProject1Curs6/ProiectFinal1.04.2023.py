# 571 Clase
# Clase
# PF - 10/08/2016
import smtplib

import pygal
import os
import re

'''
Importati functia datetime din modulul datetime. Instructiune scrisa deja (vezi mai jos)

Creati o clasa 'Stoc' care va avea:
  - o metoda constructor cu
        denumire produs
        categoria
        unitatea de masura default 'Buc'
        sold default 0
        initializati trei dictionare, cu cheie comuna (numerica), pentru data op.,
    intrari si iesiri din stoc, care vor fi atribuite fiecarei instante

  - o metoda intrari cu
        cantitatea,
        data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )
        testati daca exista chei in dictionarul cu data op. Daca exista stabileste cheia curenta
    ca fiind maximul cheilor existente plus 1, altfel va fi egala cu 1
        introduce in dict intrari cheie si cant
        introduce in dict data cheie si data op
        actualizeaza soldul

  - o metoda iesiri, similara cu precedenta. Diferente: populam dict iesiri

  - o metoda fisa produsului cu urmatoarele specificatii:
        Sa printeze 'Fisa produsului "denumire_produs"' (sa stim si noi a cui e fisa)
        Sa printeze ' Nrc ', '  Data  ', ' Intrare', ' Iesire' pentru toate tranzactiile produsului
        Sa printeze stocul actual al produsului
        pentru avansati - aliniati coloanele

Creati trei instante (produse). Pentru 2 din ele efectuati cate 4-5 operatiuni (intrari, iesiri)

Apelati metoda fisa produsului pentru cele 2 produse
''' #

from datetime import datetime

class Stoc:
    """Tine stocul unui depozit"""

    def __init__(self, prod, categ, um='Buc', sold=0, soldMin=30):
        self.prod = prod			# parametri cu valori default ii lasam la sfarsitul listei
        self.categ = categ  		# fiecare instanta va fi creata obligatoriu cu primii trei param.
        self.sold = sold			# al patrulea e optional, soldul va fi zero
        self.um = um
        self.i = dict()				# fiecare instanta va avea trei dictionare intrari, iesiri, data
        self.e = dict()				# pentru mentinerea corelatiilor cheia operatiunii va fi unica
        self.d = dict()
        self.p = dict()
        self.soldMin = soldMin


    def pretMediuIntrare(self):
        if len(self.d.keys()) == 0:
            return -1 # dam o valoare fictiva care semnalizeaza lipsa tuturor tranzactiilor de tip data
        if len(self.i.keys()) == 0:
            return -1 # dam o valoare fictiva care semnalizeaza lipsa tuturor tranzactiilor de iesire


        totalCheltuit = 0
        totalCantitate = 0
        for v in self.i.keys():
            totalCheltuit += round(self.i[v] * self.p[v], 2)
            totalCantitate += self.i[v]

        return round(totalCheltuit/totalCantitate, 2)


    def intr(self, cant, pretUnitar, data=str(datetime.now().strftime('%Y%m%d'))):
        self.pretUnitar = pretUnitar
        self.data = data
        self.cant = cant
        if self.sold < self.soldMin:
            self.avertizare("inainte intrare de marfa")
        self.sold += cant          # recalculam soldul dupa fiecare tranzactie
        if self.d.keys():               # dictionarul data are toate cheile (fiecare tranzactie are data)
            cheieNOUA = max(self.d.keys()) + 1
        else:
            cheieNOUA = 1
        self.i[cheieNOUA] = cant       # introducem valorile in dictionarele de intrari si data
        self.d[cheieNOUA] = self.data
        self.p[cheieNOUA] = self.pretUnitar
        if self.sold < self.soldMin:
            self.avertizare("dupa intrare de marfa")

    def pretMediuIesire(self):
        if len(self.d.keys()) == 0:
            return -1 # dam o valoare fictiva care semnalizeaza lipsa tuturor tranzactiilor de tip data
        if len(self.e.keys()) == 0:
            return -1 # dam o valoare fictiva care semnalizeaza lipsa tuturor tranzactiilor de iesire


        totalVanzari = 0
        totalCantitate = 0
        for v in self.e.keys():
            totalVanzari += round(self.e[v] * self.p[v], 2)
            totalCantitate += self.e[v]

        return round(totalVanzari/totalCantitate, 2)


    def iesi(self, cant, pretUnitar = 0, data=str(datetime.now().strftime('%Y%m%d'))):
        if pretUnitar == 0:
            self.pretUnitar = self.pretMediuIesire()

        #   datetime.strftime(datetime.now(), '%Y%m%d') in Python 3.5
        self.data = data
        self.cant = cant
        #punctul 2 soldMin
        if self.sold < self.soldMin:
            self.avertizare("inainte iesire de marfa")
            return
        self.sold -= self.cant
        # DACA EXISTA CHEIE IN DICTIONARE DE DATE CALENDARISTICE
        if self.d.keys():
            cheieNOUA = max(self.d.keys()) + 1
            # CHEIA NOUA VA FI CEA MAI MARE CHEIE EXISTENTA + 1
        else:
            cheieNOUA = 1
            # DACA NU EXISTA UNA DEJA ATUNCI CHEIA NOUA VA FI 1
        self.e[cheieNOUA] = self.cant       # similar, introducem datele in dictionarele iesiri si data
        self.d[cheieNOUA] = self.data
        self.p[cheieNOUA] = self.pretUnitar
        if self.sold < self.soldMin:
            self.avertizare("dupa iesire de marfa")

    def fisap(self):

        print('Fisa produsului ' + self.prod + ': ' + self.um)
        print(40 * '-')
        print(' Nrc ', '  Data ', 'Intrari', 'Iesiri','    Pret')
        print(40 * '-')
        for v in self.d.keys():
            if v in self.i.keys():
                print(str(v).rjust(5), self.d[v], str(self.i[v]).rjust(6), str(0).rjust(6),
                      str(self.p[v]).rjust(6), str(round(self.p[v] * self.i[v], 2)).rjust(10))
            else:
                print(str(v).rjust(5), self.d[v], str(0).rjust(6), str(self.e[v]).rjust(6),
                      str(self.p[v]).rjust(6), str(round(self.p[v] * self.e[v], 2)).rjust(10))

        print(40 * '-')
        print('Stoc actual:      ' + str(self.sold).rjust(10))
        print(40 * '-' + '\n')

    def totalAchizitii(self):
        if len(self.d.keys()) == 0:
            return 0
        if len(self.i.keys()) == 0:
            return 0

        totalIntrari = 0
        for v in self.i.keys():
            totalIntrari += round(self.i[v] * self.p[v], 2)

        return round(totalIntrari, 2)

    def vanzariTotale(self):
        if len(self.d.keys()) == 0:
            return 0
        if len(self.e.keys()) == 0:
            return 0


        totalVanzari = 0
        for v in self.e.keys():
            totalVanzari += round(self.e[v] * self.p[v], 2)

        return round(totalVanzari, 2)

    def grafic(self,fisier):

        puncte=[]
        for v in self.d.keys():
            if v in self.i.keys():
                w = {'value': self.i[v],'color':'red'}
            else:
                w = {'value': self.e[v],'color':'blue'}
            puncte.append(w)

        ob_chart.add('Stoc produs', puncte)

        ob_chart.render_to_file(fisier)  # salvare fisier grafic
        os.system(fisier)  # deschide fisierul

    def avertizare(self, mesaj):
            print(mesaj)
            print('soldul de', self.sold, ' este sub soldul minim de ', self.soldMin, sep=' ')
            print(40 * '-' + '\n')

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

            parola = '123test123test123'
            print(expeditor, destinatar, subiect);
            try:
                 smtp_ob = smtplib.SMTP('mail.gmx.com:587')
                 smtp_ob.starttls()  # protocol criptare
                 smtp_ob.login(username, parola)
                 for i in destinatar:
                        smtp_ob.sendmail(expeditor, i, mesaj)
                        print(f'Mesaj to {i} expediat cu succes!')
                        smtp_ob.close()
            except:
                 print(f'Mesajul  expediat catre {expeditor} de catre {destinatar} nu a putut fi expediat!')
                 print(40 * '-')

    def  cauta(self, expRe):
        rezultatCautare = re.match('\S'+expRe+'\S+', self.prod)
        if rezultatCautare :
            return True
        else:
            return False

    def cautaTranzactie(self,exp):
        listaRez = []
        for v in self.d.keys():
            if v in self.i.keys():
                vtr = round(self.i[v] * self.p[v], 2) # vtr -- valoare tranzactiei numerica
                vstr = str(vtr)
                rezultatCautare = re.findall('\S+90\S+', vstr)
                if rezultatCautare:
                    listaRez.append([self.prod, "intrare", self.p[v], self.i[v]])
            else:
                vtr = round(self.e[v] * self.p[v], 2)  # vtr -- valoare tranzactiei numerica
                vstr = str(vtr)
                rezultatCautare = re.findall('\S+90\S+', vstr)
                if rezultatCautare:
                    listaRez.append([self.prod, "iesire", self.p[v], self.e[v]])
        return listaRez

print('punctul1')
fragute = Stoc('fragute', 'fructe', 'kg')       # cream instantele clasei
lapte = Stoc('lapte', 'lactate', 'litru')
ceasuri = Stoc('ceasuri', 'ceasuri')


fragute.sold                    # ATRIBUTE
fragute.prod
fragute.intr(100, 8) # 0+100 sold nou 100
fragute.iesi(73, 9) # 100-73 = 27
fragute.intr(100, 5) # 100+27 = 127
fragute.iesi(85,7) #127 -85 = 42
fragute.intr(100, 7) #42+100 = 142
fragute.iesi(101 ) #142 -101 = 41

fragute.d                       # dictionarele produsului cu informatii specializate
fragute.i
fragute.e

fragute.sold
fragute.categ
fragute.prod
fragute.um
fragute.fisap()


print(40 * '-')
print('punctul6')
print('fragute totalAchizitii: ', fragute.totalAchizitii())
print(40 * '-')
print('punctul 6')
print('fragute vanzariTotale: ', fragute.vanzariTotale())

print(40 * '-')
print('punctul 6')
print('pret Mediu Iesire pt fragute: ', fragute.pretMediuIesire())
print(40 * '-')


print('punctul 6')
print('pret Mediu Intrare pt fragute: ', fragute.pretMediuIntrare())
print(40 * '-')

print('punctul 4')
if fragute.cauta('rag'):
    print('s-a gasit :', fragute.prod)
    print(40 * '-')

else:
    print('nu s a gasit')
    print(40 * '-')



ls = lapte.cautaTranzactie('90')
print(ls)

print(40 * '-')

lapte.intr(1500, 4)
lapte.iesi(975, 5)
lapte.intr(1200, 7)
lapte.iesi(1490, 8)
lapte.intr(1000, 8)
lapte.iesi(1200, 9)

lapte.fisap()

l = [fragute, lapte, ceasuri]

for i in l:
    i.fisap()

print('punctul 4')
for i in l:
    g = i.cauta('rag')  # g de la gasit
    if g:
        print('s-a gasit "rag" in : ', i.prod)

    '''
    1. Adaugati o metoda in clasa Stoc care sa ofere o proiectie grafica a intrarilor si iesirilor intr-o
anumita perioada, pentru un anumit produs;	--pygal-- '''
 #exemplu  pygal.Bar
ob_chart = pygal.Bar()  # creare obiect - grafic cu bare verticale alaturate
#ob_chart.add('Grafic12', (print(fragute.i.values())))  # adaugare date nepermisa de functia add
#ob_chart.add('Grafic12', (print(fragute.e.values())))  # adaugare date nepermisa de functia add


''' 
#var1 
ob_chart.add('Stoc produs', [

 {'value': 73, 'color': 'red'},
 {'value': 100, 'color': 'rgba(0,128,0, .6)'},
 {'value': 85, 'color': 'red'},
 {'value': 100, 'color': 'rgba(0,128,0, .6)'},
{'value': 101, 'color': 'red'},
{'value': 100, 'color': 'rgba(0,128,0, .6)'},
])

ob_chart.render_to_file('grafic2023.svg')  # salvare fisier grafic

os.system('grafic2023.svg')  # deschide fisierul
'''
print('punctul1')
print('pentru continuare inchide graficul!!')
fragute.grafic("grafic042023.svg")
print(40 * '-')



'''2. Adaugati o solutie in clasa Stoc care sa va avertizeze automat cand stocul 
unui produs este mai mic decat o 
limita minima, predefinita per produs.
Limita sa poata fi variabila (per produs). Preferabil sa 
transmita automat un email de avertizare;'''


'''3. Adaugati o metoda in clasa Stoc care sa transmita prin email diferite informatii(
de exemplu fisa produsului) ; 	--SMTP--

4. Adaugati o metoda in clasa Stoc care sa utilizeze Regex pentru a cauta :
    - un produs introdus de utilizator;
    - o tranzactie cu o anumita valoare introdusa de utilizator;	--re--

5. Completati aplicatia astfel incat sa permita introducerea pretului la fiecare intrare si iesire.
Pretul de iesire va fi pretul mediu ponderat (la fiecare tranzactie de intrare se va face o medie intre
pretul produselor din stoc si al celor intrate ceea ce va deveni noul pret al produselor stocate).
Pretul de iesire va fi pretul din acel moment;  

6. Creati trei metode noi, diferite de cele facute la clasa, testati-le si asigurati-va ca functioneaza cu succes;'''

''' 
def DatoriiLaFurnizor( DatoriiLaFurnizor):
    return DatoriiLaFurnizor

visine = Stoc('visine', 'fructe', 'kg')
visine2 = Stoc('visine2', 'fructe', 'kg')
print("visine.DatoriiLaFurnizor")
print(visine.DatoriiLaFurnizor)
print("visine.DatoriiLaFurnizor")
print(visine2.DatoriiLaFurnizor)
visine.DatoriiLaFurnizor(2)
'''







