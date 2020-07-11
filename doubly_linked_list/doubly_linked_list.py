"""Each Node holds a reference to its previous node
as well as its next node in the List."""


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def get_value(self):
        return self.value

    """Wrap the given value in a Node and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = Node(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a Node and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = Node(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this Node's previous and next pointers
    accordingly, effectively deleting this Node."""

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

    """Wraps the given value in a Node and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        self.length += 1
        new_node = Node(value)
        # is there is no head or no tail
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # is there is a head
        else:
            current_node = self.head
            current_node.prev = new_node
            new_node.next = current_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # check for head
        if self.head is None:
            return None
        # if there is only one head
        if self.head.next == None:
            head = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return head.get_value()
        else:
            new_head_node = self.head.next
            new_head_node.prev = None
            self.head = new_head_node
            self.length -= 1
            return new_head_node

    """Wraps the given value in a Node and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = Node(value)
        # check for head
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            current_node = self.tail
            current_node.next = new_node
            new_node.prev = current_node
            self.tail = new_node
            self.length += 1
            return new_node.get_value()

    def remove_from_tail(self):
        # if there is nothing
        if self.head is None and self.tail is None:
            return None
        # if there is one Node
        if self.head is self.tail:
            head = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return head.get_value()
        # if there is more than one Node
        else:
            last_node = self.tail
            new_last_node = last_node.prev
            self.tail = new_last_node
            new_last_node.next = None
            self.length -= 1
            return new_last_node.get_value()

    def move_to_front(self, node):
        pass
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        pass

    """Returns the highest value currently in the list"""

    def get_max(self):
        # if there is nothing
        if self.head is None and self.tail is None:
            return None
        max_value = self.head.get_value()
        current_node = self.head.next
        while current_node:
            if current_node.get_value() > max_value:
                max_value = current_node.get_value()
            current_node = current_node.next
        return max_value
