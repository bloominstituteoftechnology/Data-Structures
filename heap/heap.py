class Heap:
    def __init__(self):
        # storage starts with an unused 0 to make
        # integer division simpler later on
        self.storage = [0]
        self.size = 0

    def insert(self, value):
        # add the value to the end of the heap
        self.storage.append(value)
        # increment the size of the heap
        self.size += 1
        # call helper function _bubble_up with the index self.size
        self._bubble_up(self.size)

    def delete(self):
        # assign a variable to the element at index 1
        # (which we'll be using as our max/head of heap)
        retval = self.storage[1]
        # assign the value of the last element of the heap
        # to the element at index 1
        self.storage[1] = self.storage[self.size]
        # decrement the size of the heap
        self.size -= 1
        # remove the last element of the heap
        self.storage.pop()
        # call helper method _self_down with 1 as index
        self._sift_down(1)
        # return the variable given to the previous head of heap
        return retval

    def get_max(self):
        # we're using the 1st index as the max/head,
        # return the first index
        return self.storage[1]

    def get_size(self):
        # return self.size
        # pretty self-explanatory
        return self.size

    def _bubble_up(self, index):
        # perform a while loop that runs
        # while the value of the index divided by 2 is less than 0
        # index // 2 looks at the parent of the current index
        while index // 2 > 0:
            # if the parent is less than the current index
            # swap current index's place with its parent
            if self.storage[index // 2] < self.storage[index]:
                self.storage[index // 2], self.storage[index] = (
                    self.storage[index],
                    self.storage[index // 2],
                )
            else:
                # if the parent is not less than the current index
                # break
                break
            # assign the value of the current index divided by 2
            # to the variable index to create a new index
            index = index // 2

    def _sift_down(self, index):
        # the children of an element of a heap are represented by
        # i = current index
        # 2i = left
        # 2i + 1 = right
        # run a while loop while the current index has children
        while (index * 2) <= self.size:
            # create a variable set to the function _max_child
            # pass that function the current index
            max_child = self._max_child(index)
            # if the current index is smaller than one of the children
            # swap places with the largest child
            if self.storage[index] < self.storage[max_child]:
                self.storage[index], self.storage[max_child] = (
                    self.storage[max_child],
                    self.storage[index],
                )
            else:
                # if current index is not smaller than a child,
                # break
                break
            # set the index for the next iteration
            # to the value of max child
            index = max_child

    def _max_child(self, index):
        # we already test if index * 2 <= self.size in _sift_down,
        # so we have to test here to see if index * 2 + 1
        # is larger than self.size
        # if it is larger than self.size, we can return index * 2
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            # if index * 2 + 1 is not larger than self.size,
            # test which is larger:
            # self.storage[index * 2] or self.storage[index * 2 + 1]
            # return whichever index refers to the larger number
            return (
                index * 2
                if self.storage[index * 2] > self.storage[index * 2 + 1]
                else index * 2 + 1
            )
