"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.value}'


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

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        head = self.head
        if not self.head:
            self.length += 1
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if not self.head:
            return None
        elif not self.head.next:
            head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return head.value
        else:
            new_head = self.head.next
            head = self.head
            self.head = new_head
            self.head.prev = None
            self.length -= 1
            return head.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        if not self.head:
            return self.add_to_head(value)
        new_node = ListNode(value)
        tail = self.tail
        self.tail.next = new_node
        new_node.prev = tail
        self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if not self.tail:
            return None
        if self.head is self.tail:
            val = self.tail.value
            print(self.head, self.tail, val)
            self.tail = None
            self.head = None
            self.length -= 1
            return val
        tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return tail.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.length == 1:
            return
        elif self.length == 2:
            head = self.head
            tail = self.tail
            self.head = self.tail
            self.head.prev = None
            self.head.next = head
            head.prev = self.head
            head.next = None
            self.tail = head
            return
        elif self.tail == node:
            new_tail = self.tail.prev
            tail = self.tail
            self.tail = new_tail
            new_tail.next = None
            tail.next = self.head
            tail.prev = None
            self.head.prev = tail
            self.head = tail
            return
        else:
            return self._move_to_front(self.head, node)

    def _move_to_front(self, node, val):
        if not node:
            return
        elif node == val:
            n = node
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.prev = n
            n.next = self.head
            n.prev = None
            self.head = n
            return
        else:
            return self._move_to_front(node.next, val)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.tail.value == node:
            return
        elif self.length == 1:
            return
        elif self.length == 2:
            head = self.head
            self.head = self.tail
            self.head.next = head
            self.head.prev = None
            head.prev = self.tail
            self.tail = head
            self.tail.next = None
            return
        elif self.head == node:
            next = self.head.next
            head = self.head
            self.head = next
            self.head.prev = None
            self.tail.next = head
            head.prev = self.tail
            self.tail = head
            return
        else:
            return self._move_to_end(self.head, node)

    def _move_to_end(self, node, val):
        if not node:
            return None
        elif node == val:
            n = node
            prev = node.prev
            node.next.prev = node.prev
            node.prev.next = node.next
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
            print(self.tail, self.head)
            self.tail.next = None
        else:
            return self._move_to_end(node.next, val)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.length == 1:
            val = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        elif node == self.head:
            val = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return val
        elif node == self.tail:
            val = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return val
        else:
            return self._delete(self.head, node)

    def _delete(self, node, val):
        if not node:
            return
        elif node == val:
            n = node
            node.next.prev = node.prev
            node.prev.next = node.next
            self.length -= 1
            return n
        else:
            return self._delete(node.next, val)
    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        return self._get_max(self.head)

    def _get_max(self, node, m=0):
        if self.head is None:
            return None
        if node is None:
            return m
        else:
            m = m if m > node.value else node.value
            return self._get_max(node.next, m)

    def reverse(self):
        return self._reverse(self.head)

    def _reverse(self, node):
        if not node.next:
            self.head = node
            self.head.next = node.prev
            self.head.prev = None
            return
        else:
            n = node.next
            print('n', n)
            node.next = node.prev
            node.prev = n
            return self._reverse(n)

    def print_list(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr)
            curr = curr.next
        print([f'{x.prev}<====={x}=====>{x.next}' for x in lst])


lst = DoublyLinkedList()
# lst.add_to_head(1)
lst.add_to_head(1)
lst.print_list()
# lst.delete(1)
# lst.delete(10)
# lst.move_to_front(10)
lst.add_to_tail(40)
lst.add_to_tail(4)

print(lst.head.next, 'nextttt')
lst.move_to_end(lst.head.next)
lst.print_list()
lst.add_to_tail(3)
lst.move_to_front(lst.tail)
print(lst.head.next, 'head next')
# lst.delete(10)
# lst.delete(69)
lst.print_list()
lst.reverse()
lst.print_list()
print(len(lst))
