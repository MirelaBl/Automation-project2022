"""
312 Tuplu
tuplu
PF - 18.07.2020 v4
"""  #

# pylint: disable=invalid-name

tu = (2, 3, 6, 7, 8, 9, 0, 1, 4, 5,)

print(all(tu) < 5)  # implementare eronata
print(any(tu) > 5)  # implementare deficitara

for i, j in enumerate(tu):
    print(i, j)

print(max(tu))

print(min(tu))

print(sorted(tu))
