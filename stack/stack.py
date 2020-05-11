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
"""
#first pass
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        #add items
        self.storage.insert(0, value)
        self.size += 1

    def pop(self):
        #remove items
        self.size -= 1
        return self.storage.pop(0)

s = Stack()

s.push('candy')
s.push('scooter')
s.push('fish')
print(s.storage)
print(s.size)

s.pop()
print(s.size)
print(s.storage)
"""

#second pass 
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, value):
        # what if the list is empty?
        # -- value is the actual value, not wrapped by node
        # -- wrap it in node and make it first in our list

        new_node = Node(value) # we should do this regardless if empty

        if not self.head:
            self.head = new_node
            return self.head
    
        # and not empty?
        else:
            #we want to get to the last node in the list
            #but we need to traverse the list to get there

            current = self.head

            while current.get_next() is not None:
                #as long as we haven't reached the end of the list, keep going through it
                current = current.get_next()
                #we are now at the end of the list

            return current.set_next(new_node) #now we can add the new node to the list

    def remove_from_head(self):
        #what if the list is empty?
        # -- nothing to remove

        if not self.head:
            return None
        #what if the list isn't empty?
        else:
            #we want to return value at current head
            #also want to remove the value
            #and update self.head

            value = self.head.get_value()

            self.head = self.head.get_next()

            return value

    def remove_from_tail(self):

        if not self.head:
            return None

        else:
            current = self.head

            while current.get_next() is not None:
                #as long as we haven't reached the end of the list, keep going through it
                current = current.get_next()
                #we are now at the end of the list
            current = None
            return current #now we can remove the last item 




class Stack(LinkedList):
    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        return self.size

    def push(self, value):
        #add items
        self.add_to_end(value)
        self.size += 1

    def pop(self):
        #remove items
        if self.remove_from_head() is not None:
            self.size -= 1
        return self.remove_from_head()

s = Stack()

s.push('candy')
s.push('scooter')
s.push('fish')

print(s.__len__())

s.pop()
print(s.__len__())
