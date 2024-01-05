l = list()

M = set()

M.add(5)

M.add(7)

l.append(6)

l.append(8)
print(l)
print(M)
for x in M:
    l.append(x)

print(l)
print(M)

l.append(7)
M.add(7)
print(l)
print(M)