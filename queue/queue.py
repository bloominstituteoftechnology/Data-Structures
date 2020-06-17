"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
#Linked List Implementation
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Queue:
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
        return self.size

    def enqueue(self, value):
        # Array Implementation
        # self.storage.append(value)

        # Linked List Implementation
        new_node = Node(value)
        # If the list is empty, set the head node and its .next value to be the value
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.tail = new_node
        # Otherwise, if there are nodes, change the current tail's .next value from None to the value
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def dequeue(self):
        # Array Implementation
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     removed = self.storage.pop(0)
        #     return removed

        # Linked List Implementation
        if self.head is None:
            return None
        elif self.head.next is None:
            removed = self.head
            self.head = None
            self.size = 0
            return removed.data
        else:
            removed = self.head
            self.head = self.head.next
            self.size -= 1
            return removed.data
