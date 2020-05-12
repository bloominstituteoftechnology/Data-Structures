
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
        self.size = 0               # keeping track of the size of the linklist
        self.storage = LinkedList() # assigned a list 

    def __len__(self):     #returning the length of your list 
        return self.size
        # return len(self.storage)

    def push(self, value):  # adding a node to the head of link list 
        self.storage.add_to_head(value) #passing thru a value to the list that creates a node and assigns it to the head of the list 
        self.size = self.size +1 #this adds one to the size of the list
        # return self.storage.append(value)

    def pop(self):
        if self.size > 0: 
            self.size = self.size -1 #subtracting one from the size of the current list
        return self.storage.remove_from_head() #a method that removes a node from the current linked list.
       
    #    if not self.storage:
    #        return None
    #    else:
    #        return self.storage.pop()class Node:

class Node: # points to the next node or node has value or a pointer 
      def __init__(self, value=None, next_node=None):
          self.value = value
          self.next_node = next_node
          
      def get_value(self): #a method that returns the value of the node
          return self.value
    
      def get_next(self): # a method that returns the next node in the linked list.
          return self.next_node

      def set_next(self, new_next): # a method that sets the next_node to a different node
          self.next_node = new_next # creating a new node 

class LinkedList: 
    def __init__(self):
        self.head = None # This is the head of your linked list with a value of none.

    def remove_from_head(self): # a method that removes the current head and assigns it node next in line. 
        if not self.head: # if there is no head return a value of none
            return None
        else: 
            value = self.head.get_value() # using the method get_value that is on the Node to assign it to a value. 
            self.head = self.head.get_next() # using the method get_next to find the next Node in the linked list
            return value #returns the value that was set by line 60
            
    def add_to_head(self, value): # a method to add a node to the head of the linked list
        node = Node(value) # creating a new node using the value that is passed through. 
        node.next_node = self.head #setting the new node that was created to point to the current head
        self.head = node #setting the new node as the current head. 
      
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size
#         # return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#         self.size = self.size +1
#         # return self.storage.append(value)

#     def pop(self):
#         if self.size > 0:
#             self.size = self.size -1
#             return self.storage.pop()
#         else:
#             return None
#     #    if not self.storage:
#     #        return None
#     #    else:
#     #        return self.storage.pop()class Node:

