import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        # if no item in stack, do nothing
        if not self.storage.head and not self.storage.tail:
            return
        else:

            self.size -= 1

            # remove item from front of stack
            return self.storage.remove_from_head()

    def len(self):
        return self.size
