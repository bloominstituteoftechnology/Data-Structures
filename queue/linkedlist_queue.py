import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class ll_queue:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __len__(self):
        return len(self.storage)

    def enqueue(self,value):
        self.storage.add_to_head(value)

    def dequeue(self):
        return self.storage.remove_from_tail()

    def printlist(self):
        self.storage.print_val()