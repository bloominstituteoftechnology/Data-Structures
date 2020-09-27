class Node: 
    def __init__(self, value, next_node=None):
        # the value that the node is holding
        self.value = value
        # reference to the next node in the linked list
        self.next_node = next_node

        
    def get_value(self):
        """
        Method to get the value of a node
        """
        return self.value

    def get_next(self):
        """
        Method to get the node's "next_node"
        """
        return self.next_node

    def set_next(self, new_next):
        """
        Method to update the node's "next_node" to the new_next
        """
        self.next_node = new_next


class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        #wrap the value in a new Node
        new_node = Node(value)
        #check if the linked list is empty
        if self.head is None and self.tail is None:
            #set the head and tail to the new node
            self.head = new_node
            self.tail = new_node

            #otherwise the list must have at least one item in there
        else:
            #update the last node's "next_node" to the new node
            self.tail.set_next(new_node)#(last node in the chain).next_node = new_node
            #update the self.tail to the point to the new node that we just added
            self.tail = new_node

    def remove_tail(self):
        #remove the last node in the chain and return its value
        #check for empty list
        if self.head is None and self.tail is None:
            #return none
            return None 

        #check if there is only one node
        if self.head == self.tail:
            #store the value of the node that we are going to remove
            value = self.head.get_value()
            #remove the node
            #set the head and the tail to None
            self.head = None
            self.tail = None
            # return the stored value
            return value

            #otherwise the link list has more than one node
        else: 
            #store the value of the node that we are going to remove
            value = self.tail.get_value()
            # we need to set the "self.tail" to the second to last node 
            # we can only do this by traversing the whole list from beginning to end

            #starting from the head, we'll traverse down to the second to last node
            #init another reference to keep track of where we are in the linked
            #list as we're iterating.
            current_node = self.head
            
            # keep iterating until the node after "current_node" is the tail
            while current_node.get_next() != self.tail:
                #keep looping
                current_node = current_node.get_next()

            #at the end of the iteration set "self.tail" to the current_node
            self.tail = current_node
            #set the new tail's "next_node" to None
            self.tail.set_next(None)
            #return the value
            return value

    def remove_head(self):
        #check for empty list
        if self.head is None and self.tail is None:
            #return none
            return None
        #check if there is only one linked list node
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else: 
            #store the old head's value that we need to return
            val = self.head.get_value()
            # set `self.head` to the old head's `next_node`
            self.head = self.head.get_next()
            # return the old_head's value
            return val







