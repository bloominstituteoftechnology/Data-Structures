class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_val(self):
        return self.value

    def set_next(self, newNext):
        self.next = newNext

    def set_prev(self, newPrev):
        self.prev = newPrev

    def set_val(self, newVal):
        self.value = newVal


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.set_head_tail(node, node)
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def set_head_tail(self, head_val, tail_val):
        self.head = head_val
        self.tail = tail_val

    def swap_head_tail(self):
        value = self.head.get_val()
        self.head.set_val(self.tail.get_val())
        self.tail.set_val(value)

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value, opt=0):
        new_node = ListNode(value, None, self.head)
        if self.length:
            self.head.set_prev(new_node)
            self.head = new_node
        else:
            self.set_head_tail(new_node, new_node)
        self.length += 1 - opt

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = None
        if self.head and self.head.get_next():
            value = self.head.get_val()
            self.head = self.head.get_next()
            self.head.set_prev(None)
        elif self.head and not self.head.get_next():
            value = self.head.get_val()
            self.set_head_tail(None, None)
        self.length -= 1
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value, opt=0):
        new_node = ListNode(value, self.tail, None)
        if not self.length:
            self.set_head_tail(new_node, new_node)
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.length += 1 - opt

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        value = None
        if self.head and self.head.get_next():
            value = self.tail.get_val()
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        elif self.head and not self.head.get_next():
            value = self.tail.get_val()
            self.set_head_tail(None, None)
        self.length -= 1
        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.head:
            if node == self.head:
                return
            if self.length == 2 and node == self.tail:
                self.swap_head_tail()
            elif self.length > 2 and node == self.tail:
                self.add_to_head(self.tail.get_val(), 1)
                self.tail = self.tail.get_prev()
                self.tail.set_next(None)
            else:
                current = self.head
                while current:
                    if current == node:
                        self.add_to_head(current.get_val(), 1)
                        current.get_prev().set_next(current.get_next())
                        current.get_next().set_prev(current.get_prev())
                        break
                    current = current.get_next()

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.head:
            if node == self.tail:
                return
            if self.length == 2 and node == self.head:
                self.swap_head_tail()
            elif self.length > 2 and node == self.head:
                self.add_to_tail(self.head.get_val(), 1)
                self.head = self.head.get_next()
                self.head.set_prev(None)
            else:
                current = self.head
                while current:
                    if current == node:
                        self.add_to_tail(current.get_val(), 1)
                        current.get_prev().set_next(current.get_next())
                        current.get_next().set_prev(current.get_prev())
                        break
                    current = current.get_next()

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.head:
            if self.length == 1 and node == self.head:
                self.set_head_tail(None, None)
            elif self.length >= 2 and (node == self.head or node == self.tail):
                if node == self.head:
                    self.head = self.head.get_next()
                    self.head.set_prev(None)
                else:
                    self.tail = self.tail.get_prev()
                    self.tail.set_next(None)
            else:
                current = self.head
                while current:
                    if current == node:
                        current.get_prev().set_next(current.get_next())
                        current.get_next().set_prev(current.get_prev())
                        break
                    current = current.get_next()
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.head:
            max_value = self.head.get_val()
            if self.head.get_next():
                current = self.head
                while current:
                    if current.get_val() > max_value:
                        max_value = current.get_val()
                    current = current.get_next()
            return max_value