"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

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

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.is_empty():
            return None

        old_head = self.head

        if old_head.get_next() is None:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.get_next()
            self.head.prev = None
        self.length -= 1

        return old_head.get_value()
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.is_empty():
            return None

        old_tail = self.tail

        if old_tail.get_prev() is None:
            self.head = None
            self.tail = None
        else:
            self.tail = old_tail.get_prev()
            self.head.next = None
        self.length -= 1

        return old_tail.get_value()
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.is_empty():
            return
        current = self.head

        while current is not None:
            if current == node:
                if current.prev is not None:
                    current.prev.next = current.get_next()
                if current.next is not None:
                    current.next.prev = current.get_prev()

                current.next = self.head
                current.prev = None
                self.head = current
                return
            else:
                current = current.get_next()
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.is_empty():
            return
        current = self.head

        while current is not None:
            if current is node:
                if current.prev is not None:
                    current.prev.next = current.get_next()
                if current.next is not None:
                    current.next.prev = current.get_prev()

                if current is self.head:
                    self.head = current.get_next()
                    self.head.prev = None

                current.next = None
                current.prev = self.tail
                self.tail = current

                if self.head.get_next() is None:
                    self.head.next = self.tail
                return
            else:
                current = current.get_next()

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.is_empty():
            return

        if self.head is self.tail:
            self.head = None
            self.tail = None

        current = self.head

        while current is not None:
            if current is node:
                if current.prev is not None:
                    current.prev.next = current.get_next()
                if current.next is not None:
                    current.next.prev = current.get_prev()

                if current is self.head:
                    self.head = current.get_next()
                    self.head.prev = None

                if current is self.tail:
                    self.tail = current.get_prev()
                    self.tail.next = None

                current = None
            else:
                current.get_next()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None

        current = self.head
        max = 0

        while current is not None:
            if current.get_value() > max:
                max = current.get_value()
            current = current.get_next()

        return max