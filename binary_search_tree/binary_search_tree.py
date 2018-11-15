class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if not self.value:  # if it's the first node and empty value
            self.value = value
        elif value < self.value:  # if value is less than value on the current node
            if self.left is None:  # if there is space on the left of the current node
                self.left = BinarySearchTree(value)  # make a new node with value
            else:  # if there's already a node on the left, start running recursion of inherited insert() method with every new node
                self.left.insert(
                    value
                )  # runs recursively with provided number until there's an empty node, whether left or right
        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass
