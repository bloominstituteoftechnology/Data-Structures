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
            current = self.head #the current node is self.head
            while current.next_node: #while there is a next node
                current.next_node = new_node #the current next node is the new node
            self.tail = new_node #after exiting while loop, we know there is no next_node,
            #therefore self.tail is the new_node
        return self.tail


    def remove_head(self): 
        


    def contains(self, value): 
        current = self.head #current node is self.head
        next_node = current.get_next()
        while current: #while node exists:
            if current.get_value() == value: #if get.value() == value
                return True
            current = next_node #go to the next node
        return False

    def get_max(self): #get max value in entire list
        pass

