"""  
Left child: 2i + 1
Right: Child: 2i + 2
Parent: (index - 1) // 2
"""

"""
Heap Property
In a max heap, the heap property is that every node is >= both of its children.
"""


class Heap:
    def __init__(self):
        self.storage = [87, 79, 74]

    """ insert adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap 
    add the new value to the end of the array
    call _bubble_up to get that value into its correct index
    """

    def insert(self, value):
        # add of value to the end of the array
        self.storage.append(value)
        # print(self.storage)
        # call bubble up to get it in the correct spot
        self._bubble_up(len(self.storage) - 1)
        # print(self.storage)

    """ delete removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed."""

    def delete(self):
        pass

    """ get_max returns the maximum value in the heap in constant time. """

    def get_max(self):
        pass

    """ get_size returns the number of elements stored in the heap. """

    def get_size(self):
        pass

    """ _bubble_up moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index. 
    
    the index argument that is passed into bubble_up 
    is the index of element that we just appended
    aka the last index
    """

    def _bubble_up(self, index):
        while index > 0:
            # get the parent index
            parent_index = (index - 1) // 2
            # check if the inserted element is bigger than the parent
            current = self.storage[index]
            parent = self.storage[parent_index]
            if current > parent:
                # it's greater, swap them
                self.storage[index], self.storage[parent_index] = parent, current
                # update index to be the parent index
                index = parent_index
            else:
                # it's not bigger
                # that means the element is in its correct spot
                break

    """ _sift_down grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent. """

    def _sift_down(self, index):
        pass


heap = Heap()

heap.insert(80)
print(heap.storage)