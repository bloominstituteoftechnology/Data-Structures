class Heap:
    def __init__(self):
        self.storage = []

    def get_parent_index(self, index):
        if index == 0:
            return 0
        return (index-1) // 2

    def insert(self, value):
        self.storage.append(value)
        current_index = len(self.storage) - 1
        self._bubble_up(current_index)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        if index is not 0:
            current_index = index
            parent_index = self.get_parent_index(current_index)
            current_value = self.storage[current_index]
            parent_value = self.storage[parent_index]
            if parent_value < current_value:
                self.storage[current_index] = parent_value
                self.storage[parent_index] = current_value
                if parent_index != 0:
                    self._bubble_up(parent_index)

    def _sift_down(self, index):
        pass
