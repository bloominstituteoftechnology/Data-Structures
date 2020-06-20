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

#Linked List Implementation
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
    def __init__(self):
        # Array Implementation
        # self.storage = []

        # Linked List Implementation
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        # Array Implementation
        # return len(self.storage)

        # Linked List Implementation
        # Start at the head and add one to the count until you reach the tail (.next is None)
        return self.size

    def push(self, value):
        # Array Implementation
        # self.storage.append(value)

        # Linked List Implementation
        new_node = Node(value)
        # If the list is empty, set the head node and it's .next value to be the value
        if self.head is None:
            self.head = new_node
            # self.head.next = new_node
            self.tail = new_node
        # Otherwise, if there are nodes, change the current tail's .next value from None to the value
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def pop(self):
        # Array Implementation
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     value = self.storage.pop()
        #     return value
        
        # Linked List Implementation
        if self.head is None:
            return None
        elif self.head.next is None:
            removed = self.head
            self.head = None
            self.size -= 1
            return removed.data
        else:
            new_last = self.head
            # While there is at least two elements after the current Node, keep moving through the loop since it isn't the next to last Node
            while new_last.next.next:
                new_last = new_last.next

            removed = new_last.next
            new_last.next = None
            self.size -= 1
            return removed.data
