"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node: #represents a single node
    def __init__(self, value=None, next_node=None): 
        #value and next_node   
        #value is the data and next_node is the address to that points to next_node

        self.value = value #linked list value that's stored inside node
        self.next_node = next_node #next node in linked list. if no other node in list then it will point to None.

    def get_value(self): #gets value of node
        return self.value

    def get_next(self): #gets value of next_node
        return self.next_node

    def set_next(self, new_next): #sets next_node to new_next
        self.next_node = new_next

class LinkedList(): #properties are head and tail
    def __init__(self, head = None):
        '''
        create singly-linked list
        Takes O(1) time because we are just assigning stuff
        '''
        self.head = None
        self.tail = None
        

    def add_to_tail(self, value):   #this is OK
        
        '''
        replaces the tail with a new value that is passed on
        Takes O(n) time because it depends on the amount of input is linear.
        
        '''
        new_node = Node(value) #new instance of node class
        if not self.head: #if the list is empty:
            self.head = new_node  #self.head and self.tail is assigned as the new node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            
        return self.tail


    def remove_head(self): 
        if not self.head: #if no items in list
            return None
        #if head has no next
        if not self.head.next_node:
            #take a reference to curr head
            head = self.head
            #delete the list's head reference
            self.head = None
            # also make sure the tail points to None
            self.tail = None
            return head.value
        else:
            # we have multiple elements in our list
            value = self.head.value
            self.head = self.head.next_node
            return value
        


    def contains(self, value): 
        #check to see if list is empty:
        if not self.head:
            return None
        
        current = self.head #current node is self.head
        while current: #while node exists:
            if current.value == value: #if get.value() == value
                return True
            current = current.next_node #go to the next node
        #if we get here, we've not found the value so return false
        return False

    def get_max(self): #get max value in entire list
        if not self.head: # if no items in list:
            return None
        max_value = self.head.value #max_value is self.head.value for now
        current = self.head.get_next()
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.get_next()
        return max_value

