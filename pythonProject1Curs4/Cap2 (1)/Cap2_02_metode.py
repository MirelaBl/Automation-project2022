""" 202 Manipularea sirurilor de caractere
 Metode de manipulare
 PF - 20.07.2021 v5
"""  #

# pylint: disable=invalid-name

var1 = "Astazi e ziua ta"

print(var1.upper())  # doar litere mari
print(var1.lower())  # doar litere mici
print(var1.title())  # prima litera a fiecarui cuvant litera mare

varx = var1.upper()
print(varx.isupper())  # testeaza daca contine doar litere mari

low = var1.lower()
print(low.islower())  # testeaza contine doar litere mici

print(var1.isalpha())  # contine si spatii
r = var1.replace(" ", "")
print(r.isalpha())  # testeaza contine doar car alpha

print(var1.split())  # returneaza o lista cu elementele separate de
# subsirul ales(spatiu aici)

print(var1.find("ta"))  # Arata pozitia primei aparitii a subsirului
print(var1.find("ta", 4))  # Arata pozitia primei aparitii a
# subsirului dupa caracterul cu indexul 7

print(var1.find("e"))

print(var1)  # sirul initial ramane NEMODIFICAT

var2 = "ana are mere"

print(var2.capitalize())

var2.capitalize().replace("mere", "pere")

# variabila temporara '_'. ATENTIE, functioneaza doar in consola, nu in aplicatii

print(
    var1.center(40, '*'), "!"
)  # centreaza sirul completand cu spatii pana la 25 de caractere
print(var1.rjust(40, "/"), "!")
print(var1.ljust(40), "!")

# ljust si rjust aliniaza la stanga si dreapta

print(var1.count("ta"))  # numara de cate ori apare subsirul 'ta'

print((var1.join("-*&")))  # scrie sirul intre caracterele date

print(
    " ".join(["Astazi", "va", "fi", "soare"])
)  # scrie elementele listei despartite de sirul dat, fara capete

print(var2)

var3 = "1234560"
var4 = "A501"
print(var3.isdigit())  # testeaza contine doar car numerice
# sau
print(var3.isnumeric())
print(var4.isdigit())
print(var4.isalnum())  # testeaza contine car alphanumerice

chr(38646)
chr(22235)  # 4

"零".isdigit()
"零".isnumeric()

input("Apasa <enter> pt a iesi.")
