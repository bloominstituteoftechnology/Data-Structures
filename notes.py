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
        #  STEP 1: Wrap the value in a node
        new_node = Node(value)
        #  STEP 2: Check if we're in an empty list state
        if not self.head and not self.tail:
            #  STEP 3: Set the list's head reference to point to new_node
            self.head = new_node
            #  STEP 4: Set the list's tail reference to point to new_node
            self.tail = new_node
        else:
            #  STEP 3a: Update the old tail's next reference to refer to the new code
            self.tail.set_next(new_node)  
            #  STEP 4a: Update the LinkedList's 'tail' reference
            self.tail = new_node
            
    def remove_head(self):
        #  What if our list is empty?
        if not self.head and not self.tail:
            return None
        #  What if our list only contained a single node?
        #  if not self.head.get_next():
        if self.head is self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.get_value()
        #  store a reference to the node we're removing
        old_head = self.head
        #  update the head reference to refer to the old head's next node
        self.head = old_head.get_next()
        #  return the old head's value
        return old_head.get_value()
        #  delete the old head  <== you don't have to do this because Python cleans this up for you
        
        
        