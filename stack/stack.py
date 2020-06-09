import sys
# sys.path.append("doubly_linked_list")
# from doubly_linked_list import DoublyLinkedList

sys.path.append('src/singly_linked_list/singly_linked_list.py')
from singly_linked_list import LinkedList
# #Array
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
#         if self.storage != []:
#             self.size -= 1
#             return self.storage.pop()
#         else:
    
# Linked List
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()