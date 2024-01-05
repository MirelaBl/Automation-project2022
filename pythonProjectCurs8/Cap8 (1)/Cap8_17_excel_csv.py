"""
817 Module
Modulul excel + csv - exemple
PF - 29.06.2021 v6
"""  #

# instalare modul:      pip3 install openpyxl
#                       pip3 install xlwt - pentru fisiere .xls - exemplele sunt pt .xlsx
# instalare modul imagini:      pip3 install pillow
# documentatie : https://openpyxl.readthedocs.io/en/default/     next urmatoarele pagini

from openpyxl import Workbook
import csv
import datetime

wb = Workbook()  # Creeaza obiectul care sustine fisierul excel
ws = wb.active  # Lucreaza in worksheet-ul curent (ws) - il creeaza daca nu exista

# un rand din csv populeaza un rand din excel (primele coloane, corespunzator numarului de campuri din csv)
with open('c:/_wt/medici.csv', newline='', encoding='utf8') as csvfile:
    medici_reader = csv.reader(csvfile, delimiter=',', quotechar=None)
    for rand in medici_reader:
        ws.append(rand)
wb.save("sample1.xlsx")

# un rand din csv populeaza un rand din excel (plus inxed prima coloana, plus fullname, plus data
with open('c:/_wt/medici.csv', newline='', encoding='utf8') as csvfile:
    medici_reader = csv.reader(csvfile, delimiter=',', quotechar=None)
    indx = 0
    for rand in medici_reader:
        ws.append([indx] + rand + [rand[1]+ ' ' + rand[0]] + [datetime.datetime.now()])
        indx += 1
wb.save("sample1.xlsx")

# idem doar pentru chirurgie
with open('c:/_wt/medici.csv', newline='', encoding='utf8') as csvfile:
    medici_reader = csv.reader(csvfile, delimiter=',', quotechar=None)
    indx = 0
    for rand in medici_reader:
        if rand[3] == 'chirurgie':
            ws.append([indx] + rand)
        indx += 1
wb.save("sample1.xlsx")

wb.close()
