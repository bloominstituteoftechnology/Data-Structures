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
            node = ListNode(value)
            self.tail = node
            self.head = node
        else:
            current_node = self.head
            current_node.insert_before(value)
            self.head = current_node.prev

    def remove_from_head(self):
        current_node = self.head
        self.head = current_node.next
        current_node.delete()
        return current_node.value

    def add_to_tail(self, value):
        if self.head is None:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            current_tail = self.tail
            current_tail.insert_after(value)
            self.tail = current_tail.next

    def remove_from_tail(self):
        current_node = self.tail
        self.tail = current_node.prev
        current_node.delete()
        return current_node.value

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        node.delete()
        return node

    def get_max(self):
        if self.head is None:
            return None
        curr_node = self.head
        maxNode = -float("inf")
        if curr_node is None:
            return None
        while curr_node is not None:
            if curr_node.value > maxNode:
                maxNode = curr_node.value
            curr_node = curr_node.next
        return maxNode


node = ListNode(1)
d = DoublyLinkedList(node)
d.add_to_tail(100)
d.add_to_tail(55)
d.add_to_tail(101)

print(d.get_max())
