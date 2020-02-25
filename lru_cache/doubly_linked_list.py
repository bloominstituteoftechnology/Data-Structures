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
        newhead = ListNode(value)
        if not self.head:
            self.head = newhead
            self.tail = newhead
        else:
            newhead.next = self.head
            self.head.prev = newhead
            self.head = newhead
        self.length += 1

    def remove_from_head(self):
        if not self.head:
            return
        val = self.head.value
        if self.head is self.tail:
            self.head, self.tail = None, None
            self.length = 0
            return val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.length -= 1
        return val



    def add_to_tail(self, value):
        new = listNode(value)
        if not self.tail:
            self.head = new
            self.tail = new
        else:
            newhead.prev = self.tail
            self.tail.next = newhead
            self.tail = newhead
        self.length += 1

    def remove_from_tail(self):
        if not self.tail:
            return
        val = self.tail.value
        if self.tail is self.head:
            self.tail, self.head = None, None
            self.length = 0
            return val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.length -= 1

        return val
    

    def move_to_front(self, node):
            val = node.value
        if self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
        node.delete()
        self.length -= 1
        self.add_to_head(val)

    def move_to_end(self, node):
         val = node.value
        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
        node.delete()
        self.length -= 1
        self.add_to_tail(val)

    def delete(self, node):
         if self.head is node:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
        if self.tail is node:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None
        node.delete()
        self.length -= 1

    def get_max(self):
          if not self.head:
            return -1
        max_ = self.head.value
        curr = self.head
        while curr.next:
            curr = curr.next
            if curr.value > max_:
                max_ = curr.value
        return max_
