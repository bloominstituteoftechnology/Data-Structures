from linked_list import LinkedList


"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass. 
   #check

3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        ## array is the underlying data structure
        self.storage = []

    def __len__(self):
        return (len(self.storage))
       #pass

    def push(self, value):
        return self.storage.append(value)
        #pass

    def pop(self):
        if len(self.storage) >= 1:
            return self.storage.pop()
        #pass

# 2. Re-implement the Stack class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Stack tests pass.
class Stack:
    def __init__(self):
        self.size = 0
        ## array is the underlying data structure
        self.storage = LinkedList()

    def __len__(self):
        return self.size
       #pass

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)
        
        #pass

    def pop(self):
        if self.size >= 1:
            self.size -= 1
            return self.storage.remove_tail()
        
        #pass