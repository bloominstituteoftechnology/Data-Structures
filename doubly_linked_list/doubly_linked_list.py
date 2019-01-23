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
        if self.head is None:
            self.head = ListNode(value)
            self.tail = ListNode(value)
        else:
            to_add = ListNode(value)
            to_add.next = self.head
            self.head.prev = to_add
            self.head = to_add

    def remove_from_head(self):
        if self.head is not None:
            v = self.head.value
            n = self.head.next
            self.head = n
            if self.head is None:
                self.tail = None
            return v
        else:
            return self.head

    def add_to_tail(self, value):
        new_node = ListNode(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        if self.head is None and self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail = new_node

    def remove_from_tail(self):
        node_to_remove = self.tail
        previous_node = self.tail.prev
        previous_node.next = None
        self.tail = previous_node
        return node_to_remove.value

    def move_to_front(self, node):
        node.delete()
        self.add_to_head(node.value)

    def move_to_end(self, node):
        node.delete()
        self.add_to_tail(node.value)

    def delete(self, node):
        # Just swapping the two
        next_node = node.next
        previous_node = node.prev
        previous_node.next = next_node
        next_node.prev = previous_node

    def get_max(self):
        pass
