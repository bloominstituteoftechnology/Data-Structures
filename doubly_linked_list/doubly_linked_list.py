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
        new_node = ListNode(value, None, self.head)

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
        self.tail = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            self.tail = None
            return None

        if self.head.next is None:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed.value

        removed = self.head
        self.head = self.head.next
        self.head.prev -= 1
        return removed.vale
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.head = new_node
            self.length += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current
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
            self.tail = None
            # return None

        if self.head.next is None:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed.value

        current = self.head
        while current.next is not None:
            current = current.next

        current.prev.next = None
        self.length -= 1
        return current.value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return

        value = node.value
        current = self.head

        while current.next is not None:
            if current.value == value:
                break
            current = current.next

        if current.next is None:
            current.prev.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        
        value = node.value
        current = self.head

        while current.next is not None:
            if current.value == value:
                break
            current = current.next
        
        if current.next is None:
            current.prev.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

        self.add_to_tail(value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1

        if self.head is None and self.tail is None:
            return None
        
        if self.head is self.tail:
            self.head = None
            self.tail = None

        elif self.head is node:
            self.head = node.next
            node.delete()

        elif self.tail is node:
            self.tail = node.prev
            # node.delete()

        else:
            node.delete()


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None and self.tail is None:
            return None

        if self.head.next is None:
            return self.head.value

        max_value = self.head.value
        current = self.head.next

        while current:
            if current.value > max_value:
                max_value = current.value

            current = current.next

        return max_value