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

   singly linked lists are not symmetric, so the choice between add-to-head/remove-from-tail
   and add-to-tail/remove-from-head has performance consequences.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

         use two stacks. instantiate by putting all elements into stack one.
         to get the last element, iteratively pop off elements from stack one and 
         push onto stack two. once done, pop the first element off of stack two.
         to then push more elements into the queue, iteratively pop elements from stack two
         and push onto stack one, then push on new elements.
"""

from singly_linked_list import LinkedList
from stack import Stack

# double stack version
class Queue:

    def __init__(self):
        self.size = 0
        self.storage1 = Stack()
        self.storage2 = Stack()
    

    def __len__(self):
        return self.storage1.size + self.storage2.size


    def enqueue(self, value):

        # if second storage has any elements, move them to the first
        if self.storage2.size > 0:
            while self.storage2.size > 0:
                val = self.storage2.pop()
                self.storage1.push(val)

        self.storage1.push(value)


    def dequeue(self):

        if ((self.storage1.size == 0) and (self.storage2.size == 0)):
            return None

        # move elements over to second storage and pop off the first
        else:
            while self.storage1.size > 0:
                val = self.storage1.pop()
                self.storage2.push(val)

            # then pop off the first element.
            return self.storage2.pop()




"""# singly-linked-list version
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):

        if self.size <= 0:
            return None

        else:
            self.size -= 1
            return self.storage.remove_head()"""



"""# array version
class Queue:
    def __init__(self):

        self.size = 0
        self.storage = []
    
    def __len__(self):

        return len(self.storage)

    def enqueue(self, value):

        self.storage.append(value)
        self.size += 1

    def dequeue(self):

        if self.size <= 0:
            return None

        else:
            self.size -= 1
            return self.storage.pop(0)"""
