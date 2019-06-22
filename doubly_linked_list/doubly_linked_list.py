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
        if self.head and self.tail:
            curr_head = self.head
            new_head = ListNode(value, None, curr_head)
            self.head = new_head
            curr_head.prev = new_head
        else:
            self.head = ListNode(value)
            self.tail = self.head

    def remove_from_head(self):
        if self.head:
            curr_head = self.head
            if self.tail:
                next = self.head.next
                self.head = next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
        return curr_head.value

    def add_to_tail(self, value):
        # other steps first

        self.tail.insert_after(value)

    def remove_from_tail(self):
        if self.tail:
            curr_tail = self.tail
            curr_tail.delete()
            self.tail = curr_tail.prev
            return curr_tail.value

    def move_to_front(self, node):
        # remove `node` ...ListNode delete() BUT need to save value 1st
        value = node.value
        node.delete()
        # add `node` to head...add_to_head()
        self.add_to_head(value)

    def move_to_end(self, node):
        # similar to move_to_front()
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def delete(self, node):
        node.delete()

    def get_max(self):
        # if list is empty, return None
        if self.head == None:
            return None

        else:
            cur_max = self.head.value
            cur_node = self.head
            # loop through nodes until reach tail
            while cur_node.next:  # != None:
                cur_node = cur_node.next
                # if we find a node > cur_max, update cur_max
                if cur_node.value > cur_max:
                    cur_max = cur_node.value

            return cur_max
