from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()


    def len(self):
        return len(self.storage)
"""
Alternative Method from Tuesday 10/15/2019 Live Lecture w/ Brian Doyle

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self,value):
        self.storage.add_to_tail(value)
        self.size +=1
    
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
"""