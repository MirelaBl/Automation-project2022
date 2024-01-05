# Concatenare + indexare
sir = 'Tele' + 'cinemateca'
print(sir)
lit = sir[2+2]
if lit == sir[4]:
    print('ahahhh I know py')


if lit == sir[4:5]:
        print('I know py even better')

print(lit)
print(sir[-10:-9])
if lit == sir[-10:-9]:
    print('I know py even better!!!!!!!!!!!!!!')
x = 7
y = sir[x + 3]                          # index calculat cu o expresie
if y == sir[10]:
    print('I know py better better better')

"""# Bucla while intr-un sir - returneaza index - litera
index = 0                               # initializare variabila
while index < len(sir):
    litera = sir[index]                    # parsare
    print(index, '-', litera)
    index += 1                          # incrementare """
""" if ('t','e','l' == sir[:4]):
    print('ahaa')
ind = 0
while ind <len(sir):
    liter = sir[ind]
    ind += 1
    if ind == 4:
        break
    print(ind, '-', liter)"""


for i, j in enumerate(sir):
    print(i, j)


# Inversam ordinea literelor intr-un sir
sir = input('Introduceti un sir: ')

print('Sirul tau este', sir)
sir_invers = ''
for var in sir:
    sir_invers = var + sir_invers
    print(var)
print(sir_invers)

cuvant= input('Introduceti un cuvant: ')
print('cuvantul tau este', cuvant)
cuvant_invers = ''
for i in cuvant:
    cuvant_invers = i + cuvant_invers
    print(cuvant_invers)

week = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri']
print(week)
week.append('Sambata')
print(week)
week.extend(['Duminica', 'New_Day'])
print(week)
week.count('Luni')
print(week)
week.remove('New_Day')
print(week)

print('-----------------------')
week1 = list(week)
print(week1)
week1.sort()
print(week1)
week1.reverse()
print(week1)
print('-----------------------')

# schimbare chei/valori
pasari = {'privighetoare': 5, 'pitigoi': 3, 'pitulice': 7, 'cioara': 8}
dict_invers = {x: y for y, x in pasari.items()}
print(dict_invers)

# - # - #   SORTARE DICTIONAR
dictionar = {'Radu': 18, 'Corina': 12, 'Matei': 22, 'Elvira': 25, 'Bianca': 27}

# sortare key
lista = sorted(dictionar.keys())
print(lista)
