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

Answer #3: Elements of an array don't have a built in reference to the next element in the list, while Linked List nodes do have a next property. Also, Linked Lists don't have the same helper methods as arrays.
"""

# Array version
class Stack:
    def __init__(self):
        self.content = []

    def __len__(self):
        return len(self.content)

    def push(self, value):
        self.content.insert(0,value)

    def pop(self):
        if len(self.content) > 0:
            return self.content.pop(0)
        else:
            return None

# Linked List data structure version
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

class Stack:
    def __init__(self):
        self.length = 0
        self.content = LinkedList()

    def __len__(self):
        return self.length

    def push(self, data):
        new_node = Node(data, self.content.head)
        self.content.head = new_node
        self.length += 1
        if self.length == 1:
            self.content.tail == self.content.head

    def pop(self):
        if self.length > 0:
            popped = self.content.head
            self.content.head = self.content.head.next
            self.length -= 1

            if self.length == 0:
                self.content.tail == None
                self.content.head == None
                
            return popped.value
