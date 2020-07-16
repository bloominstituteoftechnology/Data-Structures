"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.prev_node = prev_node
        self.value = value
        self.next_node = next_node

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, new_prev):
        self.prev_node = new_prev
            
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
        new_node = ListNode(value=value)
        new_node.set_next(self.head)
        self.head = new_node
        self.head.prev_node = None
        self.length += 1

        if self.length == 1:
            self.tail = self.head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        temp = self.head

        if self.length > 1:
            self.head = self.head.next_node
            self.head.prev_node = None
            self.length -= 1

            if self.length == 0:
                self.tail = None

            return temp.value

        else:
            self.head = None
            self.tail = None
            self.length -= 1

            return temp.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, data):
        new_node = ListNode(value=data)
        current = self.head

        if self.length == 0:
            self.head = new_node
            self.tail = self.head

        else:
            while current.next_node is not None:
                current = current.next_node
            current.set_prev(current)
            current.set_next(new_node)
            self.tail = new_node

        self.tail.next_node = None
        if current:
            self.tail.prev_node = current.prev_node
        else:
            self.tail.prev_node = None
        self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        temp = self.tail

        if self.length > 1:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            self.length -= 1

            if self.length == 0:
                self.tail = None

            return temp.value

        else:
            self.head = None
            self.tail = None
            self.length -= 1

            return temp.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head
        if current is not None:
            if current == node:
                pass
            else:
                node.set_next(current)
                node.set_prev(None)
                self.head = node

                if self.length == 1:
                    self.tail = self.head
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current = self.head
        if node == self.head:
            current = node.next_node
            self.head = node.next_node
            pass
        else:
            pass
        while current.next_node is not None:
            current = current.next_node
        self.tail = node
        node.set_next(None)
        node.set_prev(current)
        current.set_prev(current)
        current.set_next(node)

        if self.length == 1:
            self.head = self.tail


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        if current is None or node is None:
            return
        if node == self.head:
            self.head = node.next_node
        if node == self.tail:
            self.tail = node.prev_node
        while node != current:
            current = current.next_node
        if current == node:
            if node.next_node:
                node.next_node.prev_node = node.prev_node
            if node.prev_node:
                node.prev_node.next_node = node.next_node

        self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self, start=None):
        if start:
            current = start
        else:
            current = self.head
        try:
            if current.next_node is not None:
                return max(current.value, self.get_max(start=current.next_node))
            elif current.next_node is None:
                return current.value
        except AttributeError:
            return None

    def search(self, value, start=False):
        if self.head is None:
            return None
        if start is False:
            current = self.head
        else:
            current = start
        while value not in current.value:
            current = current.next_node
            return current
