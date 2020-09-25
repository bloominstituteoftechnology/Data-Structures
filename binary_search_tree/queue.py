import sys
sys.path.append('../singly_linked_list/')
sys.path.append('../stack/')
from singly_linked_list import LinkedList
from stack import Stack

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
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.pop(0)

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#         return self.storage.remove_head()

class Queue:
    def __init__(self):
        self.size = 0
        # 2 stacks required
        self.push_stack = Stack()
        self.pop_stack = Stack()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.push_stack.push(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
        # re-stack to reverse order
        while self.push_stack.size > 0:
            self.pop_stack.push(self.push_stack.pop())
        # pop off one
        value = self.pop_stack.pop()
        # restack to original stack, original order
        while self.pop_stack.size > 0:
            self.push_stack.push(self.pop_stack.pop())
        return value