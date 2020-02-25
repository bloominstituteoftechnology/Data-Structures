import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


#class Queue:
#    def __init__(self):
#        self.size = 0
        # we start from zero
        # self.storage = ?
#        self.storage = DoublyLinkedList()

#    def enqueue(self, value):
#        self.size += 1
#        return self.storage.add_to_head(value)
#
#    def dequeue(self):
#        if self.size > 0:
#            return self.storage.remove_from_tail()
#        else:
#            return None
#    def len(self):
#        return self.size

class Queue: # first in first out
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        pass
    def is_empty(self):
        return self.size == 0

    def enqueue(self, value): #
        self.size += 1
        return self.storage.add_to_head(value)

    def dequeue(self):
        pass
        if self.is_empty():
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        pass
        return self.size
