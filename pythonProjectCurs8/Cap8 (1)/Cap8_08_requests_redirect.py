"""
808 Module
Modulul requests, verifica redirectare cu succes - exemple
PF - 29.06.2021 v6
"""  #

import requests

url = "http://www.infoacademy.net/course.php?p=SQL&c=prezentare"
url_vechi = url

r = requests.get(url)
print(r.history)

print(r.status_code)  # 200 ok

print(r.url)  # NOUL url, daca a fost schimbat

if str(r.history[0])[-5:-2] == '301' and r.status_code == 200:
    print('URL vechi:', url_vechi)
    print('Status code acces pagina redirectata:', r.status_code)
    print('URL redirectat:', r.url)
    print('Status code redirectare:', str(r.history[0])[-5:-2])