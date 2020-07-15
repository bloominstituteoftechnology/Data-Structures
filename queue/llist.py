class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def __repr__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # def add_to_tail(self, value):
    #     if self.head is None:
    #         self.head = Node(value)
    #     curr = self.head
    #     while curr.next:
    #         print(curr.next)
    #         curr = curr.next
    #     curr.next = Node(value)

    def add_to_tail(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        if not self.head.next:
            head = self.head
            self.head = None
            self.tail = None
            return head.value
        else:
            head = self.head
            print('head', head.next.value, head.value)
            self.head = head.next
            return head.value

    def contains(self, val):
        return self._contains(self.head, val)

    def _contains(self, node, val):
        if not node:
            return False
        if node.next is None:
            return False if node.value != val else True
        else:
            if node.value == val:
                return True
            else:
                return self._contains(node.next, val)

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

    def print_list(self):
        curr = self.head
        lst = []
        while curr is not None:
            lst.append(curr)
            curr = curr.next
        print([f'{x}====>' for x in lst])
