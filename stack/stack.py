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
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList, Node

########    Without the LinkedList and Node classes    ########
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def __len__(self):
#         return len(self.stack)

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if len(self.stack) == 0:
#             return None
#         else:
#             return self.stack.pop()


########    With the LinkedList and Node classes    ########

# class Stack:
#     _number_of_nodes = 0 # length

#     def __init__(self):
#         self.my_stack = LinkedList()
        
#     def __len__(self):
#         return Stack._number_of_nodes

#     def push(self, value):
#         self.my_stack.add_to_tail(value)
#         Stack._number_of_nodes += 1

#     def pop(self):
#         self.my_stack.remove_tail()
#         Stack._number_of_nodes -= 1

"""
The tests are written in a way where I'm supposed to be storing the stack in a list to access length???
I thought a class variable to track the number of instances that gets incremented when push and pop are called would work just as well...
So far the computer science curriculum has been very underwhelming and disappointing. WAY too much starter code. forces me into a compliance
mindset rather than a learning one. To make matters worse the material thus far has been so poorly taught that I'd be better of using other
resources and not attending lecture at all...
"""