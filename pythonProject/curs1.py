#masa produselor
masa_alune = 0.125
masa_biscuiti = 0.150
masa_cafea = 0.200

#cutii
pachete_per_cutie_alune = 1/48
pachete_per_cutie_biscuti= 1/36
pachete_per_cutie_cafea= 1/24

#volum
pachet_per_mc_alune= pachete_per_cutie_alune/32
pachet_per_mc_biscuiti = pachete_per_cutie_biscuti/32
pachet_per_mc_cafea = pachete_per_cutie_biscuti/40
#aprovizionare, cantitati aprovizionate

cantitate_aprov_alune= int ( input("cantitea alune:"))
cantitate_aprov_biscuiti= int ( input("cantitea biscuiti:"))
cantitate_aprov_cafea= int ( input("cantitea cafea:"))


#calculatii
cantitate_total = round(masa_alune * cantitate_aprov_alune + \
        masa_biscuiti *cantitate_aprov_biscuiti +  \
        masa_cafea * cantitate_aprov_cafea,2)

from math import ceil

cutii_total = ceil( cantitate_aprov_alune * pachete_per_cutie_alune) +\
    ceil(cantitate_aprov_biscuiti * pachete_per_cutie_biscuti) +\
    ceil(cantitate_aprov_cafea * pachete_per_cutie_cafea)

volum_total = ceil(cantitate_aprov_alune * pachet_per_mc_alune) +\
    ceil(cantitate_aprov_biscuiti * pachet_per_mc_biscuiti) +\
    ceil(cantitate_aprov_cafea * pachet_per_mc_cafea)
#afisare
print(f"Cantitate1: {cantitate_total} kg\nCutii:{cutii_total} buc\nVolum:{volum_total} mc")


#masa produselor
masa_alune = 0.112
masa_biscuiti = 0.150
masa_cafea = 0.190

#cutii
pachete_per_cutie_alune = 1/48
pachete_per_cutie_biscuti= 1/36
pachete_per_cutie_cafea= 1/24

#volum
pachet_per_mc_alune= pachete_per_cutie_alune/32
pachet_per_mc_biscuiti = pachete_per_cutie_biscuti/32
pachet_per_mc_cafea = pachete_per_cutie_biscuti/42
#aprovizionare, cantitati aprovizionate

cantitate_aprov_alune= int ( input("cantitea alune:"))
cantitate_aprov_biscuiti= int ( input("cantitea biscuiti:"))
cantitate_aprov_cafea= int ( input("cantitea cafea:"))


#calculatii
cantitate_total = round(masa_alune * cantitate_aprov_alune + \
        masa_biscuiti *cantitate_aprov_biscuiti +  \
        masa_cafea * cantitate_aprov_cafea,2)

from math import ceil

cutii_total = ceil( cantitate_aprov_alune * pachete_per_cutie_alune) +\
    ceil(cantitate_aprov_biscuiti * pachete_per_cutie_biscuti) +\
    ceil(cantitate_aprov_cafea * pachete_per_cutie_cafea)

volum_total = ceil(cantitate_aprov_alune * pachet_per_mc_alune) +\
    ceil(cantitate_aprov_biscuiti * pachet_per_mc_biscuiti) +\
    ceil(cantitate_aprov_cafea * pachet_per_mc_cafea)
#afisare
print(f"Cantitate2: {cantitate_total} kg\nCutii:{cutii_total} buc\nVolum:{volum_total} mc")

print('acum')
print( int ('100',16))
print(334%3)
print((7+3)(5**2))


print('aziiiiiiiiiiii')
a = '25'
if a.isdigit():
    print('numar')
elif a.isalpha():
    print( 'sdggd')


