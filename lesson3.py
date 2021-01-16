from lesson2 import A

class F:
    def __init__(self):
        super().__init__()

class B:
    def __init__(self, a: A):
        self.a = a

b = B(A())
print(b.a)
