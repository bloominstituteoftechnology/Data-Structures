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
        # if there head is None
        if self.head is None:
            # Add a head
            self.head = ListNode(value, None, value)
            # Add a tail
            self.tail = ListNode(value, value, None)
        else:
            # store current head in next value
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        # store old head in variable
        if self.head:
            # store old head in temp variable
            removed = self.head.value
            # update head to next value
            self.head.delete()
            return removed

    def add_to_tail(self, value):
        # if there is a current tail
        if self.tail is not None:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        if self.tail:
            removed = self.tail.value
            self.tail.delete()
            return removed

    def move_to_front(self, node):
        temp = node.value
        node.delete()
        self.add_to_head(temp)
        # node.insert_before(self.head)
        # if node.prev is not None:
        #     node.prev.next = node.next
        # if node.next is not None:
        #     node.next.prev = node.prev
        # self.head.next = node
        # node.prev = None
        # node.next = self.head
        # self.head = node

    def move_to_end(self, node):
        self.add_to_tail(node.value)
        # previous.next should equal next.previous
        # if node.prev is not None:
        #     node.prev.next = node.next
        # if node.next is not None:
        #     node.next.prev = node.prev
        # self.tail.next = node
        # node.prev = self.tail
        # node.next = None
        # self.tail = node

    def delete(self, node):
        return node.delete()

    def get_max(self):
        if self.head is None:
            return None

        max_val = self.head.value
        next_val = self.head.next

        while next_val is not None:
            if max_val < next_val.value:
                max_val = next_val.value
            next_val = next_val.next

        return max_val


node = ListNode(1)
dll = DoublyLinkedList(node)

dll.add_to_tail(5)
dll.add_to_tail(6)
print(dll.head.value)
print(dll.tail.value)
dll.move_to_front(dll.tail)
print(dll.head.value)
print(dll.head.next.value)
print(dll.tail.prev.value)
