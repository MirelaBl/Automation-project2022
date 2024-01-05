""" 205 Formatare
 f print
 PF - 20.07.2021 v5
"""  #

# pylint: disable=invalid-name


# f-string - o alta metoda de formatare (minim 3.7)
nume = "Mioara"
varsta = 25

print(f"{nume} are {varsta: .2f} de ani!")
print(f"""Numele: {nume.upper()} 
Varsta: {varsta * 2} ani""")


input("Apasa <enter> pt a iesi.")
