from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')

# stack uses LIFO (last in, first out)
# versus queue, which uses FIFO (first in, first out)


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Pretty straight-forward to add to head & tail, and remove from head & tail.
        # Doesn't need an up-front allocation of memory.
        # But in this case, time complexity is the same, whether you use a DLL or an array. ??
        self.storage = DoublyLinkedList()

    def push(self, value):
        # add to tail
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # remove from tail
        value = self.storage.remove_from_tail()
        if self.len() > 0:
            self.size -= 1
        return value

    def len(self):
        return self.size
