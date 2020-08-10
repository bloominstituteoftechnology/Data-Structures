from singly_linked_list import LinkedList

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

############################### 1 #################################
# This implementation of a stack passes all test_stack scenarios and 
# uses an empty array as the underlying storage structure

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size += -1
#             return self.storage.pop()



# This version of the Stack Class implements an underlying storage type of 
# Single Linked List and it passes all tests.
################################ 2 ######################################
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            x = self.storage.tail.get_value()
            self.storage.remove_tail() 
            self.size += -1
            return x


############################# 3 ######################################
#3. What is the difference between using an array vs. a linked list when 
#   implementing a Stack?




# This is similar to the difference when implementing a Queue. The main difference 
# between how arrays and linked lists work is that we have to iterate into our linked 
# lists in order to retrieve the values desired. In the case of stacks, we want to iterate
# through the linked list until we reach the tail, at which point we can remove that value.
# Arrays bypass this by utilizing Python indexing. In the case of a stack, the python
# method '.pop()' automatically removes the last element of a data structure if no index 
# position is strictly declared. This would be equal to finding the tail of a linked list. 
















