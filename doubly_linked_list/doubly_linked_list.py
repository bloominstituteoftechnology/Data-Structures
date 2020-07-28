"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Create a new node
        tmp_node = ListNode(value, None, None)
        # Increment the list length by 1
        self.length = self.length + 1

        # Update node references to reflect a new "head" node
        if self.head == None and self.tail == None:
            self.head = tmp_node
            self.tail = tmp_node
        else:
            tmp_node.next = self.head
            self.head.prev = tmp_node
            self.head = tmp_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # Empty list?
        if self.head == None and self.tail == None:
            # empty list -> return None
            return None

        # Have at least 1 node in our list
        ret_val = self.head.value

        # Only one node in the list?
        if self.head.next == None:
            # Only 1 node in the list -> return value and "clear" list
            self.head   = None
            self.tail   = None
            self.length = 0
            return ret_val

        # More than 1 node in list, adjust the head of the list, and return value
        self.head   = self.head.next
        self.length = self.length - 1

        return ret_val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Creat a new node
        tmp_node = ListNode(value, None, None)

        # Empty list?
        if self.head == None and self.tail == None:
            # empty list -> add the node and adjust the list's meta data
            self.head   = tmp_node
            self.tail   = tmp_node
            self.length = 1
            return

        # More than 1 node in list, adjust the tail of the list and the list's meta data
        self.tail.next  = tmp_node
        tmp_node.prev   = self.tail
        self.tail       = tmp_node
        self.length = self.length + 1

        return 
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # Empty list?
        if self.head == None and self.tail == None:
            # empty list -> make sure length is 0
            self.length = 0
            return None

        # 1 node list?
        if self.length == 1:
            # 1 node list -> remove node and update list meta data
            tmp_val = self.tail.value
            self.head   = None
            self.tail   = None
            self.length = 0
            return tmp_val

        # More than 1 node
        tmp_val         = self.tail.value
        tmp_nx2lst      = self.tail.prev
        tmp_nx2lst.next = None
        self.tail       = tmp_nx2lst
        self.length     = self.length - 1
        return tmp_val
              
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        tmp_node = node
        # Is the node already at the head?
        if tmp_node.prev == None:
            # Our node is already the head -> nothing to do
            return

        # Determine the node before the node to be moved
        tmp_b4 = tmp_node.prev
        # Is our node the last node?
        if tmp_node.next == None:
            # Our node is the tail node
            tmp_b4.next = None

        # Is our node an interior node?
        if tmp_node.next != None:
            # node is an interior node
            tmp_atr = tmp_node.next
            # connect b4 node to the after node
            tmp_b4.next  = tmp_atr
            tmp_atr.prev = tmp_b4

        # Position our node as the head
        tmp_node.next = self.head.next
        tmp_node.prev = None
        self.head     = tmp_node

        return
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        tmp_node = node
        # Is the node already at the end?
        if tmp_node.next == None:
            # Our node is already the head -> nothing to do
            return

        # Determine the node before the node to be moved
        tmp_b4 = tmp_node.prev

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Empty list?
        if self.head == None and self.tail == None:
            # empty list -> make sure length is 0
            self.length = 0
            return

        # Is our node the only node in the list?
        tmp_node = node
        if self.head = tmp_node and self.tail = tmp_node:
            # Our node is the only element in the list -> remove it
            self.length = 0
            self.head   = None
            self.tail   = None
            return

        # Is the node the first element in the list?
        if self.head == tmp_node:
            # Our node is the first element in a list of more than 1 nodes -> remove it
            #   and adjust the list meta data
            tmp_afr      = tmp_node.next
            self.head    = tmp_afr
            tmp_afr.prev = None
            self.length  = self.length - 1
            return 

        # Is the node the last in the list?
        if self.tail == tmp_node:
            # Our node is the last element in a list of more than 1 nodes -> remove it
            #   and adjust the list meta data
            tmp_b4       = tmp_node.prev
            self.tail    = tmp_b4
            tmp_b4.next  = None
            self.length  = self.length - 1
            return

        # Our node is an interior element
        tmp_b4          = tmp_node.prev
        tmp_afr         = tmp_node.next
        tmp_b4.next     = tmp_afr
        tmp_afr.prev    = tmp_b4
        self.length  = self.length - 1
        return

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass