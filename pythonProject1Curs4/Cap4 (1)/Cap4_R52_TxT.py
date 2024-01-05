"""
452
Exercitii - Acronime / Criptare
PF 18.09.2020 v4
"""  #

# pylint: disable=invalid-name

enunt = """
1. Creati un program care sa faca acronime cu prima litera a cuvintelor componente (litere mari)
2. Creati un program care sa returneze echivalentul numeric al textului, utilizand ordinea literelor
fara diacritice in alfabet: a=1, b=2, ..., z=26 (criptare);
Faceti decriptarea
alpha = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','x','y','w','z'] - o lista in care indexul literei este numarul asociat
"""
text = input('Introduceti textul :')
acronim = ''
for cuv in text.split(' '):
    acronim += (cuv[0]).upper()
print(acronim)

# Creati un program care sa returneze echivalentul numeric al textului a=1, b=2, ..., z=26 (lista)
# Faceti decriptarea

# Criptare
text = (input('Introduceti textul :')).lower()
lista = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'x', 'y', 'w', 'z']
ln = []

for lit in text:
    numar = lista.index(lit)
    ln.append(numar)
print(ln)

# Decriptare
text_decriptat = ''
for nr in ln:
    lit = lista[nr]
    text_decriptat += lit
print(text_decriptat)

input('Apasa <enter> pentru a iesi.')

text = 'gjdsdfasj sadfjhfasjkf'

textc = ''
for lit in text:
    n = lista.index(lit)
    textc += str(n)+' '
print(textc)

textd = ''
for i in textc.split():
    l = lista[int(i)]
    textd += str(l)
print(textd)
