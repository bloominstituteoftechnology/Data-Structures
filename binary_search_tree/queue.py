import collections 
from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
"""

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add value to the end
        self.size = self.size + 1
        self.storage.append(value)
        return value


    def dequeue(self):
        if self.size == 0:
            return None
        # remove item from the beginning
        self.size = self.size - 1
        return self.storage.pop(0)

"""
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
"""

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         # add value to the end
#         self.size = self.size + 1
#         self.storage.add_to_tail(value)
#         return value


#     def dequeue(self):
#         if self.size == 0:
#             return None
#         # remove item from the beginning
#         self.size = self.size - 1
#         value = self.storage.remove_head()
#         return value


"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""