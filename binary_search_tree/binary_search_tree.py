class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # If value is less than self value check left
        if value < self.value:
             # if self left is None create bst and set to self.left
            if self.left is None:
                self.left = BinarySearchTree(value)
                return
            # If there is a value there then insert on next node
            self.left.insert(value)

          # If value is greater than self value check right
        elif value >= self.value:
             # if self left is None create bst and set to self.left
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            # If there is a value there then insert on next node
            self.right.insert(value)

    def contains(self, target):
        # if node.value equal to target return true
        if self.value == target:
            return True
        # if target greater than value check right
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        # if target less than value check left
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

    def get_max(self):
        if self.right == None:
            return self.value

        return self.right.get_max()
