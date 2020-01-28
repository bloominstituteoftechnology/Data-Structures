import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = []

    def enqueue(self, value):
        if value not in self.storage:
            ## Add item into queue
            self.storage.insert(0, value)
            return True
        return False

    def dequeue(self):
        # Check if queue is empty
        if len(self.storage) > 0:
            return self.storage.pop()
        return None

    def len(self):
        return len(self.storage)
