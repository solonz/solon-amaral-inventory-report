from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current_data = 0

    def __next__(self):
        data = self.data[self.current_data]
        if not self.data:
            raise StopIteration()
        self.current_data += 1
        return data
