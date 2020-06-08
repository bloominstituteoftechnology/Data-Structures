from singly_linked_list.singly_linked_list import LinkedList

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

# array
# class Queue:
#     def __init__(self):
#         self.storage = []
#         self.length = 0

#     def __len__(self):
#         return self.length

#     def enqueue(self, value):
#         self.length += 1
#         self.storage.append(value)

#     def dequeue(self):
#         try:
#             removed = self.storage.pop(0)
#             self.length -= 1
#             return removed
#         except:
#             return None

# linked list


class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def enqueue(self, value):
        try:
            self.storage.add_to_tail(value)
        except:
            return None

    def dequeue(self):
        try:
            prev_head = self.storage.remove_head()
            return prev_head
        except:
            return None
