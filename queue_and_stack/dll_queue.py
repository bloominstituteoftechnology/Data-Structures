import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# Why is our DLL a good choice to store our elements?
# Deques are a generalization of stacks and queues 
# (the name is pronounced "deck" and is short for "double-ended queue").
#  Deques support thread-safe, memory efficient appends and pops from either
#  side of the deque with approximately the same O(1) performance in either direction.
#  self.storage = ?
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        

    def dequeue(self):
        #check if the list is there
        if self.size == 0:
            print("Nothing s there!")
            return
        remove_value = self.storage.head.value
        self.storage.remove_from_head()
        self.size -= 1
        return remove_value
        

    def len(self):
        return self.size
