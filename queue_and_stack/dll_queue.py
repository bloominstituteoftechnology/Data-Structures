import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
         self.storage = DoublyLinkedList

    #adding to the tail of the queue
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
    #removing the first item and returning an item from the front of the queue
    def dequeue(self):
        if self.size == 0:
            return None
    else: 
        value = self.storage.remove_from_head()
        self.size -= 1
        return value
        

    def len(self):
        return self.size
