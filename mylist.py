class MyRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.a = -1
        return self

    def __next__(self):
        self.a += 1
        if self.a == self.stop:
            raise StopIteration

        return self.a


class List:
    class _Node:
        __slots__ = ('value', 'next')

        def __init__(self, value, next_=None):
            self.next = next_
            self.value = value

    class _NodeIterator:

        def __init__(self, first):
            self._next_node = first

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next
            return value

    def __init__(self, iterable=None):
        self._head = None
        self._tail = None
        self._length = 0
        if iterable is not None:
            self.extend(iterable)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if index < 0:
            index += len(self)

        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next
        return node.value

    def __iter__(self):
        return List._NodeIterator(self._head)

    def append(self, value):
        node = List._Node(value)
        if len(self) == 0:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._length += 1

    def extend(self, iterable):
        for value in iterable:
            self.append(value)
