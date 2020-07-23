"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue? --- The popping of the element with a list is at the 
   front of the list and when using a linked_list it is at the head.  With a list elements 
   then need to be shifted down becuase the element zero was removed.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# doing the import
from data_structures.singly_linked_list.singly_linked_list import LinkedList

class Queue:
    # Implementation with a list
    #def __init__(self):
    #    self.size = 0
    #    self.storage = []
#
    # Implementation with a linked list
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    
    def __len__(self):
        return self.size

    # Implementation with a list
    #def enqueue(self, value):
    #    self.storage.append(value)
    #    # now incrementing the size 
    #    self.size += 1

    # Implementation with a linked list
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        # now incrementing the size 
        self.size += 1

        
    # Implemenation with a list        
    #def dequeue(self):
    #    # will need to pop off at the front of the list
    #    if self.size == 0:
    #        return None
    #    # decrement the size 
    #    self.size -= 1
    #    return self.storage.pop(0)

    # Implemetation with a linked list
    def dequeue(self):
        # will need to pop off at the front of the list
        if self.size == 0:
            return None
        # decrement the size 
        self.size -= 1
        return self.storage.remove_head()



if __name__ == "__main__":
    
    q = Queue()

    q.enqueue(100)
    q.enqueue(105)
    q.enqueue(110)

    r = q.dequeue()

    print("We are now printing out the r ", r)