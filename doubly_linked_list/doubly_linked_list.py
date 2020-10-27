"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

        # None <= 0 =>  <= 1 => <= 2 => <= None
        # 0 <= 1 => <= 2 => <= None
        # 1 <= 2 => <= None
        # 2 <= None
            
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

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        self.head.next = self.head
        self.head = new_node
        self.length += 1

        #[ 15 , 0, 1, 2, 3, 4, None]
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            self.length -= 1

        self.head = self.head.next
        self.length -= 1

        #[None, 0, 1, 2, 3, 4, None]
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1

        cursor = self.head
        while cursor.next.next is None:
            cursor = cursor.next

        cursor.next = None
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length > 1:
            # checks if the node is the current tail
            if self.tail == node:
                self.tail = node.prev
                self.tail.next = None

                self.head.next = self.head
                self.head = node

            else:
                self.head.next = self.head
                self.head = node

        
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