"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import ListNode
from singly_linked_list import LinkedList
import numpy as np

class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = np.array([])
        self.storage = LinkedList(None)
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        # When you form a queue you add to the head
        # self.storage = np.insert(self.storage, 0, value)
        self.storage.add_to_head(value)
        self.size += 1
        return

    def dequeue(self):
        # When you leave the queue you leave from the tail
        if self.size == 0:
            return None
        else:
            # delvalue = self.storage[-1]
            # self.storage = self.storage[:-1]
            # self.size -= 1
            # return delvalue
            tail_value = self.storage.tail.value
            self.storage.remove_tail()
            self.size -= 1
            return tail_value
