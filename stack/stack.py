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
    # the value at this linked list node
    self.value = value

    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None #first node in list
        #because we can only look at the beginning, we have to cycle through the whole list to get to the end
        self.tail = None

    #now we can directly add nodes to the list, no traversing
    #so now it is 0(1)
    def add_to_end(self, value):
        # what if the list is empty?
        # -- value is the actual value, not wrapped by node
        # -- wrap it in node and make it first in our list

        new_node = Node(value) # we should do this regardless if empty

        if not self.head:
            self.head = new_node
            self.tail = new_node

        else: #if list is not empty
            self.tail.set_next(new_node) #changes the pointer on old tail to new value
            self.tail = new_node #sets tail value to new value

    #we can directly remove this, no traversing
    #O(1)
    def remove_from_head(self):
        #what if the list is empty?
        # -- nothing to remove

        if not self.head:
            return None
        #check if head has no next value, a single-item list
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()

        #if we have a list with more than one item:
        value = self.head.get_value()
        #reset head with next value, return removed value
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None
        #if there is only one value, remove it and return it
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        #given a list longer than one:
        current = self.head

        #traverse through the list
        while current.get_next() is not self.tail:
            current = current.get_next()
        
        #once we get to the tail:
        value = self.tail.get_value()
        #set the tail to the value right before it
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False

        ## Recursive solution
        # def search(node):
        #   if node.get_value() == value:
        #     return True
        #   if not node.get_next():
        #     return False
        #   return search(node.get_next())
        # return search(self.head)  

        #traverse the list
        current = self.head
        while current:
            #check to see if value matches target value
            if current.get_value() == value:
                return True
            #regardless, update the current to the next node

        #if we are here, the target node wasn''t in the list
        return False
        
    def get_max(self):
        if not self.head:
            return None

        #to start with, max is just the first value
        max_value = self.head.get_value()
        #use current to traverse
        current = self.head.get_next()
        while current:
            if current > max_value:
                max_value = current.get_value()
            current = current.get_next()

        return max_value
        
    def add_to_head(self, value):
        #THIS IS NOT IN THE NEW STARTER CODE
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.set_next(self.head)
            self.head = new_node

    def print_ll_elements(self):
        #THIS IS NOT IN THE NEW STARTER CODE
        current = self.head

        while current is not None:
            print(current.value)
            current = current.get_next



#Commented out so I can redo from scratch

# class Stack(LinkedList):
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
#         self.head = None

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         #add items
#         self.storage.add_to_end(value)
#         self.size += 1

#     def pop(self):
#         #remove items
#         self.size -= 1
#         return self.storage.remove_from_head()

class Stack:
    def __init__(self):
        self.size = 0

    def __len__(self):
        pass
    def push(self, value):
        pass
    def pop(self):
        pass

s = Stack()

s.push('candy')
s.push('scooter')
s.push('fish')

print(s.__len__())

s.pop()
print(s.__len__())
