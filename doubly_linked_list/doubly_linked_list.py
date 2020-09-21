"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node

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
        # create new_node
        new_node = ListNode(value)
        # 1. add to empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 2. add to nonempty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # update length
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # empty list
        if self.head is None and self.tail is None:
            return None
        else: 
            # store head value before removal
            value = self.head.value
            #  with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.length = 0
                return value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.length -= 1
            return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        # empty list
        if self.head is None and self.tail is None:
            # set new_node to head and tail
            self.head = new_node
            self.tail = new_node
        else: 
            # have the current tail's 'next' pointing to the new node
            self.tail.next = new_node
            # then set the new node to now be the tail
            self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.length -= 1
        # empty list
        if self.head is None and self.tail is None:
            return
        else: 
            # store tail value before removal
            value = self.tail.value
            # 1 element
        if self.tail == self.head:
            self.tail = None
            self.head = None
            self.length = 0
            return value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.length -= 1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # 1. delete()
        if node is self.head:
            return
        self.delete(node)
        # 2. add_to_head()
        self.add_to_head(node.value)


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
        node.delete()
        self.length -= 1
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # don't need to return value
        # DO need to update head and tail
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head: # list has +2 nodes
            self.head = node.next
            node.delete() # updating prev and/or next pointers
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
        # empty list
        if not self.head:
            return
        # start with the head as the current value
        current = self.head
        # the current node is the max, for now
        max = current.value
        # while we can continue to iterate
        while current:
            # if the current node is greater than the max
            if current.value > max:
                # then this node becomes the new maximum!
                max = current.value
            # go to the next value (if it's None, the loop will end)
            current = current.next
        # once all values have been checked, return the max value
        return max
