"""
456
Accesarea fiserelor, citirea si scrierea
PF 22.09.2020 v4
"""  #

# pylint: disable=invalid-name

enunt = """1. Creati un program care sa citeasca toate liniile unui text (guta.txt)
sub forma unei liste si afisati lista. 
2. Scrieti o linie intr-un fisier, cu un text la alegere
3. Cititi primul fisier intr-un singur sir de caractere apoi afisati-l.                              #
"""  #

input('Apasa <enter> pentru a iesi.')

print("Citeste liniile unui text si le adauga intr-o lista.\n")
text = open('c:/_wt/guta.txt', "r")
linii = text.readlines()
print(linii)

print("\nVom scrie o linie la sfarsitul textului\n")
text = open('c:/_wt/guta.txt', "w+")
text.write("\nAstazi am testat scrierea in fisier\n")  		# scrie o linie in fisier
text.close()

text = open("c:/_wt/guta.txt", "r")
print(text.read()) # citeste toate liniile intr-un sir de caracter
text.close()
