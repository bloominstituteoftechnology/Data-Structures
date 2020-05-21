import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

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
# Array
# class Stack:
#     def __init__(self, arr = []):
#         self.size = 0
#         self.arr = arr
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.arr.append(value)
#         self.size += 1
#
#     def pop(self):
#         if self.size == 0:
#             print('There is nothing here.')
#             return
#         else:
#             self.size -= 1
#             return self.arr.pop(-1)

#Linked List
class Stack:
    def __init__(self, storage = None):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            print('There is nothing here')
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()
