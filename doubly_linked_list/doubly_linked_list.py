"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev
            
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
        self.add_node_to_head(ListNode(value))

    def add_node_to_head(self, node):
        self.length += 1
        node.set_prev(None)
        node.set_next(self.head)
        if self.head:
            self.head.set_prev(node)
        else:
            # the list is currently empty
            self.tail = node
        self.head = node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            # the is already empty
            return None

        self.length -= 1
        removed_value = self.head.get_value()
        self.head = self.head.get_next()
        if self.head:
            self.head.set_prev(None)
        else:
            # the list is now empty
            self.tail = None
            return removed_value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.add_node_to_tail(ListNode(value))

    def add_node_to_tail(self, node):
        self.length += 1
        node.set_prev(self.tail)
        node.set_next(None)
        if self.tail:
            self.tail.set_next(node)
        else:
            # the list is currently empty
            self.head = node
        self.tail = node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.head:
            # the list is already empty
            return None

        self.length -= 1
        removed_value = self.tail.get_value()
        self.tail = self.tail.get_prev()
        if self.tail:
            self.tail.set_next(None)
        else:
            # the list is now empty
            self.head = None
        return removed_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is not self.head:
            self.delete(node)
            self.add_node_to_head(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is not self.tail:
            self.delete(node)
            self.add_node_to_tail(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
        else:
            self.length -= 1
            prev_node = node.get_prev()
            next_node = node.get_next()
            prev_node.set_next(next_node)
            next_node.set_prev(prev_node)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None

        curr = self.head
        max_value = curr.get_value()
        while curr != None:
            max_value = max(max_value, curr.get_value())
            curr = curr.get_next()
        return max_value