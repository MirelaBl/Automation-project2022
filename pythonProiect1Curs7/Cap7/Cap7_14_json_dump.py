"""
714 Json - serializare
PF 31/01/21 v4
"""  #


import json

# creare fisier
filename = 'preferinte.json'

# informatii de serializat
preferinte_maria = ["maria", {"muzica": "folk", "sport": "ski", "culoare": "albastru"}]
preferinte_victor = ["victor", {"muzica": "rock", "sport": "box", "culoare": "verde"}]

# stocarea datelor in fisier
with open(filename, "w") as handle:         # handle = open(filename, "w")
    json.dump(preferinte_maria, handle)
with open(filename, "w") as handle:
    json.dump(preferinte_victor, handle)


# accesarea datelor
with open(filename) as handle:
    info_preferinte = json.load(handle)

print(info_preferinte)

# stocarea datelor - alt exemplu
with open(filename, "w") as handle:
    json.dump([preferinte_maria, preferinte_victor], handle)

# accesarea datelor - alt exemplu
with open(filename) as handle:
    info_preferinte = json.load(handle)

print(info_preferinte)

# doar ghilimelele sunt acceptate pentru stringuri

# corespondente tipuri de date
#   JSON            Python
#   object          dict
#   array           list
#   string          str
#   number(int)     int
#   number(real)    float
#   true            True
#   false           False
#   null            None
