import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


"""
https://he-s3.s3.amazonaws.com/media/uploads/cf1e1c1.png
Queue is a FIFO based data structure
Enqueue: Insert the element from the tail
Dequeue: Delete the element from the head 
"""

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # because of easy traversal
        # Because DLL allows to track the pointers(front and tail)
        # Dynamic memory allocation. *Ease of insertion and deletion
        self.storage = DoublyLinkedList()

    def enqueue(self, value):#PUSH
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self): #POP
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
