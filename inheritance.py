class MyMRO(type):  # наследование type = это метакласс
    """задаем свой mro"""
    def mro(cls):
        return (cls, Animal, object)  # явно задаем порядок!


class Animal:

    def __init__(self):
        self.weight = 100


class Horse(Animal):

    def __init__(self):
        super().__init__()

    def run(self):
        print("i'm running!")


class Eagle(Animal):

    def __init__(self):
        super().__init__()

    def fly(self):
        print("i'm flying!")


class Pegasus(Horse, Eagle):

    def __init__(self):
        # В родительских классах тоже используется super(),
        # поэтому все инициализаторы сработают в порядке MRO
        super().__init__()


class Rabbit(Horse, Eagle, metaclass=MyMRO):

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    pegasus = Pegasus()
    pegasus.run()
    pegasus.fly()
    print(pegasus.weight)

    # [<class '__main__.Pegasus'>, <class '__main__.Horse'>,
    # <class '__main__.Eagle'>, <class '__main__.Animal'>, <class 'object'>]
    print(Pegasus.mro())

    rabbit = Rabbit()
    # (<class '__main__.Rabbit'>, <class '__main__.Animal'>, <class 'object'>)
    print(Rabbit.mro())
    try:
        rabbit.run()
    except AttributeError as e:
        print(e)

"""
Когда нельзя линеаризировать
неразрешимые примеры:
    class X: ...
    class Y: ...
    class A(X, Y): ...
    class B(Y, X): ...
    class G(A, B): ...
Для A порядок X -> Y, а для B – обратный Y -> X

class X: ...
class Y(X): ...
class A(X, Y): ...
Здесь класс X наследуется дважды
нарушает либо порядок старшинства либо порядка

"""