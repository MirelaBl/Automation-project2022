"""
812 Module
Modulul pygal_maps_world - exemple
PF - 29.06.2021 v6
"""  #


import os
from pygal_maps_world import maps

# http://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html

# tari
worldmap_chart = maps.World()
worldmap_chart.title = 'Tari alese'
worldmap_chart.add('Romania', ['ro'])
worldmap_chart.add('Moldova', ['md'])
worldmap_chart.add('Franta', ['fr'])
worldmap_chart.add('UK', ['gb'])
worldmap_chart.add('USA', ['us'])
worldmap_chart.render_to_file('tari.svg')

os.system('tari.svg')  # deschide fisierul


# continente
supra = maps.SupranationalWorld()
supra.add('Sediul central', [('europe', 1)])
supra.add('Sediul financiar', [('north_america', 2)])
supra.add('Sediu recuperare', [('oceania', 3)])
supra.render_to_file('continente.svg')

os.system('continente.svg')  # deschide fisierul
