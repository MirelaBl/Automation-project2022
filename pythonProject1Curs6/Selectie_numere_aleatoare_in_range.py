from random import randint

l = []
for i in range (1, 9):
    while True:
        x = randint(1, 8)
        if len(l) == 8:
            break
        elif x in l:
            continue
        else:
            print(x)
            l.append(x)       

