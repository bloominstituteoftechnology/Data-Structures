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

# class Queue:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
    
#     def __len__(self):
#         pass

#     def enqueue(self, value):
#         pass

#     def dequeue(self):
#         pass


'''
Queue class with list storage structure.
'''

class Queue:
    class Node:
        def __init__(self, element):
            self.element = element
            self.front = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, element):
        new_node = self.Node(element)
        
        if self.tail.is_empty():
            self.tail.front = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1
    
    def dequeue(self):
        if self:
            self.head = self.head.front
        else:
            return None
    
    def first(self):
        if self.is_empty():
            return None
        else:
            return self.head.element
            
            
s = Queue()
s.enqueue(1)
s.enqueue('two')
s.enqueue(3)
s.enqueue('four')
print(s.first())