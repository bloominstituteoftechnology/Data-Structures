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

"""
#first pass 
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        #removes items from queue
        self.size -= 1
        return self.storage.pop()

q = Queue()

print(q.__len__())
q.enqueue('puppies')
q.enqueue('apples')
q.enqueue('soccer ball')

print(q.__len__())
print(q.storage)

q.dequeue()
print(q.storage)

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


class Queue(LinkedList):
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        #adds items to queue
        self.size += 1
        self.storage.add_to_end(value)

    def dequeue(self):
        #removes items from queue
        if not self.storage.head:
            return None

        self.size -= 1
        return self.storage.remove_from_head()

q = Queue()

print(q.__len__())
q.enqueue('puppies')
q.enqueue('apples')
q.enqueue('soccer ball')

print(q.__len__())
q.dequeue()
print(q.__len__())