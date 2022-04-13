# Implementing a stack using a python list


class ArrayStack:
    """LIFO Stack implementation"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        """return but do not remove element at the top"""

        """If empty raise an empty exception"""
        if self.is_empty():
            raise Exception('Stack is empty.')
        return self._data[-1]  # Last item in the list

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty.')
        return self._data.pop()  # remove last item from the list
