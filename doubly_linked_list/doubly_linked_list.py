"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        # When initializing, both prev and next point to None
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create a new node
        new_node = ListNode(value, None, None)
        # increment the length
        self.length += 1
        # if the DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # if the DLL is not empty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # Get the value
        value = self.head.value
        # delete the node
        self.delete(self.head)
        return value
        
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # create a new node
        new_node = ListNode(value, None, None)
        # increment the length of DLL
        self.length += 1
        # if DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # Get the value
        value = self.tail.value
        # delete the node
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # get the value
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # if list is empty
        if not self.head and not self.tail:
            return None
        # if 1 node
        if self.head==self.tail:
            self.head = self.tail = None
        # if the node is the head
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        # if the node is the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        # if the node is somewhere in the middle
        else:
            node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        max_value = self.head.value
        current_node = self.head

        # walk through the entire list
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
