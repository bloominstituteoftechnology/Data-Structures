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

        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            # self = DoublyLinkedList(ListNode(value))

    def remove_from_head(self):
        temp = self.head
        if self.head and self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        elif self.head:
            self.head.delete()
            self.head = self.head.next
            self.length -= 1
            return temp.value

    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            # self = DoublyLinkedList(ListNode(value))

    def remove_from_tail(self):
        temp = self.tail
        if self.tail and self.tail == self.head:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        elif self.tail:
            self.tail.delete()
            self.tail = self.tail.prev
            self.length -= 1
            return temp.value

    def move_to_front(self, node):
        if self.head == node:
            pass
        elif self.tail == node:
            self.tail = node.prev
            self.tail.next = None
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
        else:
            node.delete()
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node

    def move_to_end(self, node):
        if self.tail == node:
            pass
        elif self.head == node:
            node.next.prev = None
            self.head = node.next
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        else:
            node.delete()
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

    def delete(self, node):
        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
            self.length -= 1
            return node.value
        elif self.head == node:
            node.delete()
            self.head = node.next
            self.length -= 1
            return node.value
        elif self.tail == node:
            node.delete()
            self.tail = node.prev
            self.length -= 1
            return node.value
        elif self.head == None and self.tail == None:
            pass
        else:
            node.delete()
            self.length -= 1
            return node.value

    def get_max(self):
        max_value = self.head.value
        current_node = self.head
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
