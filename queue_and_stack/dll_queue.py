import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        #DLL offers 'dynamic memory allocation' and ease of insertion/deletion
        # self.storage = ?

    def enqueue(self, value):
        self.size +=1
        self.storage.add_to_tail(value)
            

    def dequeue(self):
        if self.size is 0:
            return 
        self.size -= 1
        return self.storage.remove_from_head() 

    def len(self):
        
        return self.size

   


