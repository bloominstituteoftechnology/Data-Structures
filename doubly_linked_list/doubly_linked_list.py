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
        current_head = self.head
        #   If head exists
        if self.head:
            self.head = ListNode(value, None, current_head)
            current_head.prev = self.head
        #   If head does not exist then tail does not exist. Must assign new node to head AND tail.
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #   If head exists
        if self.head:
            current_head = self.head
            #   If there is only one node both head and tail should be None
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                self.head.delete()
                self.head = current_head.next
                self.length -= 1

            return current_head.value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #   If tail exists
        if self.tail:
            newNode = ListNode(value, self.tail)
            self.tail.next = newNode
            self.tail = newNode
            #   Tail does not exist then head does not exist
        else:
            self.tail = ListNode(value)
            self.head = self.tail
        self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
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