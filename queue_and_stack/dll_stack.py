import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.dll = DoublyLinkedList()

    def push(self, value):
        self.size +=1
        self.dll.add_to_tail(value)

    def pop(self):
        if self.size ==0:
            return
        else:
            self.size -=1

            value = self.dll.remove_from_tail()
            return value

    def len(self):
        return self.size
