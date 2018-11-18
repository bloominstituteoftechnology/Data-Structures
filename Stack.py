class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return f'<Node: {self.value}>'

    def __repr__(self):
        return f'<Node: {self.value}>'


class Stack:

    def __init__(self):
        self.head = None

    def pop(self):
        if self.head is None:
            return None

        n = self.head
        self.head = self.head.next_node
        n.next_node = None

        return n

    def push(self, n):
        n = Node(n)
        n.next_node = self.head
        self.head = n

    def __str__(self):
        r = ""

        p = self.head
        while p != None:
            r += str(p) + ' -> '
            p = p.next_node

        return r


s = Stack()
s.push('Brian')
s.push('Shawn')
s.pop()
print(s)
