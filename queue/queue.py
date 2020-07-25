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

from singly_linked_list.singly_linked_list import Node, LinkedList

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return len(self.storage)
#
#     # adds an element to the end
#     def enqueue(self, value):
#         self.storage.insert(0, value)
#
#     # removes an element from the end
#     def dequeue(self):
#         if self.storage != []:
#             return self.storage.pop()
#         else:
#             return None

# implementing Queue class, using linked list implementation
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    # adds an element to the end
    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    # removes an element from the end
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            node = self.storage.remove_head()
            return node
        else:
            return None

