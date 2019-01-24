class Heap:
    def __init__(self):
        self.storage = []

    # O(log n)
    def insert(self, value):
        self.storage.append(value)  # O(1)
        self._bubble_up(len(self.storage) - 1)  # O(log n)

    # O(log n)
    def delete(self):
        if len(self.storage) > 1:
            old_value = self.storage[0]  # O(1)
            self.storage[0] = self.storage[-1]  # O(1) to look up in an array
            self.storage.pop()  # O(1) to pop from end of array
            self._sift_down(0)  # O(log n)
            return old_value
        # only one number left in heap so no need for _sift_down
        elif len(self.storage) == 1:
            old_value = self.storage[0]
            self.storage = []  # O(1)
            return old_value

    # O(1)
    def get_max(self):
        return self.storage[0]

    # O(1)
    def get_size(self):
        return len(self.storage)

    # O(log n)
    def _bubble_up(self, index):
        # if it's the first in storage, there's none above it
        if index == 0:
            return
        # index // 2 will always be parent node (but 0 indexing)
        parent_index = ((index + 1) // 2) - 1
        # if node is larger than parent
        if self.storage[index] > self.storage[parent_index]:
            # swap parent and child - O(1)
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            #  increment to prepare for next loop
            return self._bubble_up(parent_index)

    def _sift_down(self, index):
        # get first child
        first_child_index = (index + 1) * 2 - 1
        # if no child
        if first_child_index > len(self.storage) - 1:
            return
        # if one child
        elif first_child_index == len(self.storage) - 1:
            if self.storage[index] < self.storage[first_child_index]:
                # swap parent and child - O(1)
                self.storage[index], self.storage[first_child_index] = self.storage[first_child_index], self.storage[index]
                #  increment to prepare for next loop
                return self._sift_down(first_child_index)
        # has two children
        else:
            second_child_index = first_child_index + 1
            larger_index = first_child_index
            second_is_larger = False
            if self.storage[second_child_index] > self.storage[first_child_index]:
                larger_index = second_child_index
                second_is_larger = True
            if self.storage[index] < self.storage[larger_index]:
                # swap parent and child - O(1)
                self.storage[index], self.storage[larger_index] = self.storage[larger_index], self.storage[index]
                #  increment to prepare for next loop
                return self._sift_down(larger_index)                
