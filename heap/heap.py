class Heap:
    def __init__(self):
        # storage starts with an unused 0 to make
        # integer division simpler later on
        self.storage = [0]
        self.size = 0

    def insert(self, value):
        # append value to the end
        self.storage.append(value)
        # increase size counter
        self.size += 1
        # bubble up the last item on array which was just appended
        self._bubble_up(self.size)

    def delete(self):
        if len(self.storage) == 1:
            return None
        removed_placeholder = self.storage[1]

        # overwrite top/max value with value at the end of array
        self.storage[1] = self.storage[self.size]
        self.storage.pop()  # remove the last element which was copied to front
        self.size -= 1  # reduce size by 1

        if self.size > 0:
            # sift the previouly last value to a lower place
            self._sift_down(1)

        return removed_placeholder

    def get_max(self):
        if self.size > 0:
            return self.storage[1]
        else:
            return None

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        # while storage[index] has a parent "node"
        while index // 2 > 0:
            # if parent is < child
            if self.storage[index//2] < self.storage[index]:
                # pythonic way of switching elements in array
                self.storage[index//2], self.storage[index] = (
                    self.storage[index], self.storage[index//2]
                )
            # if parent is not < child, then break while-loop
            else:
                break
            # reset condition for while loop
            index = index // 2

    def _sift_down(self, index):
        # function to return index of child with max value
        def max_child_index_finder(index):
            # if right child doesn't exist, return index of left child
            if index * 2 + 1 > self.size:
                return index * 2
            else:
                # return the index of the child with the higher value
                return max(index*2, index*2+1, key=lambda x: self.storage[x])

        # If left child exists
        while (index * 2) <= self.size:
            # find max_child_index
            max_child_index = max_child_index_finder(index)
            # if parent is smaller than max child: swap values
            if self.storage[index] < self.storage[max_child_index]:
                self.storage[index], self.storage[max_child_index] = (
                    self.storage[max_child_index], self.storage[index]
                )
            else:
                # stop condition if parent is larger than both children
                break
            # reset index value for while loop
            index = max_child_index

