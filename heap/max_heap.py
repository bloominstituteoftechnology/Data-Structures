class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) <= 0:
            return None
        else:
            old_max = self.storage[0]
            if len(self.storage) > 1:
                self.storage[0] = self.storage.pop(-1)
                self._sift_down(0)
            else:
                self.storage.pop(0)
            return old_max

    def get_max(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.storage[index] > self.storage[parent_index]:
            self.storage[parent_index], self.storage[index] = \
                self.storage[index], self.storage[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self, index):
        if len(self.storage) > 2 * index + 2:
            left_child = self.storage[2 * index + 1]
            right_child = self.storage[2 * index + 2]
            if left_child >= right_child:
                max_child_index = 2 * index + 1
            else:
                max_child_index = 2 * index + 2
        elif len(self.storage) > 2 * index + 1:
            max_child_index = 2 * index + 1
        else:
            return
            
        while index < len(self.storage) - 1 and \
            self.storage[index] < self.storage[max_child_index]:
                self.storage[max_child_index], self.storage[index] = \
                    self.storage[index], self.storage[max_child_index]
                index = max_child_index
                if len(self.storage) > 2 * index + 3:
                    left_child = self.storage[2 * index + 1]
                    right_child = self.storage[2 * index + 2]
                    if left_child >= right_child:
                        max_child_index = 2 * index + 1
                    else:
                        max_child_index = 2 * index + 2
                elif len(self.storage) > 2 * index + 2:
                    max_child_index = 2 * index + 1
