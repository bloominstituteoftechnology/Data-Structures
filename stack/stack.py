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
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1
#
#     def pop(self):
#         if self.size > 0:
#             value = self.storage.pop()
#             self.size -= 1
#             return value
#         return None

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = None

    def __len__(self):
        return self.size

    def push(self, value):
        tail = Node(value)
        if self.size == 0:
            self.storage = tail
            self.size += 1
        else:
            self.__append(self.storage, tail)
            self.size += 1


    def pop(self):
        node = self.storage.next
        if self.size == 0:
            return None
        elif self.size == 1 and self.storage.next == None:
            node = self.storage
            self.storage = None
            self.size -= 1
            return node
        else:
            node = self.__remove(node)
            self.size -= 1
            return node

    def __remove(self, node):
        parent = node
        tail = parent.next

        while tail.next:
            parent = tail
            tail = parent.next
         parent.next = None
        return tail


    def __append(self, head, tail):
        node = head.next
        if not node:
            node = tail
        else:
            self.__append(node, tail)

class Node:
    def __init__(self, value, node = None):
        self.next = node
        self.value = value
