"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""    
    
    def add_to_head(self, value): # the new node becomes the head of our list 
        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev  
            self.length += 1
        else:
            self.__init__(node=ListNode(value))

    # def add_to_head(self,value):
    #     new_node = ListNode(value, None, None)
    #     self.length += 1
    #     if not self.head and not self.tail:
    #         self.head = new_node
    #         self.tail = new_node
    #     else: 
    #         new_node.next = self.head  #set the new node's next to the current head 
    #         self.head.prev = new_node #reassign head to point to the new node 
    #         self.head = new_node



    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    
    def remove_from_head(self):
        if self.head:
            if self.head.next is None:
                self.tail = None
            current_head = self.head.value
            self.head =self.head.next
            self.length -= 1
            return current_head
        else:
            return None

    # def remove_from_head(self):
    #     value = self.head.value
    #     self.delete(self.head)
    #     return value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    
    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1
        else:
            self.__init__(node=ListNode(value))

    # def add_to_head(self,value):
    #     new_node = ListNode(value, None, None)
    #     self.length -= 1
    #     if not self.head and not self.tail:
    #         self.head = new_node
    #         self.tail = new_node
    #     else: 
    #         new_node.prev = self.tail
    #         self.tail.next = new_node
    #         self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    
    def remove_from_tail(self):
        if self.tail:
            if self.tail.prev is None:
                self.head = None
            current_tail = self.tail.value
            self.tail =self.tail.prev
            self.length -= 1
            return current_tail
        else:
            return None

    # def remove_from_tail(self):
    #     value = self.tail.value
    #     self.delete(self.tail)
    #     return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    
    def move_to_front(self, node): #check if the node is the head 
        current_node = node
        node.delete()
        self.length -= 1
        self.add_to_head(current_node.value) # stores a reference to the node we are going to move 

    # def move_to_front(self, node):
    #     if node is self.head:
    #         return None
    #         value = node
    #     if node is self.tail:
    #         self.remove_from_tail()
    #     else:
    #         node.delete()
    #         self.length -=1
    #         self.add_to_head(value)

    

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    
    def move_to_end(self, node): #check if the node is the head 
        current_node = node
        if current_node.prev is None:
            self.head = current_node.next
        node.delete()
        self.length -= 1
        self.add_to_tail(current_node.value) #stores a reference to the node we are going to move 
    
    # def move_to_front(self, node):
    #     if node is self.tail:
    #         return None
    #         value = node
    #     if node is self.head:
    #         self.remove_from_head()
    #     else:
    #         node.delete()
    #         self.length -=1
    #         self.add_to_tail(value)


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    
    def delete(self, node): # store incoming node in variable 
        current_node = node
        if node.prev is None and node.next is None: # this node is the only one on the list 
            self.head = None # removing the value pointing its value to none 
            self.tail = None # removing the value pointing its value to none 
            self.length -= 1 
            return node.value # this value would be deleted/ no longer connected to the list 

        elif node.prev is None: # this checks if the incoming node is deleted from the head 
            self.head = node.next 
            node.delete()
            self.length -= 1 
            return node.value

        elif node.next is None: # this checks if the incoming node is deleted from the tail 
            self.tail = node.prev
            node.delete()
            self.length -=1
            return node.value

        else: 
            node.delete() # removes nodes that are in between the head and tail of the list 
            self.length -= 1
            return node.value
        
        # def delete(self, node):
        #     if not self.head and not self.tail:
        #         return None
        #     self.length -=1
        #     if self.head is self.tail:
        #         self.head = None
        #         self.tail = None
        #     #check if the node is the head 
        #     elif self.head is node:
        #         self.head = node.next
        #         node.delete()
        #     #otherwise, there's no additional reference we need to update 
        #     else:
        #         node.delete()


        
    """Returns the highest value currently in the list"""
    
    def get_max(self): #looping through all nodes looking for the biggest value 
        if not self.head:
            return None

        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val

    # def get_max(self): # init a variable that will keep track of the largest element we have seen so far 
    #     current_max = self.head.value
    #     current = self.head.next
    #     while current is not None:
    #         if current.value > current_max:
    #             current_max = current.value
    #         current = current.next
    #     return current_max


