import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size+=1
        return self.storage.add_to_head(value)
    def is_empty(self):
        return self.size==0


    def dequeue(self,value):
        if self.is_empty():
            return
        else:
            self.size -=1
            return self.storage.remove_from_tail(value)

    def len(self):
        return self.size