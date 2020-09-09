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


# array ran ok
# linkedlist test ran ok
# had to place this module into queue folder also

# difference is the syntax and you use the methods from the class creation to implement it

from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        # self.storage = []
        self.storage = LinkedList()
        

    def __len__(self):
        #return len(self.storage)
        return self.size
        

    def push(self, value):
        # return self.storage.append(value)
        self.storage.add_to_tail(value)
        self.size += 1


    def pop(self):
        #if self.storage == []:
            #return None
       # else:
           # return self.storage.pop()
        if self.size != 0:
            self.size -=1
        return self.storage.remove_tail()


