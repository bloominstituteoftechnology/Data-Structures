import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # It is a very efficient structure to implement queues with a O(n) complexity.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_(value)

    def dequeue(self):
        self.size -= 1
        value = self.storage.head.value
        self.storage.remove_from_head()
        self.size -= 1
        return value

    def len(self):
        return self.size