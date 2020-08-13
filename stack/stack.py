
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
   
   In a array, each element is independent and
   can be accessed using it's [index=value] .
    
   In a linked list, each node/element
      points to the next, --> [] --> [] --> node
"""
# --------------------------------------------------------------------------------------------
# add singlylinkedlist to file for testing 
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
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

 

    def remove_tail(self):
        # (2+ node) if tail == None ; return None
        # else assign value --> to tail value
        # assign tail to that "next" value
        # adjust node length
        # return value

        if self.tail is None:
            return None

        elif self.tail == self.head:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            

        else:
            value = self.tail.get_value()
            self.tail = self.tail.get_next()
            self.length -= 1
            return value
 
# create output table to test each node to try to find problem !! 


# --------------------------------------------------------------------------------------------




# class Stack:
# # 1. Implement the Stack class using an array as the underlying storage structure.
# #    Make sure the Stack tests pass.
#     def __init__(self):
#         self.size = 0
#         # data structure 
#         self.storage = []

#     def __len__(self):
#         # return  self.storage to len(self.storage)
#         return len(self.storage)

#     def push(self, value):
#         # append value to self.storage
#         self.size += 1
#         return self.storage.append(value)

#     def pop(self):
#         # check to see if self.storage >= 1:
#         #  return self.storage.pop()
#         if len(self.storage) >= 1:
#             self.size -= 1
#         return self.storage.pop()
            


class Stack:
# 2. Re-implement the Stack class, this time using the linked list implementation
#    as the underlying storage structure. Make sure the Stack tests pass.
    def __init__(self):
        self.size = 0
        # add imported LinkedList
        self.storage = LinkedList()

    def __len__(self):
        # return self.size
        return self.size
        

    def push(self, value):
        # adjust self.size =+ 1
        # func add_to_tail()
        # return self.storage.add_to_tail(value)
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # check self.size is "greater than or equal" to 1: self.size -= 1
        # func remove_tail()
        # return self.storage.remove_tail()
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()
