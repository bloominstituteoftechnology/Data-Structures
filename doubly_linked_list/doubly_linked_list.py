"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, nextl=None):
       self.value = value
       self.prev = prev
       self.next = nextl 
    
    def __str__(self):
        return f"{self.value}"


    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        #create a new node from value
        new_node = ListNode(value)
        #create a reference for node's next node
        old_next = self.next
        #change the next pointer of node to point to new_node
        self.next = new_node
        #new_node nextl will point to node's next 
        new_node.next = old_next
        new_node.prev = self
        #change next's old to point to new node if is not None
        if old_next is not None: 
            old_next.prev = new_node

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        #create a new node
        new_node = ListNode(value)
        #create reference to node that came before node
        old_prev = self.prev
        #new node will become the value of self.prev
        self.prev = new_node
        #the previous node will become the new node's previous
        new_node.next = self
        #if previous node is not none
        if old_prev is not None: 
            new_node.prev = old_prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        #prev.next will equal to next node
        self.prev.next = self.next
        #next.prev will equal to prev node 
        self.next.prev = self.prev
        #prev = none
        self.prev = None
        #next = none
        self.nextl = None
        del self

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        if self.head is None: 
            self.length = 0 
        else: 
            self.length = 1

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        #if head is none, this means that both the tail and head are none. we will have to make the new node the head and tail
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        
        else: 
            #new node's next will point to old head 
            new_node.next = self.head
            #old head prev will point to new node 
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #case 1: there is no head so we need to return None
        if self.head is None: 
            return None  
        #case 2: there is only one node, so we need to remove both head and tail, length = 0
        if self.length == 1: 
            current_head = self.head
            self.head = None
            self.tail = None
            self.length = 0 
            return current_head.value
        #case 3: there is more than one node , so we need to make self.head = self.head.next, self.head.next.prev = none, self.length -= 1
        if self.length > 1: 
            current_head = self.head
            self.head = current_head.next
            self.head.prev = None
            self.length -= 1
            return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        #create a new node for value
        new_node = ListNode(value)
        if self.tail is None: 
            self.tail = new_node
            self.head = new_node
         
        else: 
            #create a reference to current tail 
            current_tail = self.tail 
            #current_tail.next points to new node 
            current_tail.next = new_node
            new_node.prev = current_tail
            #new node becomes self.tail
            self.tail = new_node
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        pass
        if self.length == 0: 
            return None
        
        elif self.length == 1:
            old_tail = self.tail 
            self.head = None
            self.tail = None
            self.length = 0
            return old_tail.value
            
        else: 
            old_tail = self.tail
            self.tail.prev.next = self.tail.next 
            self.tail = self.tail.prev
            old_tail.prev = None
            return old_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # TODO: Catch errors if list is empty or node is not in list
        # For now assumine node is in list
        pass

    """Returns the highest value currently in the list"""
    def get_max(self):
        # Loop through all nodes, looking for biggest value
        # TODO: Error checking
        pass





