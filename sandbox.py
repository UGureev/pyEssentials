import timeit
from myhashmap import HashMap

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (self.x == other.x) and (self.y == other.y)
        else:
            raise TypeError

    def __hash__(self):
        return hash(f'x{self.x}y{self.y}')


l = [Vector(i, j) for i in range(100) for j in range(100)]
s = {Vector(i, j) for i in range(100) for j in range(100)}
h = HashMap(((Vector(i, j), j) for i in range(100) for j in range(100)))


def func1():
    if Vector(56,76) in l:
        a = 1


def func2():
    if Vector(56,76) in s:
        a = 1


def func3():
    if Vector(56,76) in h:
        a = 1
    #a = h.get(Vector(56,76))


print(timeit.timeit(func1, number=1000))
print(timeit.timeit(func2, number=1000))
print(timeit.timeit(func3, number=1000))


