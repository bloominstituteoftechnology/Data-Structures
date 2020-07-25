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

    Assumptions - 
        A) We are implement a stack with a linked list, not extending the 
        the linked list by inheritance.
        B) We are doing this with true OOP principles, ie Abstraction 
        and encapsulation

    With those assumptions, we need to improve our linked list class and add
    functionality to surface features like counting. Python fundamentally 
    operates on a "We are all consenting adults" mentality, and I can easily 
    reach into my linked list and implement a count at the Stack object.  But 
    that would effectively violate the concepts of abstraction and 
    encapsulation. Alternatively I could inherit the capabilities of my linked 
    list, and add new methods, but that would be extension/inheritance, not 
    implementation.

    So this is the justification for modifying my linked list class to add more
    functionality that can be surfaced, while still being abstracted and 
    encapsulated.

    I feel this is the best "form" even though it might not be 100% pythonic
    aka "we are all consenting adults here"  It is more expedient to just reach
    into my linked list class, and modify it how ever I want.

"""

from singly_linked_list import LinkedList

class ArrayStack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        '''
        Returns the number of elements in the stack
        '''
        return len(self.storage)

    def push(self, value):
        '''
        Adds a value to the top of the stack
        '''
        self.storage.insert(0, value)

    def pop(self):
        '''
        removes and returns the element at the top of the stack
        '''
        if not self.storage:
            return None

        return self.storage.pop(0)
    
class Stack:
    '''
    A stack implemented with a linked list
    '''
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        '''
        Returns the number of elements in the stack
        '''
        return self.size

    def push(self, value):
        '''
        Adds a value to the top of the stack
        '''
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        '''
        removes and returns the element at the top of the stack
        '''
        if self.size == 0:
            return None

        self.size -= 1
        return self.storage.remove_head()
