class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        pass

    def insert_before(self, value):
        pass

    def delete(self):
        pass

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
    
    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        if self.head is None:
            self.head = ListNode(value) #if there is no head 
            self.tail = ListNode(value) #go ahead and set the list up
        else:
          new_node = ListNode(value) #create the node. 
          new_node.set_next(self.head) # going in front of head so current head next.
          self.head.set_prev(new_node) # new_node will come before head so setting prev.
          self.head = new_node #making the head change

    def remove_from_head(self):
        node_to_remove = self
        if self.head == None:
            return self.head
        else:
            returning = self.head.get_value()
            self.head = self.head.get_next()
            if self.head is None:
                self.tail = None
            return returning
            # get previous on head isn't needed because this isn't set
            # up in a circular setting it was then if head was removed  previous
            # would be the tail so a connect with the new head and tail would have to be made.
            # because it is not a circle connection all other connections should be set.

    def add_to_tail(self, value):
        new_node = ListNode(value)  # create the node.
        new_node.set_prev(self.tail)  # came before so prev has to be set up.
        self.tail.set_next(new_node)  # set self.tail next to new node.
        # new node doesn't have a new next because it is now the tail.
        if self.head is None and self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail = new_node

    def remove_from_tail(self):
        node_to_remove = self
        previous_node = self.tail.get_prev()
        previous_node.set_next(None)# cutting the link off from the current tail.
        self.tail = previous_node  # making the change. 
        

    def move_to_front(self, node):
        current_head = self.head # grab the current head
        traveling_node_next = node.get_next()
        traveling_node_prev = node.get_prev()
        #What this is doing is allowing for a new connection to be set up
        #I can then connect these to nodes together to keep the chain. 
        # 1  2   3 
        # we are grabing 2   
        # 1   3  
        # we now need 1 and 3 to be connected. 
        traveling_node_prev.set_next(traveling_node_next) #1>>3next
        traveling_node_next.set_prev(traveling_node_prev) # 1<<3previous
        #connected   1 >><<3 
        #now set the node up to the front. 
        self.head = node 
        node.set_next(current_head) # connect so  1 2 3 4 5 take 4 
        # we already connected 3 and 5 on lines 90 and 91. 
        # now take the 4 and connect it 4 >> to 1(what was the head)
        current_head.set_prev(node)
        #now connect   what was the head to the new head   4 <<< 1 


    def move_to_end(self, node):
        pass

    def delete(self, node):
        """ just have to link out the node
        take the connect of the node and connect
        so left connection and right connection just needs to be 
        connected. 
        """
        pass
