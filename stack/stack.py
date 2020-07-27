"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
#  LIFO Order  
# You can only push to add a new element to the top of the stack, pop to remove the element from the top, and peek at the top element without popping it off.
class Stack:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self): #remove last one
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop()

#  Do the same with  linked list
# A linked list is a sequence of data items, just like an array. But where an array allocates a big block of memory to store the objects, the elements in a linked list are totally separate objects in memory and are connected through links:
#use Node instead of Stack
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.items = LinkedList()
# Data Structures HW/Data-Structures/singly_linked_list/singly_linked_list.py
# /Users/lambdacatalina/Desktop/LAMBDA-SCHOOL/COMPUTER SCIENCE/Data Structures HW/Data-Structures/singly_linked_list/singly_linked_list.py

# import sys
# sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

class LinkedListStack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return len(self.size)

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1


    def pop(self): #remove last one
        if self.storage != []:
            return self.storage.remove_head
        else:
            return None
