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
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode( value, self, current_next)
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
        new_node = ListNode(key, value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        key = self.head.key
        value = self.head.value
        self.delete(self.head)
        return key, value #dont know if this is needed or not, don't understand the need to return the key and value

    def add_to_tail(self, value):
        new_node = ListNode(key, value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        key = self.tail.key
        value = self.tail.value
        self.delete(self.tail)
        return key, value

    def move_to_front(self, node):
        if node is self.head:
            return
        key = node.key
        value = node.value
        self.delete(node)
        self.add_to_head(key, value)

    def move_to_end(self, node):
        if node is self.tail:
            return
        key = node.key
        value = node.value
        self.delete(node)
        self.add_to_tail(key, value)

    def delete(self, node):
        if not self.head and not self.tail:
            print("Tried deleting node not in the list")
            return
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            node.delete()

    def get_max(self):
        current_value = self.head
        max_value = current_value.value
        while current_value is not None:
            if current_value.value > max_value:
                max_value = current_value.value
            current_value = current_value.next
        return max_value
