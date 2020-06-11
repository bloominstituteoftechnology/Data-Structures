"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
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
        new_node = ListNode(value)
        self.length += 1
        # if there is an empty list then we need to set the head and tail
        # equal to the new node.
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # since appending to the front...the previous head becomes the new heads next node.
            new_node.next = self.head
            # the previous heads previous node will now point to the new node.
            self.head.prev = new_node
            # the new head is equal to the new node. 
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # self.length -= 1
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        # if there is an empty list then we need to set the head an tail
        # equal to the new node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # since appending to the back(tail)...the new node previous node is equal to the previous tail.
            new_node.prev = self.tail
            # the previous tail next node now must point to the new node
            self.tail.next = new_node
            # the tail now becomes the new node. 
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # why does this not work?? not sure why reducing the length of the list when removing
        # causes an error in the test. I dont believe the self.length attribute is correct
        # without reducing the length. 
        # self.length -= 1
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.tail and not self.head:
            return
        self.length -= 1
        if self.tail == self.head:
            self.tail = None
            self.head = None
        # if the self.tail is equal to the node we want to delete. Than we will set
        # the tail node equal to the nodes previous node. 
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        # if the self.head is equal to the node we want to delete. Than we will set
        # the head node equal to the nodes next node. 
        elif self.head is node:
            self.head = node.next
            node.delete()
        # if the node that we want to delet is not the head or the tail, then the delete
        # method in ListNode takes care of the setting of previous and next nodes. 
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current = self.head
        max_value = current.value
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

