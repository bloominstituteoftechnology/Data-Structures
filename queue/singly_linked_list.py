class Node:
    def __init__(self, value=None, next=None):
        self.value = value        
        self.next_node = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):        
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)
        
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # call set_next with the new_node on the current tail node
            self.tail.set_next(new_node)
            # update self.tail to point to the new last Node in the linked list
            self.tail = new_node

            # current = self.head
            # while current.get_next() is not None:
            #     current = current.get_next()            
            # current.set_next(new_node)

    def remove_head(self):
        if self.head is None:
            return None
        # save the head Node's data
        data = self.head.get_value()
        # both head and tail refer to the same Node
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # set both to be None 
            self.head = None
            self.tail = None
        else:
            # we have more than one Node in the linked list 
            # delete the head Node 
            # update `self.head` to refer to the Node after the Node we just deleted
            self.head = self.head.get_next()
        return data
    
    # def remove_head(self):
    #     if not self.head:
    #         return None        
    #     else:            
    #         value = self.head.get_value()
    #         self.head = self.head.get_next()
    #         return value