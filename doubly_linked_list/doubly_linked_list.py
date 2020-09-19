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
    Deletes the node from the DLL so we don't have to repeat
    code.
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
       new_node = ListNode(value)
       self.length += 1 
       if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
       else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        else:
            value = self.head.value
            self.head.delete()
            if self.head is self.tail:
                self.head = self.head.next
                self.tail = self.tail.prev
            else:
                self.head = self.head.next
            self.length -= 1
            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
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
        if not self.head and not self.tail:
            return None
        else:
            value = self.tail.value
            self.tail.delete()
            if self.tail is self.head:
                self.head = self.head.next
                self.tail = self.tail.prev
            else:
                self.tail = self.tail.prev
            self.length -= 1
            return value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
         node.delete()
         self.length -= 1
         if node is self.head:
            self.head = self.head.next
         if node is self.tail:
            self.tail = self.tail.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head and not self.tail:
            return None
        current = self.head
        max_val = self.head.value
        while current:
            if max_val < current.value:
                max_val = current.value
            else:
                current = current.next
        return max_val