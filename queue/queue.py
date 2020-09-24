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

# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value=value
#         self.next_node=next_node

#     def get_value(self):
#         return self.value
    
#     def get_next_node(self):
#         return self.next_node

#     def set_next_node(self,next_new):
#         self.next_node=next_new

 
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
    
#     def add_to_head(self,value):
#         #create a new Node
#         new_node=Node(value)
#         if self.head is None:
#             #update the head and tail attributes 
#             self.head=new_node
#             self.tail=new_node
#         else:
#             #set the next node of the new node to the head 
#             new_node.set_next_node(self.head)
#             #update the head attribute
#             self.head=new_node

#     def add_to_tail(self,value):
#         #create a new node
#         new_node=Node(value)
#         # if the linked list is empty (case 1)
#         if self.head is None:
#             #update the head and tail attributes 
#             self.head=new_node
#             self.tail=new_node
#         # the linked list is not empty (case 2)
#         else:
#             #update the next node of the tail 
#             self.tail.set_next_node(new_node)
#             #update self.tail
#             self.tail=new_node
    
#     def remove_head(self):
#         # if it is an empty list (case1)
#         if self.head is None:
#             return None 
#         # else return the old value of the head 
#         else:
#             ret_value=self.head.get_value()
#             #list with one element 
#             if self.head ==self.tail:
#                 self.head =None
#                 self.tail=None
#             else:
#                 self.head=self.head.get_next_node()
#                 return ret_value
    
#     def remove_tail(self):
#         # if it is an empty list 
#         if self.head is None:
#             return None
#         else:
#             ret_value=self.tail.get_value()
#             #list with one element 
#             if self.head ==self.tail:
#                 self.head =None
#                 self.tail=None
#             # if the list has more than 2 elements 
#             else:
#                 #if the next node is not the tail 
#                 # assign the current_node to the next 
#                 # set the current node to None by doing so the current node becomes the new tail 
#                 current_node =self.head
#                 while current_node.next_node is not self.tail:
#                     current_node=current_node.next_node
#                     current_node.set_next_node(None)
#                     self.tail=current_node
#                 return ret_value


from singly_linked_list import LinkedList
    
    


class Queue:
    def __init__(self):
        self.size = 0
        self.storage=LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size +=1
        return self.storage

    def dequeue(self):
        if self.size >=1:
           value=self.storage.remove_head()
           self.size -=1
           return value
        
