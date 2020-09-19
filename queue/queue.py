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
import sys
sys.path.append("../singly_linked_list")
from singly_linked_list import LinkedList


# class Queue:
#     def __init__(self):
#         self.storage = []
#         # self.storage = ?
#
#     def __len__(self):
#         return len(self.storage)
#
#     def enqueue(self, value):
#         self.storage.append(value)
#
#     def dequeue(self):
#         while len(self.storage) == 0:
#             return None
#         return self.storage.pop(0)
# Array

# LinkedList Implementation of queue
class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, item):
        self.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.remove_head()

if __name__ == "__main__":
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
