class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # append value to storage
        self.storage.append(value)
        # bubble up pass in last index
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # store max value to return at end
        max_val = self.storage[0]
        # swap first and last
        self._swap_indices(0, len(self.storage) - 1)
        # remove last index
        self.storage.pop()
        # call sift down to move max back to top and min back to bottom
        self._sift_down(0)
        # return max value
        return max_val

    def get_max(self):
        # Max at index 0
        return self.storage[0]

    def get_size(self):
        # return length of storage
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index == 0 and self.storage[parent_index] < self.storage[index]:
            self._swap_indices(parent_index, index)

        if self.storage[parent_index] < self.storage[index]:
            self._swap_indices(parent_index, index)
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        # get max_child index
        max_child = self._max_child(index)
        # return if max child index is greater than max storage index
        if max_child > len(self.storage)-1:
            return
        # swap max shild and parent
        self._swap_indices(max_child, index)
        # repeat
        self._sift_down(max_child)

    def _swap_indices(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def _max_child(self, index):
        left_child = index * 2 + 1
        right_child = index * 2 + 2
        # check for right child
        if right_child > len(self.storage) - 1:
            # if no right child then max child is left child
            return left_child
        else:
            # Compare right and left childs and return greater one
            if self.storage[left_child] > self.storage[right_child]:
                return left_child
            else:
                return right_child
