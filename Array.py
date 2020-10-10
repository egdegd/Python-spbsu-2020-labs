class Array(object):
    def __init__(self, *elements):
        self._data = elements

    def append(self, element):
        self._data = self._data + (element,)

    def index(self, element):
        try:
            pos = self._data.index(element)
        except ValueError as err:
            pos = -1
        return pos

    def pop(self, index):
        self._data = self._data[:index] + self._data[index + 1:]

    def remove(self, element):
        index = self.index(element)
        if index != -1:
            self.pop(index)

    def __add__(self, other):
        res = Array()
        res._data = self._data + other._data
        return res

    def __str__(self):
        return str(self._data)

    def __eq__(self, other):
        return self._data == other._data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

