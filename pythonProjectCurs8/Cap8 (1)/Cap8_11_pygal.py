"""
811 Module
Modulul pygal - exemple
PF - 29.06.2021 v6
"""  #

# http://www.pygal.org/en/stable/documentation/output.html#png

import pygal
import os

# exemplu  pygal.Bar
ob_chart = pygal.Bar()  # creare obiect - grafic cu bare verticale alaturate
ob_chart.add('Grafic', (1, 33, 17, 15, 31, 86))  # adaugare date
ob_chart.render_to_file('grafic.svg')  # salvare fisier grafic

ob_chart.add('Grafic_1', [10, 20, 18, 29, 14, 23, 39]).render_to_file('grafic.svg')  # se pot adauga in continuare

os.system('grafic.svg')  # deschide fisierul


# exemplu  pygal.Line
ob_c1 = pygal.Line(title='Note Python',
                   x_title='Capitol',
                   y_title='Nota',
                   title_font_size=55,)
ob_c1.add('Catalog', [91, 95, 87, 99, 100, 79, 100, 98])
ob_c1.add('Catalog1', [81, 75, 97, 100, 89, 77, 100, 98])
ob_c1.x_labels = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CA']
ob_c1.render_to_file('catalog.svg')

os.system('catalog.svg')


# exemplu  pygal.StackedBar
lista_v = [1, 3, 2, 4, 3, 5, 15]
lista_i = (10, 2, 3, 4, 5, 6, 7)
ob_c2 = pygal.StackedBar()  # bare verticale una peste alta
ob_c2.add('Vanzari', lista_v)
ob_c2.add('Incasari', lista_i)
# punem etichete valorilor pe axa x
ob_c2.x_labels = ['Lu', 'Ma', 'Mi', 'Jo', 'Vi', 'Sa', 'Du']

ob_c2.render_to_file('vanzari.svg')

os.system('vanzari.svg')
