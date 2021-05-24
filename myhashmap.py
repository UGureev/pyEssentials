class LinearMap:
    """
    обычная Map, в составе список, в котором хранятся кортежи (key, value)
    """
    def __init__(self):
        self.items = []

    def add(self, k, v):
        """
        добавляет в список кортеж (key, value)
        """
        self.items.append((k, v))

    def get(self, k):
        """
        перебирает список в поисках нужного key
        """
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError


class BetterMap:
    """
    улучшенная Map
    хранит список обычных Map, обращается к ним, по вычисленному хэшу ключа
    """
    def __init__(self, n=100):
        """
        n - количество начальных слотов, которые заполняем пустыми Map'ами
        """
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        """
        определяем индекс слота, как остаток от деления хэша ключа на количество слотов
        это позволяет в будущем сразу выйти на слот в котором хранится нужное значение
        т.е. скорость поиска ключа прямо пропорциональна количеству слотов, но жрет память
        """
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        """
        находит нужную Map, и добавляет в нее кортеж (key, value)
        """
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)


class HashMap:
    """
    классическая HashMap
    отличие от BetterMap только в том, что слоты создаются динамически по мере наполнения
    так, чтобы в самом нижнем уровне LinearMap содержалось минимальное количество элементов
    """
    def __init__(self, iterable=None):
        """
        на старте создаем BetterMap в два слота
        и счетчик размера
        """
        self.maps = BetterMap(2)
        self.num = 0
        if iterable is not None:
            for k, v in iterable:
                self.add(k, v)

    def __contains__(self, item):
        try:
            a = self.get(item)
            return True
        except KeyError:
            return False

    def get(self, k):
        return self.maps.get(k)

    def add(self, k, v):
        # ресайз при количестве нижнегоуровневых Map равного количеству элементов
        if self.num == len(self.maps.maps):
            self._resize()

        self.maps.add(k, v)
        self.num += 1

    def _resize(self):
        new_maps = BetterMap(self.num * 2)
        for m in self.maps.maps:
            for k, v in m.items:
                new_maps.add(k, v)
        self.maps = new_maps


if __name__ == '__main__':
    lm = LinearMap()
    lm.add('3', 'Linear')
    print(lm.get('3'))
    map_ = BetterMap()
    map_.add('3', 'Better')
    print(map_.get('3'))
    hm = HashMap()
    hm.add('1', 'HashMap')
    print(hm.get('1'))
