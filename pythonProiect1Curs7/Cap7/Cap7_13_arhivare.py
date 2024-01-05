"""
713 Module
Modulul zipfile
PF - 15.06.2021 v6
"""  #


from datetime import datetime
import zipfile  # similar pentru rar modulul rarfile

# deschide arhiva existenta
fisier_zip = zipfile.ZipFile("C:\Users\Mirela\exempluArhiva\Cap7.zip","r")

# listeaza numele fisierelor din arhiva
count = 1
for nume in fisier_zip.namelist():
	print("Fisier {0}:".format(count), nume)
	count += 1

# lista cu informatii despre fisiere
for info in fisier_zip.infolist():
	print(type(info))
	print('\n', info.filename)
	print('\tComment:\t', info.comment)
	print('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
	print('\tZIP version:\t', info.create_version)
	print('\tCompressed:\t', info.compress_size, 'bytes')
	print('\tUncompressed:\t', info.file_size, 'bytes')
	if info.file_size - info.compress_size > 0:
		print('Comprimat')
	else:
		print('Necomprimat')

# extrage un singur fisier (fisier extras, calea)
fisier_zip.extract('countries.json', 'c:/_wt/test/abcd/')

# extrage toate fisierele
fisier_zip.extractall('c:/_wt/test/test')

# info despre un fisier din arhiva
fisier_zip.getinfo("cities.json")

# fisierele in arhiva
fisier_zip.printdir()

fisier_zip.close()


# creaza o arhiva noua si adauga fisiere in aceasta
ob_scrie = zipfile.ZipFile("c:/_wt/exemplu2.zip", "w+")  # cream obiectul
ob_scrie.write('c:/_wt/medici.txt', 'm7.txt')
ob_scrie.write('c:/aaa/CSSNotesForProfessionals.pdf', 'css2.pdf')
ob_scrie.read('m7.txt')  # citim fisierul

ob_scrie.close()

# scriem intr-un fisier din arhiva
ob_scrie = zipfile.ZipFile("c:/_wt/exemplu2.zip", "a")
ob_scrie.writestr('c5.txt', "\nAm reusit sa scriu astazi {0}".format(datetime.today()))
ob_scrie.read('c5.txt')
ob_scrie.close()


# Cream arhiva comprimata 1
arh_comp = zipfile.ZipFile('c:/_wt/exemplu3.zip', 'w', compression=zipfile.ZIP_DEFLATED)
arh_comp.write('c:/_wt/People_small.txt', 'ps.txt')

# verificam daca e comprimata
for info in arh_comp.infolist():
	print('\n', info.filename)
	print('\tCompressed:\t', round(info.compress_size / 1024 ** 2, 1), 'Mb')
	print('\tUncompressed:\t', round(info.file_size / 1024 ** 2, 1), 'Mb')

arh_comp.close()

# Cream arhiva comprimata 2
arh_comp = zipfile.ZipFile('c:/_wt/exemplu4.zip', 'w', compression=zipfile.ZIP_BZIP2)
arh_comp.write('c:/_wt/People_small.txt', 'ps.txt')

for info in arh_comp.infolist():
	print('\n', info.filename)
	print('\tCompressed:\t', info.compress_size, 'bytes')
	print('\tUncompressed:\t', info.file_size, 'bytes')
