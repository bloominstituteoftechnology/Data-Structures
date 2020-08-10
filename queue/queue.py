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
################################ 1 ####################################
# This implementation of the Queue class is built with an underlying
# storage structure of an empty array

# # it passes all tests
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             x = self.storage[0]
#             self.storage.pop(0)
#             self.size = len(self.storage)
#             return x
  



################################### 2 ########################################
# This class utilizes an empty version of the LinkedList, and passes all test_queue.py

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
        if self.size == 0:
            return None
        else:
            x = self.storage.head.get_value()
            self.storage.remove_head()
            self.size += -1
            return x


############################### 3 ###############################
# 3. What is the difference between using an array vs. a linked list when 
#    implementing a Queue?

# The main difference between using an array vs a linked list is the ability to access
# elements of the data structure via indexing. This is possible in arrays but if you
# work with linked lists it will make a difference on how you operate
# on the underlying structure. Since arrays are a core part of python programming,
# we can use python ready methods to manipulate our data. Arrays can have their elements
# directly called upon through indexing. When working with linked lists, we have to 
# iterate through the list to find the values we need, and we have to use customized
# methods to do so.