import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class dll_queue():
    def __init__(self):
        self.storage = DoublyLinkedList()
        self.size = len(self.storage)

    def __len__(self):
        return self.size

    def enqueue(self,value):
        self.storage.add_to_tail(value)
        self.size +=1

    def dequeue(self):
        if self.size == 0:
            return None
        else: 
            self.size -= 1
            return self.storage.remove_from_head()