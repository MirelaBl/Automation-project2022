"""
802 Module
Modulul re - exemple
PF - 27.06.2021 v6
"""  #


import re
import os


# Cautare in text cu re.search() - cauta in linie, toate liniile care contin From
fisier = open('text1.txt')

count = 0
for line in fisier:
    line = line.rstrip()
    if re.match('^From: ', line):
        count +=1
        print(line)
print(count)


# Cautare in text cu RE - cauta in linie, toate liniile incep cu From, dar ne intereseaza doar e-mail
fisier.seek(0)
lista_email = []
for line in fisier:
    line = line.rstrip()
    email =  re.findall('^From: (\S+@\S+\.\S{2,4})', line)
    if email:
        lista_email += email
print(lista_email)
print(len(lista_email))


# cauta toate numerele (nu doaar cifrele)
a = '''Astazi sunt 22 grade celsius dimineata 32 la pranz si 30 seara. La noapte vor fi doar 20 grade.'''
masurare = re.findall('[0-9]+', a)  # returneaza toate aparitiile intr-o lista
moment = ['dim', 'pranz', 'seara', 'noaptea']
temp = dict(zip(moment, masurare))
print(temp)


# cauta diverse
c = 'Adresa mea de email este paul@infoacademy.net sau paul@fratila.ro si numarul de ttelefon telefonist ...ton '
d = re.findall('\S+@\S+', c)  # cauta toate aparitiile de forma e-mail
print(d)
e = re.findall('\s(t[a-z]+n)\s',  c)  # returneaza cuvinte care incep cu t si se termina cu n, delimitate de spatii
print(e)
f = re.findall('\W([t][a-z]*[n])\W', c)  # cuvinte care incep cu t si se termina cu n, delimitate de caractere non alnum
print(f)


# extrage domeniu din e-mail
c = 'Email: paul@infoacademy.net , paul@fratila.ro si numarul de telefon ...'
e = re.findall('@([\w]+\.[\w]{2,})', c)  # cauta toate caracterele dupa @ pana la spatiu, fara acesta

for i in e:
    print('http://www.' + i)


# extrage numere rationale dintr-un fisier .txt
fis = open('text1.txt')

rez_list = []

for line in fis:
    line = line.rstrip()
    extrage = re.findall('^X-DSPAM-Confidence: ([0-9]+\.{1}[0-9]*)', line)
    # punctul are sens de virgula aici (toate cifrele inclusiv dupa virgula)
    if extrage:
        numar = float(extrage[0])
        rez_list.append(numar)

print(rez_list)
print('Maxim:', max(rez_list))
print(len(rez_list))


# extrage numere rationale cu escape character
k = 'Avem de incasat $25.0, $3.258 de la clienti'
l = re.findall('\$[0-9]+\.{1}[0-9]*', k)  # \$ - caracterul $ nu semnificatia acestuia din REGEX
print(l)


# verifica nr tel
def verifica_nr_tel():
    nr = input(' Introduceti nr de tel - trebuie sa cuprinda 10 cifre si sa inceapa cu 07: ')
    # import re
    if re.search('^07[0-9]{8}$', nr):
        print('Numar corect')
    elif not nr.isdigit():
        print('Trebuie sa contina doar cifre')
    elif len(nr) != 10:
        print(f'Trebuie sa aiba 10. Numarul tau are {len(nr)}')
    elif not nr.startswith('07'):
        print('Tre sa inceapa cu 07. Numarul tau incepe cu {0}'.format(nr[0:2]))

verifica_nr_tel()


# Extrage pana la primul caracter ":". Daca scoatem "?" - pana la ultimul
x = 'From: Using the : character'
print(re.findall('^F.+?:', x))


# Extragere numere dintr-un text / suma lor
y = open('regex.txt')
suma = 0
big_list = []

for line in y:
    line = line.rstrip()
    z = re.findall('[0-9]+', line)
    if z:
        big_list += z
        for i in z:
            suma += int(i)

print(suma)
print(big_list)


# Split - regex
y = "cand ti-e sete bei bere cand ti-e foame mananci mere daca nu ai poti manca pere sa traiesti mai vere \
hai, la treaba"
l = re.split('[bmpv]ere', y)
print(l)


# re.sub
x = re.sub('[a-z]ere', '?', y)
print(x)


# cautare dupa codul caracterelor
sir1 = "Chineză: 我喜歡編程"
abc = re.findall("{0}|{1}".format(str(chr(31243)), str(chr(25105))), sir1)
print(abc)


# putem capta rezultatul unor comenzi de sistem
stdout = os.popen('ping -n 1 8.8.8.8')
print(type(stdout))
print(stdout,"\n\n")
# Citim output-ul
result = stdout.read()
# Afisam output-ul
print(result)

# Cautam cu ajutorul modulului re in rezultat "Metoda 1"
cauta = re.search("(\d{1,3}%\sloss)", result)
if cauta:
    print(cauta.group(0))

# Cautam cu ajutorul modulului re in rezultat "Metoda 2"
cauta = re.search("Lost\s=\s(\d+)", result)
if cauta:
    print(cauta.group(0))

# Cautam cu ajutorul modulului re in rezultat "Metoda 3"
cauta=re.search("Lost = (\d+)",result)
if cauta:
    print(cauta.group(0))


# punctul si pipe ( | )
la = """ala ana ama 
asa ada 
ela ema 
eba ena eva"""
print(re.search('a.a', la))  # prima aparitie
print(re.findall('a.a', la))  # toate aparitiile a orice caracter a
print(re.findall('e.a',la))  # toate aparitiile e orice caracter e
print(re.findall('e.a|a.a',la))  # toate aparitiile a orice caracter a si e orice caracter e
print(re.findall('e.a | a.a',la))  # atentie, spatiul e tratat ca atare
print(re.search('e.a|a.a',la))  # acelasi lucru, fara spatii, alt rezultat


# Metacaracterele ^, $
print(re.search('^a.a', la))  # care incepe cu
print(re.search('e.a$', la))  # care se termina cu
lb = 'test regex'
print(re.search('\Atest regex\Z', lb))  # care contine exact textul
print(re.findall('e[blmnvx]a',la))  # cuvinte de 3 litere, incep cu e, se termina cu a, au o consoana (b,l,m,n,v,x)
print(re.findall('e[^aeiou]a',la))   # cuvinte de 3 litere, incep cu e, se termina cu a plus orice car diferit de vocala


# re.compile(patern, flag) flag poate fi re.IGNORECASE, re.MULTILINE, re.DOTALL
def validare(email):
    # compilare expresie regex intr-un obiect regex
    regex_object = re.compile(r'^\S+@\S+\.[a-z]{2,4}$', re.IGNORECASE)

    result = regex_object.search(email)

    if result:
        print("Email ok")
    else:
        print("Email incorect")

e1 = 'aNa@a.ro'
e2 = 'ana@a.r'
e3 = 'ana.ana@info.info'
e4 = 'ana@info.Infor'

validare(e1)