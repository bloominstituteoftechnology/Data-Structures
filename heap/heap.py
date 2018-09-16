import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        value_index = self.get_size() - 1
        self._bubble_up(value_index)

    def delete(self):
        to_delete = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(0)
        return to_delete

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if self.storage[parent] < self.storage[index]:
            self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
            if parent != 0:
                self._bubble_up(parent)
            return
        """Sean Solution
            while (index - 1) // 2 >= 0:
              if self.storage[(index - 1) // 2] < self.storage[index]:
                self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
              index = (index - 1) / 2

        """

    def _sift_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child > self.get_size() - 1:
            return
        if right_child > self.get_size() - 1:
            return
        if self.storage[left_child] > self.storage[index]:
            self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
            self._sift_down(left_child)
        if self.storage[right_child] > self.storage[index]:
            self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
            self._sift_down(right_child)
        """ Sean Solution
        while (index *2 + 1) <= len(self.storage) - 1:
          mc = self._max_child(index)
          if self.storage[index] < self.storage[mc]:
            self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
          index = mc
        

        def _max_child(self, index):
          if index * 2 + 2 > len(self.storage) - 1:
            return index * 2 + 1
          else:
            return index * 2 + 1 if self.storage[index *2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2
        """
