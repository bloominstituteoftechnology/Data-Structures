"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        pass
            
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
        # turn value into an object of ListNode
        new_node = ListNode(value)
        # increase length by 1
        self.length += 1

        # check to see if there is already a head (if DLL is empty)
        if not self.head:
            # point the head and the tail attribute to it
            self.head = new_node
            self.tail = new_node
        # if there is already a head:
        else: 
            # set the new node's next to the current head
            new_node.next = self.head
            # set the current head's prev to new node
            self.head.prev = new_node
            # assign head to the new node
            self.head = new_node
        return (f"Added {self.head} to the head")
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of head
        current_head = self.head
        # Check to see if there is a head. if not, return None.  
        if not current_head:
            return None
        self.length -= 1
    
        # if head.next is None
        if not self.head.next:
            self.head = None
            self.tail = None
        # if head.next is Not None
        # AKA: we have more than one item in the linked list
        else:
            # set head.next's prev to None
            self.head.next.prev = None
            # set head to head.next
            self.head = self.head.next
        # return value
        return current_head
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # wrap input value in a ListNode
        new_node = ListNode(value)
        # increment DLL length attribute
        self.length += 1

        # if DLL is empty
        if not self.head:
            # set head and tail to new node instance
            self.head = new_node
            self.tail = new_node    
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            # set tail to new node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if DLL.head is None: 
        if not self.head:
            return None
        # decrement length
        self.length -= 1
        # get current tail
        current_tail = self.tail
        
        # checkt to see if there are multiple items in DLL
        if not self.tail.prev:
            self.head = None
            self.tail = None
            return current_tail
        else:
            # set current tail prev to None
            self.tail.prev.next = None
            # set current tail prev to tail
            self.tail = self.tail.prev
            return current_tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass