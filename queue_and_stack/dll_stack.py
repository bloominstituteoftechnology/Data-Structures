import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack(DoublyLinkedList):
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        #increment size
        self.size+= 1
        if self.storage.head == None:
            self.storage.add_to_head(value)
        else:
            self.storage.add_to_tail(value)


    def pop(self):
        if self.size == 0:
            return None
        #decrease size
        self.size -= 1
        #store tail for return
        tor = self.storage.tail.value
        self.storage.remove_from_tail()
        return tor

    def len(self):
        return self.size
