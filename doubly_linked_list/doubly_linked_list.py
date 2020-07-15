"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
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


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):

        new_node = ListNode(value)
        if self.head and self.tail:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.length += 1

    def remove_from_head(self):

        target_to_delete = self.head

        if self.length == 0:

            return None

        elif self.length == 1:

            self.length -= 1
            self.head = None
            self.tail = None

            return target_to_delete.value

        else:
            self.head = target_to_delete.next
            self.length -= 1

            return target_to_delete.value

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.tail and self.head:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def remove_from_tail(self):
        tail_to_delete = self.tail
        if not self.head:
            return None
        elif self.length == 1:
            self.tail = None
            self.head = None
            self.length -= 1
            return tail_to_delete.value
        else:
            self.length -= 1
            self.tail = tail_to_delete.prev

            return tail_to_delete.value

    def move_to_front(self, node):
        if node == self.head:
            return
        else:
            temp = node.value
            self.delete(node)
            self.add_to_head(temp)

    def move_to_end(self, node):
        if node == self.tail:
            return
        else:
            temp = node.value
            self.delete(node)
            self.add_to_tail(temp)


    def delete(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.tail:
            self.tail = node.prev
            node.delete()
        elif node == self.head:
            self.head = node.next
            node.delete()
        else:
            node.delete()
        self.length -= 1


    def get_max(self):
        if self.head is None:
            return None
        current = self.head
        current_max = current.value
        while current.next is not None:
            current_max = max(current_max, current.next.value)
            current = current.next
        return current_max


dd = DoublyLinkedList(ListNode(1))

print(dd.get_max())
dd.add_to_tail(100)

print(dd.tail.value)
dd.add_to_tail(55)

print(dd.get_max())
