"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        if self.node is None:
            self.height = -1
        else:
            if self.node.left is None and self.node.right is None:
                self.height = 0
            elif self.node.right is None:
                self.height = self.node.left.update_height() + 1
            elif self.node.left is None:
                self.height = self.node.right.update_height() + 1
            else:
                self.height = max(self.node.left.update_height(),
                                  self.node.right.update_height()) + 1
        return self.height

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        if self.node is None or (self.node.left is None and 
                                 self.node.right is None):
            self.balance = 0
        else:
            # Update sub-tree balances.
            if self.node.left:
                self.node.left.update_balance()
            if self.node.right:
                self.node.right.update_balance()
                
            if self.node.right is None:
                self.balance = - self.node.left.height - 1
            elif self.node.left is None:
                self.balance = self.node.right.height + 1
            else:
                self.balance = (self.node.right.height -
                                self.node.left.height)
        return self.balance

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        original_parent = self.node
        self.node = original_parent.right.node
        original_parent.right = self.node.left
        self.node.left = AVLTree(original_parent)
        

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        original_parent = self.node
        self.node = original_parent.left.node
        original_parent.left = self.node.right
        self.node.right = AVLTree(original_parent)

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        self.update_height()
        self.update_balance()
        while abs(self.balance) > 1:
            if self.balance < -1:
                if self.node.left.balance > 0:
                    self.node.left.left_rotate()
                    self.update_height()
                    self.update_balance()
                self.right_rotate()
                self.update_height()
                self.update_balance()
            elif self.balance > 1:
                if self.node.right.balance < 0:  
                     self.node.right.right_rotate()
                     self.update_height()
                     self.update_balance()
                self.left_rotate()
                self.update_height()
                self.update_balance()

        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance.
    """
    def insert(self, key):
        if self.node is None:
            self.node = Node(key)
        else:
            if key < self.node.key:
                if self.node.left is None:
                    self.node.left = AVLTree(Node(key))
                else:
                    self.node.left.insert(key)
            else:
                if self.node.right is None:
                    self.node.right = AVLTree(Node(key))
                else:
                    self.node.right.insert(key)
        self.rebalance()
