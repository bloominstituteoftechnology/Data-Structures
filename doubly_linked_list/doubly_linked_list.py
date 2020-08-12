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
     and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Wraps the given value in a ListNode
        node = ListNode(value)
        self.length += 1
        # Check if the DLL is empty
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            # Set new node's next to self.head
            node.next = self.head
            # Set the head's previous pointer to the new node
            self.head.prev = node
            # Set the head to the new node
            self.head = node
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Wraps the given value in a ListNode
        node = ListNode(value)
        self.length += 1
        # Check if the DLL is empty
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            # Set new node's prev to the current tail
            node.prev = self.tail
            # Set the tail node's next pointer to the new node
            self.tail.next = node
            # Set the tail to the new node
            self.tail = node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.head.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        # Decrement length
        self.length -= 1

        # Check if the DLL is empty
        if not self.head and not self.tail:
            return
        # Check if there is only one item in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Check if the node is the head node
        elif node == self.head:
            #Set the head node to the current head node's next node
            self.head = self.head.next
            self.head = None
            self.tail = None
        # Check if the node is the tail node
        elif node == self.tail:
            # Set the tail node to the current tail node's previous node
            self.tail = self.tail.prev
            self.head = None
            self.tail = None
        else:
            self.head = None
            self.tail = None

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass