"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_to_tail(self, value):
        new_tail = Node(value=value)
        if self.head == None:
            self.head = new_tail
            self.tail = new_tail
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_tail
            self.tail = new_tail

    def remove_head(self):
        current = self.head
        if current == None: return None
        self.head = self.head.next
        current.next = None
        return current.get_value()

    def contains(self, value):
        current = self.head
        while current != None:
            if current.get_value() == value:
                return True
            current = current.next
        return False

    def get_max(self):
        current = self.head
        if current == None: return None
        max = 0
        while current != None:
            if current.get_value() > max:
                max = current.get_value()
            current = current.next
        return max

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


# LL = LinkedList()
# for i in range(10):
#     LL.add_to_tail(i)
#
# LL.add_to_tail(3)
# print(LL.head.get_value())
# print([node.get_value() for node in LL])
# LL.remove_head()
# print(LL.head.get_value())
# print([node.get_value() for node in LL])
# print(LL.contains(9))
# print(LL.contains(11))
# print(LL.get_max())