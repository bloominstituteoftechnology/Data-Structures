
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.get_value

    def get_next_node(self):
        return self.get_next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def add_to_tail(self, value):
        self.length += 1
        new_node = Node(value)
        if not self.head:
            self.head, self.tail = new_node, new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node            

    def remove_head(self):
        if not self.head:
            return None
        self.length -= 1
        head_value = self.head.value
        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next_node
        return head_value

    def add_to_head(self, value):
        self.length += 1
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
        else:
            prev_head = self.head
            self.head = new_node
            self.head.set_next(prev_head)

    def contains(self, target):
        for i in self:
            if i.value == target:
                return True
        return False

    def __len__(self):
        return self.length

    def get_max(self):
        if not self.head:
            return None
        if len(self) is 0:
            return None
        sorted_ll = sorted([i.value for i in self])
        return sorted_ll[-1]

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next_node