"""
702 Module
Modulul platform
PF - 15.06.2021 v6
"""  #


import platform


def modaccess(nume_modul: str, fisier_metode: dict):
    for i in fisier_metode:
        metoda = nume_modul + '.' + i
        print(metoda.ljust(40), "->", fisier_metode[i].ljust(40), "->", eval(metoda))


metode = {"machine()": "info arhitectura hardware a computerului",
          "system()": "tipul sistemului de operare",
          "win32_ver()": "versiunea de windows si alte informatii",
          "processor()": "tipul procesorului",
          "node()": "numele dispozitivului in retea",
          "platform()": "info sistem de operare",
          "architecture()": "info arhitectura si sistem operare",
          "version()": "versiunea sistemului de operare",
          "python_version_tuple()": "un tuplu cu info vers python",
          "python_version()": "un string cu versiunea python",
          "python_implementation()": "implementarea python curenta",
          }

modaccess('platform', metode)

for i in dir(platform):
    print(i)

#help(platform)
