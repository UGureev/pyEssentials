class A():
    def f(self):
        print("A")

class B():
    
    def f(self):
        print("B")

class C():
    pass

class D(A):
    pass

class E(A):
    pass

class F(D, C, E):
    pass

print(F.mro())

f = F()
f.f()