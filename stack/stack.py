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

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        
        # and not empty?
        else:
            #now we don't need to traverse the whole list

            #set the current tail's next to the new node
            self.tail.set_next(new_node)
            #set self.tail to the new node
            self.tail = new_node

    #we can directly remove this, no traversing
    #O(1)
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

    def add_to_head(self, value):
      new_node = Node(value)

      if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node

      else:
        new_node.set_next(self.head)
        self.head = new_node

    def print_ll_elements(self):
      current = self.head

      while current is not None:
        print(current.value)
        current = current.get_next





class Stack(LinkedList):
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        self.head = None

    def __len__(self):
        return self.size

    def push(self, value):
        #add items
        self.storage.add_to_end(value)
        self.size += 1

    def pop(self):
        #remove items
        if self.storage.remove_from_tail() is not None:
            self.size -= 1
        return self.remove_from_tail()

s = Stack()

s.push('candy')
s.push('scooter')
s.push('fish')

print(s.__len__())

s.pop()
print(s.__len__())
