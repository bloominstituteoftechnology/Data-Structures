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

    def add_to_head(self, value):
        node_to_add = ListNode(value)
        if self.head is None:
            self.head = node_to_add
        elif self.head is not None:
            current_head = self.head.value
            self.head = node_to_add
            self.head.insert_after(current_head)

    def remove_from_head(self):
        current_head = self.head
        self.head.delete()
        return current_head.value

    def add_to_tail(self, value):
        list_node = ListNode(value)
        if self.tail is None:
            self.tail = list_node
        else:
            prev_tail = self.tail
            self.tail = list_node
            self.tail.prev = prev_tail
            self.tail.insert_before(self.tail.value)

    def remove_from_tail(self):
        current_tail = self.tail
        self.tail.delete()
        return current_tail.value

    def move_to_front(self, node):
        if self.head is not None:
            prev_head = self.head.value
            self.head = node
            self.head.insert_after(prev_head)

    def move_to_end(self, node):
        if self.tail is not None:
            prev_tail = self.tail.value
            self.tail = node
            self.tail.insert_before(prev_tail)

    def delete(self, node):
        pass

    def get_max(self):
        current_max = 0
        current_node = self.head

        while current_node is not None:
            if current_node.value > current_max:
                current_max = current_node.value
            current_node = current_node.next
        return current_max if current_max > 0 else None