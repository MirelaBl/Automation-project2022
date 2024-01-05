"""
701 Module
Crearea modulelor in Python (modululmeu)
PF - 15.06.2021 v6
"""  #


#
# pip show <<package_name>>
# pip uninstall <<package_name>>

TEMP_MEDIE = 12


def patrat(nr=1):
    """ Ridicarea la patrat"""
    try:
        rezult = nr * nr
    except TypeError:
        rezult = "Introduceti un numar"
    return rezult


def cub(nr=1):
    """ Ridicarea la cub"""
    try:
        rezult = nr * nr * nr
    except TypeError:
        rezult = "Trebuie sa introduci un numar"
    return rezult


def factorial(n=5):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print("E un modul. Importa acest modul pentru a putea utiliza functiile din el.")

# pynetcdf (0.7)                         - Standalone Scientific.IO.NetCDF (2.4.11) built for NumPy
