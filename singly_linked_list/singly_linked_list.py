class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node

    def __str__(self):
        return f'{self.value}'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            return value

        else:
            value = self.tail.get_value()
            curr_node = self.head

            while curr_node.get_next() != self.tail:
                curr_node = curr_node.get_next()

            self.tail = curr_node
            self.tail.set_next(None)
            return value

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    def __str__(self):
        return f'tail: {self.tail}, head: {self.head} '



l = LinkedList()

l.add_to_tail(1)
l.add_to_tail(2)
l.add_to_tail(3)


print(l)