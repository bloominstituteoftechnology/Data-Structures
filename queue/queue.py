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
from singly_linked_list import LinkedList
from stack import Stack
# Using arrays

# class Queue:
#     def __init__(self, ls=[]):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         if self.size <= 0:
#             return 0
#         else:
#             return self.size

#     def enqueue(self, value):
#         self.size +=1
#         return self.storage.append(value)

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size += -1
#             return self.storage.pop(0)

# For Linked Lists
class Queue:
    def __init__(self):
        self.size = 0
        self.link = LinkedList()
        self.first = None
    
    def __len__(self):
        if self.size <= 0:
            return 0
        else:
            return self.size

    def enqueue(self, value):
        self.size += 1
        self.link.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size += -1
            return self.link.remove_head()

# Stretch 
class QueueWithStack:
    def __init__(self):
        self.size = 0
        self.stacks1 = Stack()
        self.stacks2 = Stack()

    def __len__(self):
        if self.size <= 0:
            return 0
        else:
            return self.size
    
    def enqueue(self, value):
        self.size += 1
        self.stacks1.push(value)

    def dequeue(self):
        """
        We can only pop of the end right now, but we need to get to the head
        use the second stack to hold everything
        """
        if self.size == 0:
            return None
        else:
            while self.stacks1.size > 1:
                self.stacks2.push(self.stacks1.pop())
            # hold the head to return it
            popped = self.stacks1.pop()
        
            # Gotta push them all back to preserve order
            while self.stack2.size > 0:
                self.stack1.push(self.stack2.pop())
            self.size += -1
            return popped