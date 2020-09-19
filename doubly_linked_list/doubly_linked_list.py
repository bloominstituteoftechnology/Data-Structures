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
        if self.prev:
            self.next.prev = self.prev
        if self.next:
            self.prev.next = self.next
            
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
        new_node = ListNode(value)
        # add to empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # add to non empty list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
 
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # an empty list
        if self.head is None:
            return None
        # a list of one element
        elif self.head is self.tail:
            current_val = self.head     # saves current head to return later
            self.delete(self.head)      # deletes current head
            self.add_to_head(self.tail) # sets tail to head
            self.length = 0
            return current_val.value
        # a list of 2+ elements
        else:
            current_node = self.head          # saves current head to return later
            temp_node = self.head.next        # saves node after head for assigment
            self.head = temp_node             # adds node after previous head
            self.length -= 1                  # updates the length
            return current_val.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.tail == None: # empty list
            self.head = new_node
            self.tail = new_node
        elif self.tail == self.head: # single item list
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail == None:
            return None
        elif self.tail == self.head:
            current = self.tail
            self.delete(self.tail)
            self.length = 0
            return current.value
        else:
            current = self.tail
            self.delete(self.tail)
            self.length -= 1
            return current.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return node
        self.delete(node)
        self.add_to_head(node.value)
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Don't need to return value
        # DO need to update head and tail
        if self.head is None:
            return None
        elif self.head is self.tail: # list with one
            self.head = None
            self.tail = None
        elif node is self.head: # list with two+ values and removing the head
            self.head = node.next
            node.delete()
        elif node is self.tail: # list with 2+ values and removing the tail
            self.tail = node.prev
            node.delete()
        else: # list with 2+ values and removing from somewhere in the middle
            node.delete()
        self.length -= 1
            
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = self.head
        temp = self.head.next

        while temp.value != None:
            if temp.value > max.value:
                max = temp
        return max