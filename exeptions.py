try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
except (ValueError, IndexError):
    print("Можно сразу много в одном блоке, но так лучше не делать")
    raise  # передать то же исключение дальше
else:
    # этот блок нужен чтобы выполнить дополнительный код после удачной попытки
    # т.к. в попытке должно быть минимум кода
    print("Выполняется, если try закончился успешно")
finally:
    print("Выполняется абсолютно в любом случае, даже если был return")

##########

try:
    a = int(input())
finally:
    print("Это минимальный блок try")

##########


class ObjectWithDestructor:
    def __del__(self):
        raise ValueError("Исключение в деструкторе не приводит к завершению программы")


obj = ObjectWithDestructor()
del obj


# сцепление исключеней
try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError
except ValueError:
    raise IndexError from ValueError
    # raise IndexError from None  # заменяет исходное исключение
    # однако оно все равно сохраняется в __context__ для отладки

e = ZeroDivisionError()
e.__context__ = ValueError()  # исходное исключение
e.__suppress_context__ = True  # подавление исходного исключение
e.__cause__ = IndexError()  # генерируемое исключение
raise e


# предупреждения, выводят исключения но не прерывают программу
# наследники класса Exception -> Warning -> UserWarning
import warnings
warnings.warn(message="Warning!", category=DeprecationWarning, stacklevel=1)