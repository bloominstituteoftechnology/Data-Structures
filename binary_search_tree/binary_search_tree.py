class BinarySearchTree:

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
    def insert(self, value):
        
        # Defines wich side of the tree to add the value as the string version of the attribute
        attr = "right" if value >= self.value else "left"
        # Gets the child binary search tree desired (either larger or smaller side)
        child_bst = getattr(self, attr)
        # If the child is empty
        if child_bst is None:
            # create a new bst
            new_bst = BinarySearchTree(value)
            # set it to the new bst
            setattr(self, attr, new_bst)
        # If it's not
        else:
            # Insert it into child tree (recursively)
            child_bst.insert(value)
        
        "Same as above"
        # if value >= self.value:
        #     if self.right is None:
        #         self.right = BinarySearchTree(value)
        #     else:
        #         self.right.insert(value)
        # else:
        #     if self.left is None:
        #         self.left = BinarySearchTree(value)
        #     else:
        #         self.left.insert(value)

    """
    To search a given key in Binary Search Tree,
    we first compare it with root,
    if the key is present at root, we return root.
    If key is greater than root’s key,
    we recur for right subtree of root node.
    Otherwise we recur for left subtree.
    """
    def contains(self, target):
        # Check to see if head is equal to target
        isEqualTo = self.head.isEqalTo(target)
        # 1. Start from root.
        # 2. Compare the inserting element with root, if less than root, then recurse for left, else recurse for right.
        # 3. If element to search is found anywhere, return true, else return false.

    def get_max(self):
        pass
