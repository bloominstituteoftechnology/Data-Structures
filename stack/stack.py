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
   -- Array has accessible info by index, and can be accessed; and has memory allocated in the stack section. Linked List points to the next node, so it is less accessible; and memory of a linked list gets allocated in the heap section. 
"""

'''
Stack class with array storage structure.
'''

# class Stack:
#     def __init__(self):
#         self.container = []
#         # self.storage = ?
        
#     def is_empty(self):
#         return not self

#     def __len__(self):
#         return len(self.container)

    # def push(self, value):
    #     self.container.append(value)

    # def pop(self):
    #     if len(self.container) < 1:
    #         return None
    #     else:
    #         return self.container.pop()
    
    # def show(self):
    #     return self.container
    
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.pop())
# print(s.show())


'''
Stack class with list storage structure.
'''

class Stack:
    class Node:
        def __init__(self, element, _next):
            self.element = element
            self._next = _next
            
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return not self
    
    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            result = self.head.element
            self.head = self.head._next
            self.size -= 1
            return result
    
    def top(self):
        if self.is_empty():
            return None
        return self.head.element
            
            
s = Stack()
s.push(1)
s.push('two')
s.push(3)
s.push('four')
print(s.top())


# return all values in the list a -> b -> c -> d -> none
def __str__(self):
    output = ''
    current_node = self.head # create tracker node variable
    while current_node is not None: # loop until it's None
        
        output += f'{current_node.value} -> ' # (Custom syntax for specific list)
        
        current_node = current_node.next_node # update tracker node to the next node