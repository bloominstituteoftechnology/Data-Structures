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
    
    #removing the first item and returning an item from the front of the queue
    def dequeue(self):
        if self.size == 0: 
            return None
        else: 
            new_head = self.storage.remove_from_head()
            self.size -=1 #DO NOT FORGET TO DECREMENT FROM THE SIZE
        return new_head
        

    def len(self):
        return self.size
