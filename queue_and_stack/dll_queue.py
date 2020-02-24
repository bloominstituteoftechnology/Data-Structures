import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self, value=None):
        self.size = 0
        self.storage = DoublyLinkedList(value)
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        # pass
        self.size += 1
        self.storage.add_to_head(value)
        """Adds to the back of the Queue"""

    def dequeue(self):
        
        value = self.storage.remove_from_tail()
        if not value==None:
            print('this is the value ',value)
            self.size -= 1
            return value
        else:
            # print('this is the value when none ',value)
            return value
        


    def len(self):
        # pass
        return self.size
        """takes the length of the queue"""


