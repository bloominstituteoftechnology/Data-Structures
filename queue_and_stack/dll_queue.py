import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        return self.size

    def dequeue(self):
        if self.size < 1:
            return None
        self.size -= 1
        return self.storage.remove_from_head()
        

    def len(self):
        return self.size
