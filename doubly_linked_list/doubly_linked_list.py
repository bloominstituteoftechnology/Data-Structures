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
        # create a new node from the value passed in
        new_node = ListNode(value)

        # increment the length of the list by 1
        self.length += 1

        # if the head and tail are None
        # set the head and tail to the new node created
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        # else set the new node's next to the head
        # set the head's prev to the new node
        # set the head to be the new node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # grab the current value from the head
        value = self.head.value

        # call delete on the list to remove the head
        self.delete(self.head)

        # return the value grabbed from the head
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # create a new node from the value passed in
        new_node = ListNode(value)

        # increment the length of the list by 1
        self.length += 1

        # if the head and tail are None
        # set the head and tail to the new node created
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        # else set the prev node on the new node to the tail
        # set the next on the tail to the new node
        # set the tail to be the new node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # grab the current value from the tail
        value = self.tail.value

        # call delete on the list to remove the tail
        self.delete(self.tail)

        # return the value grabbed from the tail
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        # grab the value from the node passed in
        value = node.value

        # delete the node passed in from the list
        self.delete(node)

        # add node to the head of the list
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        # grab the value from the node passed in
        value = node.value

        # delete the node passed in from the list
        self.delete(node)

        # add node to the end of the list
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # set the length of the list to minus 1
        self.length -= 1

        # if there is no head or tail, return out of the function
        if not self.head and not self.tail:
            return

        # if the head and tail are the same, we only have one node
        # remove it's references and it will be deleted.
        if self.head is self.tail:
            self.head = None
            self.tail = None

        # if the list's head is the same as the node passed in
        # set the head to the next node and remove references to the head
        elif self.head is node:
            self.head = node.next
            node.delete()

        # if the list's tail is equal to the node passed in
        # set the tail equal to the previous node and remove references to the tail
        elif self.tail is node:
            self.tail = node.prev
            node.delete()

        # else the node is somewhere in the middle, remove references to the node passed in
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # if we don't have a head, return None
        if not self.head:
            return None

        # set new variable max_value equal to the current head value
        current = self.head
        max_value = current.value

        # while head is not None
        while current:
            # if the current value is greater than the current max_value
            # replace max_value with the current node's value
            if current.value > max_value:
                max_value = current.value

            # move the current node to the next in the list and re-compare
            current = current.next

        # by this time, we have the maximum value in the list so return it
        return max_value
