import math


class MyRange:

    def __init__(self, start, end=None, step=1):
        if end is None:
            self.end = start
            self.start = 0
        elif step < 0:
            self.start = end
            self.end = start
        else:
            self.end = end
            self.start = start
        if step != 0:
            self.step = step
        else:
            raise ValueError("Step cannot be zero.")
        self.length = math.ceil(abs((self.end - self.start) / self.step))

    def __len__(self):
        return self.length

    def __repr__(self):
        return f'MyRange({self.start},{self.end},{self.step})'

    def __iter__(self):
        result = self.start
        for _ in range(len(self)):
            yield result
            result += self.step
