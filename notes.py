class Node:  # Nodes don't use indexing; you have to jump through each node until you get to the desired one.
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
      
    def set_next(self, new_next):
        self.next_node = new_next
        
    def set_value(self, value):
        self.value = value   
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
      
    def add_to_tail(self, value):
        #  wrap the value in a node
        new_node = Node(value)
        #  check if we're in an empty list state
        if not self.head and not self.tail:
            #  set the list's head reference to point to new_node
            self.head = new_node
            #  set the list's tail reference to point to new_node
            self.tail = new_node
        else:
            #  update the old tail's next reference to refer to the new code
            self.tail.set_next(new_node)  
            #  update the LinkedList's 'tail' reference
            self.tail = new_node
        
        
        