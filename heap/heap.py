class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) > 1:
            old_value = self.storage[0]
            self.storage[0] = self.storage[-1]
            self.storage.pop()
            self._sift_down(0)
            return old_value
        elif len(self.storage) == 1:
            old_value = self.storage[0]
            self.storage = []
            return old_value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return
        parent_index = ((index + 1) // 2) - 1
        if self.storage[index] > self.storage[parent_index]:
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]

            return self._bubble_up(parent_index)

    def _sift_down(self, index):

        first_child_index = (index + 1) * 2 - 1

        if first_child_index > len(self.storage) - 1:
            return

        elif first_child_index == len(self.storage) - 1:
            if self.storage[index] < self.storage[first_child_index]:

                self.storage[index], self.storage[first_child_index] = self.storage[first_child_index], self.storage[index]

                return self._sift_down(first_child_index)

        else:
            second_child_index = first_child_index + 1
            larger_index = first_child_index
            second_is_larger = False
            if self.storage[second_child_index] > self.storage[first_child_index]:
                larger_index = second_child_index
                second_is_larger = True
            if self.storage[index] < self.storage[larger_index]:

                self.storage[index], self.storage[larger_index] = self.storage[larger_index], self.storage[index]

                return self._sift_down(larger_index)
