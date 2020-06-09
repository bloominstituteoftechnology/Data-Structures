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

Answer #3: Elements of an array don't have a built in reference to the next element in the list, while Linked List nodes do have a next property. Also, Linked Lists don't have the same helper methods as arrays.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Array version
class Queue:
    def __init__(self):
        self.content = []
    
    def __len__(self):
        return len(self.content)

    def enqueue(self, value):
        self.content.append(value)

    def dequeue(self):
        if len(self.content) > 0:
            return self.content.pop(0)

# Linked list version
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

class Queue:
    def __init__(self):
        self.length = 0
        self.content = LinkedList()
    
    def __len__(self):
        return self.length

    def enqueue(self, value):
        new_node = Node(value, None)
        if self.length == 0:
            self.content.head = new_node
            self.content.tail = new_node
        else:
            self.content.tail.next = new_node
            self.content.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.length > 0:
            popped_node = self.content.head
            self.content.head = self.content.head.next
            self.length -= 1
            return popped_node.value
