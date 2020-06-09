
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

# Working with ARRAY
class Stack:
    def __init__(self, storage = []):
        self.size = 0
        self.storage = storage
    def __str__(self):
        return f'{self.storage}'
    def __len__(self):
        return self.size
    def push(self, value):
        self.size += 1
        self.storage.append(value)
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()
testarr = []
test = Stack(testarr)
test.push(1)
test.push(2)
print(test.pop())
print(test)
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.data = LinkedList()
    def __str__(self):
        return f'{self.data}'
    def __len__(self):
        return self.size
    def push(self, value):
        self.data.add_to_tail(value)
        self.size += 1
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.data.remove_from_tail()
            
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self,data):
        new_node = Node(data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_from_tail(self):
        if self.tail is None:
            return None
        data = self.tail.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else: 
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
        return data
    
    def remove_from_head(self):
        if self.head is None:
            return None
        data = self.head.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        return data

'''
#testarray = []
test = Stack()
test.push(1)
test.push(2)
test.push(3)
print('test pop is', test.pop())
'''