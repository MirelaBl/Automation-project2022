print("---------Calculator Deficit Caloric-------------")
print("................................................")
varsta = int(input("Introdu vârsta: "))
greutate = int(input("Introdu greutatea în kg: "))
inaltime = int(input("Introdu înălțimea în cm: "))
sex = int(input("Sexul: 1.Masculin 2. Feminin "))
listaactivitati = ['1. Muncă sedentară și puține alte activități',
                   '2. Muncă în picioare sau exerciții ușoare 1-3 zile pe săptămână',
                   '3. Activități zilnice moderate sau exerciții 5-6 zile pe săptămână',
                   '4. Exerciții intense zi de zi sau muncă fizică intensă plus exerciții 1-3 zile pe săptămână',
                   '5. Sportiv de performanță sau muncă fizică intensă plus exerciții de peste 3 ori pe săptămână']
listarezultate = ['Rata metabolică bazală este: ',
                  '-> Slăbire ușoară 0.25 kg/săpt =',
                  '-> Slăbire medie 0.50 kg/săpt =',
                  '-> Slăbire extremă 1.00 kg/săpt =',
                  '!! Consultă medicul dacă vrei să slăbești 0.5 kg/săpt sau mai mult !!']
print("Nivelul de activitate fizică:")
for activitatea in listaactivitati:
    print(activitatea)
activitate = int(input("Introdu valoarea: " ))
rmbb = int(10*greutate+6.25*inaltime-5*varsta+5)
rmbf = int(10*greutate+6.25*inaltime-5*varsta-161)
#Bărbat
print("--------------------------------------------------------")
if sex == 1 and activitate==1:
    print(listarezultate[0],int(rmbb*1.2),"Kcal/zi")
    print(listarezultate[1],int(rmbb*1.2-250),"Kcal/zi")
    print(listarezultate[2],int(rmbb*1.2-500),"Kcal/zi")
    print(listarezultate[3],int(rmbb*1.2-1000),"Kcal/zi \n",listarezultate[4])
elif activitate==2:
    print(listarezultate[0],int(rmbb*1.375),"Kcal/zi")
    print(listarezultate[1],int(rmbb*1.375-250),"Kcal/zi")
    print(listarezultate[2],int(rmbb*1.375-500),"Kcal/zi")
    print(listarezultate[3],int(rmbb*1.375-1000),"Kcal/zi \n",listarezultate[4])
elif activitate==3:
    print(listarezultate[0],int(rmbb*1.55),"Kcal/zi")
    print(listarezultate[1],int(rmbb*1.55-250),"Kcal/zi")
    print(listarezultate[2],int(rmbb*1.55-500),"Kcal/zi")
    print(listarezultate[3],int(rmbb*1.55-1000),"Kcal/zi \n",listarezultate[4])
elif activitate==4:
    print(listarezultate[0],int(rmbb*1.725),"Kcal/zi")
    print(listarezultate[1],int(rmbb*1.725-250),"Kcal/zi")
    print(listarezultate[2],int(rmbb*1.725-500),"Kcal/zi")
    print(listarezultate[3],int(rmbb*1.725-1000),"Kcal/zi \n !!",listarezultate[4])
elif activitate==5:
    print(listarezultate[0],int(rmbb*1.9),"Kcal/zi")
    print(listarezultate[1],int(rmbb*1.9-250),"Kcal/zi")
    print(listarezultate[2],int(rmbb*1.9-500),"Kcal/zi")
    print(listarezultate[3],int(rmbb*1.9-1000),"Kcal/zi \n !!",listarezultate[4])
#Femeie
if sex == 2 and activitate == 1:
    print(listarezultate[0],int(rmbf*1.2),"Kcal/zi")
    print(listarezultate[1],int(rmbf*1.2-250),"Kcal/zi")
    print(listarezultate[2],int(rmbf*1.2-500),"Kcal/zi")
    print(listarezultate[3],int(rmbf*1.2-1000),"Kcal/zi \n !!",listarezultate[4])
elif activitate==2:
    print(listarezultate[0],int(rmbf*1.375),"Kcal/zi")
    print(listarezultate[1],int(rmbf*1.375-250),"Kcal/zi")
    print(listarezultate[2],int(rmbf*1.375-500),"Kcal/zi")
    print(listarezultate[3],int(rmbf*1.375-1000),"Kcal/zi \n !! ",listarezultate[4])
elif activitate==3:
    print(listarezultate[0],int(rmbf*1.55),"Kcal/zi")
    print(listarezultate[1],int(rmbf*1.55-250),"Kcal/zi")
    print(listarezultate[2],int(rmbf*1.55-500),"Kcal/zi")
    print(listarezultate[3],int(rmbf*1.55-1000),"Kcal/zi \n !!",listarezultate[4])
elif activitate==4:
    print(listarezultate[0],int(rmbf*1.725),"Kcal/zi")
    print(listarezultate[1],int(rmbf*1.725-250),"Kcal/zi")
    print(listarezultate[2],int(rmbf*1.725-500),"Kcal/zi")
    print(listarezultate[3],int(rmbf*1.725-1000),"Kcal/zi \n !!",listarezultate[4])
elif activitate==5:
    print(listarezultate[0],int(rmbf*1.9),"Kcal/zi")
    print(listarezultate[1],int(rmbf*1.9-250),"Kcal/zi")
    print(listarezultate[2],int(rmbf*1.9-500),"Kcal/zi")
    print(listarezultate[3] ,int(rmbf*1.9-1000),"Kcal/zi \n !! ",listarezultate[4])

print("--------------------------------------------------------")