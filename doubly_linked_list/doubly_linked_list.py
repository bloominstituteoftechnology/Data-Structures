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
        # create listNode w/value
        node = ListNode(value)
        # empty list
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            #node.next = self.head

        self.length += 1

        pass

    def remove_from_head(self):
        pass

    def add_to_tail(self, value):
        self.tail.insert_after(value)
        # not a complete solution
        pass

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        value = node.value
        node.delete()
        # add node to head ... add to head()
        self.add_to_head(value)

    def move_to_end(self, node):
            # similar to move to front
        pass

    def delete(self, node):
        pass

    def get_max(self):
        if self.head == None:
            return None
        else:
            cur_max = self.head.value
            cur_node = self.head

        # loop through nodes until reach tail
        # if list empty, return None
        # if we find node > max, update max
        # return max value
        while cur_node.next:  # !=None:
            cur_node = cur_node.next
            if cur_node.value > cur_max:
                cur_max = cur_node
                # don't forget to check the value

        return cur_max
