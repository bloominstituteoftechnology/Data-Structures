class Heap:
    def __init__(self):
        self.storage = []
        self.count = 0

    def insert(self, value):
        self.storage.append(value)
        self.count += 1
        parent = self.storage[_get_parent(self.count - 1)]
        while parent < value:
            current_index = self._bubble_up(self.count - 1)
            parent = _get_parent(current_index)
        # COME BACK TO THIS

    def delete(self):
        top_value = self.storage[0]
        self.storage.pop[0]
        # COME BACK TO THIS
        return

    def get_max(self):
        return self.storage[0]

    def _get_parent(self, index):
        # returns index of parent node
        return (index - 1) // 2

    def _get_left(self, index):
        # return left child of parent node
        left_index = index * 2 + 1
        if left_index > len(self.storage) - 1:
            return None
        else:
            return left_index

    def _get_right(self, index):
        # returns right child of parent node
        right_index = index * 2 + 2
        if right_index > len(self.storage) - 1:
            return None
        else:
            return right_index

    def _bubble_up(self, index):
        if _get_parent(index) > self.storage[index]:
            # swap_var =
            self._bubble_up(index)
        pass

    def _sift_down(self, index):
        pass
