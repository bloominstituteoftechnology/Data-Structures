import sys
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList

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
# 1. Array
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if self.storage == []:
#             return None
#         else:
#             return self.storage.pop(0)

# 2. Linked List
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if len(self) >= 1: # if length is greater than or equal to 1, 
            self.size -= 1 # then you can minus 1 until you reach 0
        return self.storage.remove_head()

# 3. What is the difference between using an array vs. a linked list when implementing a Queue?
# When using a queue, the difference is adding a tail.
# An array can simply append the element to the last instance, whereas in a linked list
# the "last element" would have to be updated to point to the "new last element", and
# the "new last element" would have to point to None.