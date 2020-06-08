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

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#         return self.storage

#     def pop(self):
#         if self.__len__() is 0:
#             return None
#         else:
#             return self.storage.pop()

class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node
        
    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        if self.size < 0:
            self.size = 0
        return self.size

    def push(self, value):
        self.size += 1
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
            # print(current.value, "inside push")

    def pop(self):
        print(self.size, "WHAT is the head")
        self.size -= 1
        if not self.head:
            return None
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value


# b = Node()


# i = Stack()

# i.push(1), i.__len__()
# i.push(2), i.__len__()
# i.push(34), i.__len__()
# print(i.pop(), i.__len__())
# print(i.pop(), i.__len__())
# print(i.pop(), i.__len__())