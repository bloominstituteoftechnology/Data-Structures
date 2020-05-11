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


class Queue(LinkedList):
    def __init__(self):
        self.size = 0
        self.head = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        #adds items to queue
        self.add_to_end(value)
        self.size += 1

    def dequeue(self):
        #removes items from queue
        if self.remove_from_head() is not None:
            self.size -= 1
        return self.remove_from_head()

q = Queue()

print(q.__len__())
q.enqueue('puppies')
q.enqueue('apples')
q.enqueue('soccer ball')

print(q.__len__())
q.dequeue()
print(q.__len__())
