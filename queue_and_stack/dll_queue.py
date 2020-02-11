import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# FIFO -- FIRST IN FIRST OUT -- WAITING IN LINE AT 711, DMV, ETC
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # Add item to back of queue
    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    # Remove and return item from front of queue
    def dequeue(self):
        if self.size is not 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None
    # Number of items in queue
    def len(self):
        return self.size
