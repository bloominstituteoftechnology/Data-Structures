class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # check if value is less than self.value
        if value < self.value:
            # check if self.left exists
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value > self.value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):

        # Check if target equals self.value
        if target == self.value:
            # Found target, return true
            return True

        # Check if target is less than self.value
        if target < self.value:
            # Check if self.left exists
            if self.left == None:
                # Cannot find target, return false
                return False
            # Recursively calls contains method passing target
            return self.left.contains(target)
        # Check if target is greater than self.value
        if target > self.value:
            # Check if self.right exists
            if self.right == None:
                # Cannot find target, return false
                return False
            # Recursively calls contains method passing target
            return self.right.contains(target)

    def get_max(self):
        if self.right == None:
            return self.value
        return self.right.get_max()
