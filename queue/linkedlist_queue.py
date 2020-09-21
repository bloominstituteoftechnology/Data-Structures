import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

class ll_queue:
    def __init__(self):
        self.size = 0 
        self.storage = LinkedList()

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
            return self.storage.remove_head()

    def printlist(self):
        self.storage.print_val()