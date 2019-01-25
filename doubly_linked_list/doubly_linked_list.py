"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value, key=None):
        # the current next that will be shifted down after insertion
        current_next = self.next
        # adds current_next to next value and self to prev during init
        self.next = ListNode(key, value, self, current_next)
        if current_next:
            current_next.prev = self.next
        return self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value, key=None):
        current_prev = self.prev
        self.prev = ListNode(key, value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev

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
        self.max = node

    # O(1)
    def add_to_head(self, value, key=None):
        # O(1)
        if self.head:
            new_head = self.head.insert_before(value)
            self.head = new_head
            self.max = new_head if new_head.value > self.max.value else self.max
        # O(1)
        else:
            new_node = ListNode(key, value)
            self.head = new_node
            self.tail = new_node
            self.max = new_node

    # O(1)
    def remove_from_head(self):
        if self.head:
            old_head = self.head
            old_head.delete()
            self.head = old_head.next
            return old_head.key, old_head.value

    # O(1)
    def add_to_tail(self, value, key=None):
        # O(1)
        if self.tail:
            new_tail = self.tail.insert_after(value, key)
            self.tail = new_tail
            self.max = new_tail if new_tail.value > self.max.value else self.max
        # O(1)
        else:
            new_node = ListNode(key, value)
            self.tail = new_node
            self.head = new_node
            self.max = new_node
        return self.tail

    # O(1)
    def remove_from_tail(self):
        if self.tail:
            old_tail = self.tail
            old_tail.delete()
            self.tail = old_tail.prev
            return old_tail.key, old_tail.value

    # O(1)
    def move_to_front(self, node):
        node.delete()
        self.add_to_head(node.value)

    # O(1)
    def move_to_end(self, node):
        if self.head == node:
            self.head = node.next
        node.delete()
        return self.add_to_tail(node.value, node.key)

    # O(1)
    def delete(self, node):
        node.delete()

    # O(1)
    def get_max(self):
        return self.max.value
