class BinarySearchTree:

    # O(1)
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """
    A new key is always inserted at leaf.
    We start searching a key from root till we hit a leaf node.
    Once a leaf node is found,
    the new node is added as a child of the leaf node.
    """
    # O(log n)
    def insert(self, value):
        # Defines wich side of the tree to add the value as the string version of the attribute
        attr = "right" if value >= self.value else "left"  # O(1)
        # Gets the child binary search tree desired (either larger or smaller side)
        child_bst = getattr(self, attr)  # O(1) probably
        # If the child is empty
        if child_bst is None:
            # create a new bst
            new_bst = BinarySearchTree(value)  # O(1)
            # set it to the new bst
            setattr(self, attr, new_bst)  # O(1) probably
        # If it's not
        else:
            # Insert it into child tree (recursively)
            child_bst.insert(value)  # Recursing through half so O(log n)

    """
    To search a given key in Binary Search Tree,
    we first compare it with root,
    if the key is present at root, we return root.
    If key is greater than root’s key,
    we recur for right subtree of root node.
    Otherwise we recur for left subtree.
    """
    # O(n) if tree is unbalanced, otherwise O(log n)
    def contains(self, target):
        if self.value == target:
            return True
        attr = "right" if target > self.value else "left"  # O(1)
        child_bst = getattr(self, attr)  # O(1) probably
        if child_bst is None:
            return False  # O(1)
        return child_bst.contains(target)  # Recurses through half so O(log n) - if tree is balanced

    # O(log n)
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()  # Recurses through half so O(log n)
