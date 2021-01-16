class Person(object):
    """
    некий класс
    """
    
    #свойства класса
    class_name: str = "class"
    class_age: int = 99

    def __init__(self, name=None, age=None):
        """
        инициализация объекта, конструктор
        """      
        self.name = name
        self.age = age
        #скрытое свойство
        self.__weight: float
        """отличие скрытого свойства с _ от __ в том
        что для __ включается переименование свойства
        оно становится извне видно как _Person__weight
        необъходимо для классов наследников, чтоб не переопределяли это свойство"""

    def __repr__(self):
        """
        представление, для вывода объекта в виде исполняемого кода
        """
        return f"Person({self.name},{self.age})"

    @property
    def weight(self):
        """
        геттер скрытого поля
        """
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        """
        сеттер скрытого поля
        """
        self.__weight = float(value)

    def print_info(self):
        """
        метод объекта
        """
        print(f"{self.name} is {self.age}")

    @classmethod
    def print_class(cls):
        """
        метод класса, можно обращаться к полям класса
        создавать объекты текущего класса
        """
        print(f"{cls.class_name} is {cls.class_age}")

    @staticmethod
    def print_some_info():
        """
        статический метод класса, просто выполняет некий код
        """
        print("Вывод статического метода")

if __name__ == "__main__":
    john = Person()
    john.name = "John"
    john.age = 21

    lucy = Person("Lucy", 19)

    john.print_info()
    john.print_class()
    lucy.print_info()
    print(lucy)
    Person.print_some_info()
    lucy.weight = 50.8
    print(lucy.weight)
