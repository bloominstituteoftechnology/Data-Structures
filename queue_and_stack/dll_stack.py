import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        #check if the list is there
        if self.size == 0:
            print("Nothing s there!")
            return

        
        self.size -= 1
        return self.storage.remove_from_head()
        


    def len(self):
        return self.size
