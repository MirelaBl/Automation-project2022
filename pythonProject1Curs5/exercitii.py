class Dict1:


    def __init__(self):
        self.dc = {}

    def adauga(self):
        while True:
            count = 0
            print('introduce un cuv')
            cuvant= input().lower()

            if cuvant == '':
                print('nu ai adaugat nimic')
                break
            elif cuvant in self.dc.keys():
                print('adaugat deja')
                break
            else:
                print('introdu descriere')
                descr = input().lower()
                self.dc[cuvant]= descr

dex = Dict1()

dex.adauga()

for v in Dict1.values():
    print(v)

print(dex)