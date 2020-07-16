"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
"""

"""
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
"""
# class Stack:
#      def __init__(self):
#          self.values = []
#      def __len__(self):
#          return len(self.values)
#      def push(self, value):
#          self.values.append(value)
#      def pop(self):
#          if self.__len__() == 0:
#              return None
#          else:
#              return self.values.pop()
#      def peek(self):
#          return self.valuess[len(self.values)-1]

"""
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
"""
from singly_linked_list.singly_linked_list import Node, LinkedList

class Stack:  
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        self.head = None
        self.tail = None
    # Checks if stack is empty 
    def is_empty(self): 
        if self.head == None: 
            return True
        else: 
            return False
    # Method to add data to the stack 
    # adds to the start of the stack 
    def push(self, value):
      self.storage.add_to_tail(value)
      self.size += 1
    # Remove element that is the current head (start of the stack) 
    def pop(self):  
        if self.__len__()<1: 
            return None
        else:
          self.size -=1 
          return self.storage.remove_tail()
    def __len__(self):
        return self.size

# arr = Stack()
# print(arr.__len__())
# # arr.push(12)
# arr.push(1)
# print(arr.__len__())
# arr.push(17)
# arr.push(23)
# print(arr.__len__())
# print(arr)
# arr.pop()
# print(arr.__len__())
# print(arr)

"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
