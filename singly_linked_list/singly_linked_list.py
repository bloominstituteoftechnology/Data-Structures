class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.count = 0

    def add_to_head(self, data):
        new_node = Node(value=data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
        if self.count == 1:
            self.tail = self.head

    def remove_head(self):
        if self.count > 0:
            temp = self.head
            self.head = self.head.next_node
            self.count -= 1

            if self.count == 0:
                self.tail = None

            return temp.value

    def add_to_tail(self, data):
        new_node = Node(value=data)
        if self.count == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.set_next(new_node)
        self.tail = new_node
        self.count += 1

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next_node
        return False

    def get_max(self, start=None):
        if start:
            current = start
        else:
            current = self.head
        try:
            if current.next_node is not None:
                return max(current.value, self.get_max(start=current.next_node))
            elif current.next_node is None:
                return current.value
        except AttributeError:
            return None
