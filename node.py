class Node:
    def __init__(self, value=None, next_node=None): # prev_node=None
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
        #DLL
        # self.prev_node = prev_node
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next): 
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference to the head of the list (if head == None, LL empty)
        self.head = None
        # reference to the tail of the list 
        self.tail = None 

    def add_to_head(self, value):
        # create new Node with value 
        new_node = Node(value)
        # update pointer of new Node -> 'head'
        new_node.set_next(self.head)

        # inserting into empty LL
        if self.head is None:
            # mark new Node as 'head' & tail
            self.head = new_node
            self.tail = new_node

        # inserting into LL with +1 Nodes 
        else:
            # mark new Node as 'head'
            self.head = new_node
    
    def add_to_tail(self, value):
        # create new Node with value 
        new_node = Node(value)

        # inserting into empty LL
        if self.tail is None:
            # mark new Node as 'head' and 'tail'
            self.head = new_node
            self.tail = new_node

        # inserting into LL with +1 Nodes
        else: 
            self.tail = new_node
            # update next pointer of old 'tail'
            self.tail.set_next(new_node) # <-- ! Moved from original line! 
    
    def remove_head(self):
        # remove from empty LL
        if self.head is None:
            return
        
        # remove from LL with 1 element 
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        # general 
        else: 
            # new head = old head's next Node 
            self.head = self.head.get_next()