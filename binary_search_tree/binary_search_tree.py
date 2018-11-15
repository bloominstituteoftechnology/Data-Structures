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
        if target == self.value:  # if root node and target has the same value
            return True
        elif target < self.value:  # if target has a smaller value
            if (
                self.left is None
            ):  # if there's no node to the left, nothing else to search
                return False
            else:  # if there is a node basically, start running the recursion
                return self.left.contains(
                    target
                )  # run recursive check on left nodes to check a target match
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:  # all cases + if there's no root node
            return False

    def get_max(self):
        pass
