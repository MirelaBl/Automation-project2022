"""
807 Module
Modulul requests - exemple
PF - 29.06.2021 v6
"""  #


import requests

# extragem continut pagina
conect = requests.get('https://www.infoacademy.net/cursuri')
type(conect)
# vizualizam continutul html
print(conect.text)


# pagina speciala pentru teste
r = requests.get('http://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
print(r.status_code)
print(r.text)

# metoda POST
payload = dict(key1='value1', key2='value2')
r = requests.post('http://httpbin.org/post', data = payload)
print(r.text)
r.headers.values ()

# metoda GET
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
r.json()
print(r.text)


mesaje = """ cateva mesaje posibile:
	200 – Pagina a fost incarcata cu success.
	301 – MOVED_PERMANENTLY
	307 – Pagina a fost temporar redirectata (temporary_redirect)
	403 – Accesul este interzis (FORBIDDEN)
	404 – Fisierul nu a fost gasit
	408 – Cererea a expirat (request timeout)
	500 – INTERNAL_SERVER_ERROR
"""