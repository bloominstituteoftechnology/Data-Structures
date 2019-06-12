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

    def add_to_head(self, value):
        if not self.head:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = ListNode(value, self.head.prev, self.head)
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    def remove_from_head(self):
        if not self.head:
            return None
        if not self.head.next:
            head = self.head

            self.head = None

            self.tail = None

            self.length -= 1

            return head.value

        value = self.head.value

        self.head = self.head.next

        self.head.prev = None

        self.length -= 1

        return value

    def add_to_tail(self, value):
        if not self.head:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = ListNode(value, self.tail, self.tail.prev)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def remove_from_tail(self):
        if self.tail == self.head:
            tail = self.tail

            self.tail = None
            self.head = None
            self.length -= 1
            return tail.value
        tail = self.tail
        self.tail = self.tail.next
        self.length -= 1
        return tail.value

    def move_to_front(self, node):
        self.head.prev = node
        node.next = self.head
        self.head = node

    def move_to_end(self, node):
        node.prev = self.tail
        node.next = self.tail.next
        self.tail = node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev.next

    def get_max(self):
        pass


node = ListNode("Hello")
dll = DoublyLinkedList(node)

print(dll.head)
dll.remove_from_tail()
print(dll.head)
print(dll.tail)
print(dll)
print(len(dll))
