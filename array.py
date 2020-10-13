"""
First homework assignment in the course "Python".

Created by Emdin Grigory.
"""


class Array(object):  # noqa: WPS214
    """Сlass of "lists" with functionality like a list."""

    def __init__(self, *elements):
        """
        Init class.

        Args:
             elements: elements to init.
        """
        self._data = elements  # noqa: WPS110

    def append(self, element):
        """
        Add elements.

        Args:
            element: elements to add.
        """
        self._data = self._data + (element,)  # noqa: WPS110

    def index(self, element):
        """
        Find the first occurrence of the specified value.

        Args:
            element: element to search for.

        Returns:
            index of the first element or (-1) if the element is not present.
        """
        try:
            pos = self._data.index(element)
        except ValueError:
            pos = -1
        return pos

    def pop(self, index):
        """
        Delete values by index.

        Args:
            index: index to delete.
        """
        self._data = self._data[:index] + self._data[index + 1:]  # noqa: WPS110 E501

    def remove(self, element):
        """
        Delete element by value.

        Args:
            element: element to delete.
        """
        index = self.index(element)
        if index != -1:
            self.pop(index)

    def get_data(self):
        """
        Get storage with elements.

        Returns:
            storage with elements.

        """
        return self._data

    def __add__(self, other):
        """
        Add two instances of the class Array.

        Args:
            other: instance to add.

        Returns:
            sum of two instances.

        Raises:
            TypeError: other is not instance of Array
        """
        if isinstance(other, Array):
            sum_data = self._data + other.get_data()  # noqa: WPS110
            return Array(*sum_data)
        raise TypeError

    def __eq__(self, other):
        """
        Compare two instances for equality.

        Args:
            other: instance to compare.

        Returns:
            True if instances are equal, False else.
        """
        if isinstance(other, Array):
            return self._data == other.get_data()
        return False

    def __len__(self):
        """
        Return length of data.

        Returns:
            length
        """
        return len(self._data)

    def __getitem__(self, index):
        """
        Get element by index.

        Args:
            index: index to element.

        Returns:
            element by index.
        """
        return self._data[index]
