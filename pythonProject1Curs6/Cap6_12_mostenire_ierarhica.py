"""
612 OOP  
Mostenire ierarhica - multipla
PF - 08.06.2021 v5
"""  #

class A:
    x = 10
    y = "a"

class B(A):
    x = 20
    z = [1,2,3]

class C(B):
    x = 30
    w = {1: 'cirese'}

class M(A):
    x = 100

class N(M):  # mostenire ierarhica
    x = 1000

class X(N):  # clasa X mosteneste clasa N, care mosteneste M, care mosteneste A
    pass

obj1 = X()

print(obj1.x)  # instanta va prelua atributul x de la cea mai apropiata, N in acest caz
print(obj1.y)

dir(X)

print('A.x', A.x, '\nB.x', B.x, '\nB.z', B.z, '\nC.y', C.y, '\nC.w', C.w, '\nN.x', N.x)

class Y(N, B, A):  # Mostenire multipla
    pass

obj2 = Y()
Y.__mro__
print(obj2.y)
print(obj2.x)
print(obj2.z)
