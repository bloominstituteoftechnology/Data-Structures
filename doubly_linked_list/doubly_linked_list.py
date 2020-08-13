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
        if self.length == 0:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            node = ListNode(value, next=self.head)
            self.head.prev = node
            self.head = node
        self.length += 1
       
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        
        retval = self.head.value
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None 
        else:
            #Length is 1
            self.head = None
            self.tail = None
        self.length -= 1
        return retval
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.length == 0:
            node = ListNode(value)
            self.tail = node
            self.head = node
        else:
            node = ListNode(value, prev=self.tail)
            self.tail.next = node
            self.tail = node
        self.length += 1 
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        
        retval = self.tail.value
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            #Length is 1
            self.head = None
            self.tail = None
        self.length -= 1
        return retval
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            self.head = node
            self.tail = node
        elif node is self.head:
            pass
        elif node is self.tail:
            self.tail = node.prev
            self.tail.next = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            node.delete()
            node.next = self.head
            self.head.prev = node
            self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 0:
            self.head = node
            self.tail = node
        elif node is self.head:
            self.head = node.next
            self.head.prev = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        elif node is self.tail:
            pass
        else:
            node.delete()
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return
        
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None and self.tail is None:
            return
        
        max_value = self.head.value
        current = self.head.next
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            
            current = current.next
        return max_value