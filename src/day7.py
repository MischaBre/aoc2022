class Item:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name}: {self.get_size()}'

    def __repr__(self):
        return self.__str__()

    def get_size(self):
        return self.size


class Folder(Item):
    def __init__(self, name: str):
        super().__init__(name, 0)
        self.content: list[Item] = list()

    def __str__(self):
        return 'd: ' + super().__str__()

    def __repr__(self):
        return self.__str__()

    def add_item(self, item: Item):
        self.content.append(item)

    def get_items(self):
        result = list()
        for c in self.content:
            if type(c) == Folder:
                result.append(Folder(c).get_items())
            else:
                result.append(c)
        return result

    def get_size(self):
        return sum([c.get_size() for c in self.content])

    def get_subfolders(self):
        return [c for c in self.content if type(c) == Folder]

    def get_subfolders_with_max_size(self, max_size: int):
        return [c for c in self.content if c.get_size() <= max_size and type(c) == Folder]


class File(Item):
    def __init__(self, name: str, size: int):
        super().__init__(name, size)

    def __str__(self):
        return 'f: ' + super().__str__()

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    hdd = Folder('hdd')
    hdd.add_item(File('a', 10))
    hdd.add_item(File('b',20))
    ca = Folder('c')
    ca.add_item(File('d', 30))
    ca.add_item(File('e', 60))
    x = Folder('x')
    y = Folder('y')
    y.add_item(File('i', 10))
    x.add_item(y)
    x.add_item(File('h', 10))
    ca.add_item(x)
    hdd.add_item(ca)
    z = Folder('z')
    z.add_item(File('g', 20))
    hdd.add_item(z)
    print(hdd.get_size())
    print(hdd.get_items())
    print(hdd.get_subfolders())
    print(hdd.get_subfolders_with_max_size(30))