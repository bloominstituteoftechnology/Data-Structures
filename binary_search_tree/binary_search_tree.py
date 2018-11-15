class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'<Node: {self.value}>'

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class BinarySearchTree:

    def __init__(self, value=None):
        self.value = Node(value)
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value.get_value():
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

        if value > self.value.get_value():
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass


bst = BinarySearchTree("50")
bst.insert("25")
bst.insert("75")
print("SELF" + str(bst.value))
print("LEFT: " + str(bst.left))
print("RIGHT: " + str(bst.right))
