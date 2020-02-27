"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev  # pointers
        self.next = next  # if we only have next, then it's single linked

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    # Inserts are just changing the pointers
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

    def __len__(self):     # built in method, this is way for them to access it
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)       #
        self.length += 1                                  # increase the length
        # when adding to the head, we have to pass in base cases to see if the list is empty
        if not self.head and not self.tail:
            self.head = new_node         #
            self.tail = new_node         #
        else:
            new_node.next = self.head     # the old head is pushed to next
            self.head.prev = new_node     # the new_node that we defined becomes the head
            self.head = new_node          # and then, we make the head equals to new node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value


    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length +=1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # have to get the value first and delete the value
        # delete re-arranges the pointer and we get the return value
        value = self.tail.value
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
        # get the value
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):      # this is for the node
        self.length -= 1      # decriment the length the first
        # think of special cases
        if not self.head and not self.tail:
            return
        # if head and tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # if there is only one item in the list i.e. selfhead == self.tail
        # so we change it to None

        # if head
        elif self.head == node:
            # first we need to update the pointer
            self.head = self.head.next
            node.delete()  # we use the delete function described above

        # if tail
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()

        # otherwise like empty?

        else:
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        # compare values
        if not self.head:
            return None

        max_value = self.head.value
        current = self.head.next     # here is where we start
        while current: # if we have something in current
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
