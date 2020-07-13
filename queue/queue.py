# Implement the Stack and Queue classes using built-in Python lists 
# and the Node and LinkedList classes you created during the 
# Module 1 Guided Project.

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

# Has the methods: enqueue, dequeue, and len.
# enqueue adds an element to the back of the queue.
# dequeue removes and returns the element at the front of the queue.
# len returns the number of elements in the queue.

# Array implementation of Queue class
class Queue:
    """Array implementation of Queue class"""
    def __init__(self):
        self.size = 0
        # self.storage = ?
    
    def __len__(self):
        """Returns the number of elements in the queue"""
        pass

    def enqueue(self, value):
        """Adds an element to the back of the queue"""
        pass

    def dequeue(self):
        """Removes and returns the element at the front of the queue"""
        pass


# # OOP implementation of Queue class
# class Queue:
#     """OOP implementation of Queue class using Node and LinkedList classes"""
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
    
#     def __len__(self):
#         """Returns the number of elements in the queue"""
#         pass

#     def enqueue(self, value):
#         """Adds an element to the back of the queue"""
#         pass

#     def dequeue(self):
#         """Removes and returns the element at the front of the queue"""
#         pass