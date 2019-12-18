"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None, key=None):
        self.value = value
        self.prev = prev
        self.next = next
        self.key = key

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
        new_node = ListNode(value, None, None)
        self.length += 1
        # first node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # new node prev will be None so it does not need to be changed
        # new node next will be old head
        # old head prev will be new node
        # LL head reference changed to new node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        node = self.head
        self.delete(self.head)
        return node

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # first node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # new node next will be None so it does not need to be changed
        # new node prev will be the old tail
        # old tail next will be new node
        # LL tail reference changed to new node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        node = self.tail
        self.delete(self.tail)
        return node

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
        self.length -= 1
        # if trying to delete when no nodes exist
        if not self.head and not self.tail:
            # TODO: shouldn't happen, but handle anyway
            return
        # single node case
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # if deleting head
        # get the next node reference from node being deleted
        # change head reference to next node
        # delete node
        elif self.head is node:
            self.head = node.next
            node.delete()
        # if deleting tail
        # get the prev node reference from node being deleted
        # change tail reference to prev node
        # delete node
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        # no node case
        # -?
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # start at head
        current = self.head
        # get value
        max_value = current.value
        # iterate through the nodes via their next reference
        # compare max and current, keep track of max
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value


node = ListNode(1)
dll = DoublyLinkedList(node)
print(dll)
print(dll.length)
dll.add_to_head(5)
print(dll.length)
dll.add_to_tail(10)
print(dll.length)
