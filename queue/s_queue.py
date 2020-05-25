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
"""
import sys
sys.path.append('../stack')
from array_stack import Stack

class Queue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()
    
    def __len__(self):
        return(len(self.push_stack) + len(self.pop_stack))

    def enqueue(self, value):
        while len(self.pop_stack) > 0:
            self.push_stack.push(self.pop_stack.pop())
        self.push_stack.push(value)
                
    def dequeue(self):
        if len(self.push_stack) == 0 and len(self.pop_stack) == 0:
            return None
        else:
            while len(self.push_stack) > 0:
                self.pop_stack.push(self.push_stack.pop())
            return self.pop_stack.pop()
