
from random import randint
print('introdu un numar')
def game():
    """
    ghiceste  numarul
    """
    global numar
    numar= randint(1,100)
    global nrincercari
    nrincercari = 0
    while True:
        numarintr = int(input())
        nrincercari +=1
        if numar == numarintr:
            print('felicitari Nr corect din '+str(nrincercari)+' incercari')
            break
        elif numarintr > numar:
            print('nr prea mare')
            continue
        else:
            print('nr prea mic')
        continue

game()
