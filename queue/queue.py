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


'''
Queue class with array storage structure.
'''

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if self.size < 1:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)
        


'''
Queue class with list storage structure.
'''

# class Queue:
#     class Node:
#         def __init__(self, element):
#             self.element = element
#             self.next = None
            
#         def get_value(self):
#             return self.element
        
#         def get_next(self):
#             return self.next
        
#         def set_next(self, target):
#             self.next = target
            
#         def is_empty(self):
#             return self is None
    
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
    
#     def __len__(self):
#         return self.size
    
#     def enqueue(self, element):
#         self.size += 1
#         new_node = self.Node(element)
        
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node
    
#     def dequeue(self):
#         if self.head is None and self.tail is None:
#             return None
#         else:
#             self.size -= 1
#             old_head = self.head.get_value()
#             if self.head.get_next() is None:
#                 self.head = None
#                 self.tail = None
#             else:
#                 self.head = self.head.get_next()
#             return old_head
    
#     def first(self):
#         if self is None:
#             return None
#         else:
#             return self.head.element
            
            
# s = Queue()
# s.enqueue(1)
# s.enqueue('two')
# s.enqueue(3)
# s.enqueue('four')
# print(s.first())