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

    # passed test
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    # passed test
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
# test node delete test
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

    # passed test
    def add_to_head(self, value):
        # Wraps the given value in a ListNode
        new_head = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    # passed testing
    def remove_from_head(self):
        # assign value to head
        value = self.head.value
        if not self.head:
            return
        # if there is only one node return none
        elif self.head == self.tail:
            self.head = self.tail = None
        # otherwise delete the head by 1 length
        else:
            self.delete(self.head)
        self.length -= 1
        # return what is left
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    # passed testing
    def add_to_tail(self, value):
        new_tail = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    # passed testing
    def remove_from_tail(self):
        if self.tail is None and self.head is None:
            return None
        # create temporary variable to keep track of the current tail
        temp = self.tail
        # value you want to return is reassigned
        if self.tail == self.head:
            self.delete(self.tail)
            self.length = 0
            self.tail = None
            self.head = None
        else:
            self.tail = temp.prev
            self.tail.next = self.head
            temp.delete()
            self.length -= 1
        return temp.value

    # or this?

    #   def remove_from_tail(self):
    #       new_tail = self.tail
    #       if self.tail == self.head:
    #           self.delete(self.tail)
    #           self.length = 0
    #       else:
    #           self.tail = new_tail.prev
    #           new_tail.delete()
    #           self.length -= 1
    #           return new_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    # passed testing
    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.length -= 1

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    # passed testing
    def move_to_end(self, node):
        # if the length is greater than 1 node
        if self.length > 1 and node is not self.tail:
            # insert a node as the next or tail
            self.tail.insert_after(node.value)
            self.tail = self.tail.next
        if node == self.head:
            self.head = node.next
        node.delete()

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    # passed test remove from head, line 12
    def delete(self, node):
        # if statement for if node was the head or tail
        if not self.head:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # use remove_from_head open ended
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        # use remove_from_tail open ended
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        else:
            node.delete()
        self.length -= 1
        
        """this logic returns 9 instead of 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.tail == node:
            self.remove_from_head()
        elif self.head == node:
            self.remove_from_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1"""

    """Returns the highest value currently in the list"""

    # use max_val built in function
    # passed testing
    def get_max(self):
        if not self.head and self.tail:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val

