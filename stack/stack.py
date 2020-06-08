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


from doubly_linked_list import DoublyLinkedList
class Stack:
    def __init__(self):
        self.size = 0

        self.storage = DoublyLinkedList()
        

    def __len__(self):
        return self.size
    # So here adding an element to the top of the stock
    def push(self, value):
        # if self.size == 0:
        self.size += 1
        self.storage.add_to_tail(value)
        # else:
            # self.size +=1 
            # self.storage.add_to_tail(value)

            
    # Here removing the element from the stack
    def pop(self):
        if self.size == 0: # if the size is null return None
            return None
        elif self.size == 1: # if the size is equalts to a number then remove from the head
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            self.size -= 1 #remove from them tail.
            return self.storage.remove_from_tail()
        
           

    


