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
    Wrap the given value in a ListNode and insert it before this node.
    Note that this node could already have a previous node it is pointing to.
    """    
        
    def insert_before(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    
    """
    Wrap the given value in a ListNode and insert it after this node.
    Note that this node could already have a previous node it is pointing to.
    """
    
    def insert_after(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
            
    """
    Rearranges this ListNode's previous and next pointers 
    accordingly, effectively deleting this ListNode.
    """        
            
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
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
        new_node = ListNode(value, none, none)
        # If list is currently empty
        self.length += 1
        if self.head is None and self.tail is None:
            # Set the head and tail to equal the new node
            self.head = new_node
            self.tail = new_node
        else:
            # the list already has elements in it
            # make new node's next value point to current head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        head_value = self.head.value
        self.delete(self.head)
        return head_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value
    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_head(old_value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_tail(old_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if empty list, do nothing
        if self.head is None and self.tail is None:
            return
        # the list is only one node
        self.length -+ 1
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        # the node is the HEAD node (so make sure we handle the head pointer correctly
        elif self.head == node:
            self.head = node.prev
            node.delete()
        # the node is the TAIL node (make sure tail is handled correctly)
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        # the node is just some node in the list
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass