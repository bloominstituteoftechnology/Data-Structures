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
#class Queue:
#    """Array (a.k.a. list) implementation of Queue data structure"""
#
#    def __init__(self):
#        """Initialize array-based Queue class"""
#
#        self.queue = []
#    
#    def __len__(self):
#        """Return length of Queue class"""
#
#        return len(self.queue)
#
#    def enqueue(self, value):
#        """Add an element to initialized Queue class"""
#
#        self.queue.append(value)
#
#    def dequeue(self):
#        """Remove least recently added element from Queue class"""
#
#        if len(self.queue) < 1:
#            return None
#        else:
#            return self.queue.pop(0)

from singly_linked_list import LinkedList 


class Queue:
    """Singly-linked list implementation of Queue data structure"""

    def __init__(self):
        """Initialize singly-linked list-based Queue class"""

        self.size = 0
        self.queue = LinkedList()

    def __len__(self):
        """Return length of Queue class"""

        return self.size

    def enqueue(self, value):
        """Add an element to initialized Queue class"""

        self.queue.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        """Remove least recently added element from Queue class"""

        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.queue.remove_head()




