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
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
        
    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        return self.storage

    def pop(self):
        if self.size ==0:
            return None
        else:
            value = self.storage.pop()
            self.size -= 1
        return value

# Stack Using Linked list

import sys
sys.path.append('../singly_linked_list')

from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    def __len__(self):
        return self.size
    def push(self, value):
        self.storage.add_to_head(value)
        self.size +=1
        return self.storage
    def pop (self):
        if self.size == 0:
            return None
        else:
           node =  self.storage.remove_head()
           self.size -= 1
        return node


# if __name__ == '__main__':
#     Stack.main()



        




# stack = Stack()
# print(len(stack))
# print(stack.push(4))
# print(stack.push(5))
# print(stack.push(6))
# print(stack.pop())
# print(len(stack))