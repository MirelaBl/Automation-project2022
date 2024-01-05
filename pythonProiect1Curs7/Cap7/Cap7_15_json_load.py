"""
715 Json - serializare
PF 31/01/21 v4
"""  #

import json

# creare obiect fisier
cities = 'cities.json'
countries = 'countries.json'
regions = 'regions.json'

# accesarea datelor - alt exemplu
o = open(cities)
t = open(countries)
r = open(regions)

orase = json.load(o)
tari = json.load(t)
regiuni = json.load(r)

print(orase)
print(regiuni)
print(tari)

for i in orase:
    if i['CountryID'] == 202:
        print(i['City'])

regiune_dorita = 'Victoria'

for j in regiuni:
    regiuni_alese = []
    if j['Region'] == regiune_dorita:
        regiuni_alese.append(j["_id"])
    for i in orase:
        if i["RegionID"] in regiuni_alese:
            print(i["City"], i["RegionID"], regiune_dorita, i["CountryID"])
