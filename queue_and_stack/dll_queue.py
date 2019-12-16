import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # More efficient to add and remove items from the queue and no up front memory allocation (queue can grow as big as it needs to) with a DLL.
        # self.storage = DoublyLinkedList()
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        if self.size == 0:
            self.storage.add_to_tail(value)
        else:
            self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.storage.tail is None:
            return None
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
