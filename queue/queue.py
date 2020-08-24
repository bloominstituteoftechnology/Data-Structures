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
# Queue using an array
class Queue:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.items != []:
            return self.items.pop(0)
        else:
            return None

#Queue using a linked list
from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.items = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.items.add_to_tail(value)
        

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1 
            return self.items.remove_head()

