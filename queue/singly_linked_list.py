# a  class that represents the individual elements in our LL
class Node:
    def __init__(self,value=None, next_node=None):
        self.value=value
        self.next_node=next_node
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node
    
    def set_next_node (self,new_next):
        self.next_node=new_next

class LinkedList:
    def __init__(self):
        #what attributes do we need to create a LinkedList ?
        self.head=None
        self.tail=None
    
    def add_to_head(self,value):
        #create a new Node
        new_node=Node(value)
        if self.head is None:
           #update head and tail attributes 
           self.head=new_node
           self.tail=new_node
        else:
            #set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            #update the head attribute
            self.head=new_node



    
    def add_to_tail(self,value):
        #1. create a node from the value 
        new_node=Node(value)
        # Whats the rule we want to set to indicate that the linked list is empty?
        # wouldn't it be better to check the head ? 

        #case1: consider the LL being empty 

        if self.head is None:
            #update the head and tail attributes
            self.head=new_node
            self.tail=new_node
        #case2 : consider the LL not being empty 
        else:
          
            self.tail.set_next_node(new_node)
            #reassign self.tail to refer to the new node 
            self.tail=new_node

    def remove_head(self):
         # case1: empty list
        if self.head is None:
            return None
         #  return the value of the old head
        else:
            old_head=self.head.get_value()
            if self.head==self.tail:
                self.head==None
                self.tail==None
            else:
                self.head=self.head.get_next_node()
                return old_head

    def remove_tail(self):
        # if we have an emoty list we dont have to remove anything 
        if self.head is None :
            return None
        #else return value of the old head
        else:
            ret_value=self.tail.get_value()

        #if we have a list with one element 
        if self.head==self.tail:
           self.head=None
           self.tail=None

        #list with two elements 
        else:
             # if current.next node is not the tail 
             # assign current to current.next.. then you set it to None making that the new tail 
             # return the current value

            cur_node=self.head
            while cur_node.get_next_node()is not self.tail:
                cur_node=cur_node.get_next_node()
        # keep going 
        #update pointer of temp node (prev_tail)None 
            cur_node.set_next_node(None)
            self.tail=cur_node
        #return value 
        return ret_value

    def contains(self,value):
        cur_node=self.head
        while cur_node is not None:
            # if value exists
            if cur_node.get_value()==value:
                return True
        
        return False






        

