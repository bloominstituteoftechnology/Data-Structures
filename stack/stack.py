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

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.storage:
            return self.storage.pop()
        return None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        """ Counts the number of nodes in the linked list iteratively.
        """
        temp_value = self.head
        count = 0
        while(temp_value):
            count +=1
            temp_value = temp_value.next
        return count
    
    def __iter__(self):
        """Makes linked liste iterable
        """
        node = llist.head
        while node:
            yield node
            node = node.next

    def push(self, value):
        """ Inserts a new node at the beginning of the linked list
        """
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """ Returns the data of the node at the front of the linked list
        and removes the node. It returns None if there are no nodes.
        """
        if self.head is None:
            return None
        else:
            popped = self.head.value
            self.head = self.head.next
            return popped
