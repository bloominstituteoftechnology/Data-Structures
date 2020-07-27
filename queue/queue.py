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

  ANSWER:
   An array contains all elements together in memory. A linked list has nodes, distributed throughout memory, that have pointers referencing the next node, making them more memory efficient. When building a Queue, 
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()
        
    def __len__(self):
        return self.linked_list.count

    def enqueue(self, value):
        self.linked_list.add_to_tail(value)

    def dequeue(self):
        if self.linked_list.count > 0:
          return self.linked_list.remove_head()
        else:
          pass
