from typing import Optional

"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left: Optional[AVLTree] = None
        self.right: Optional[AVLTree] = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node: Optional[Node] = node
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
        if not self.node:
            self.height = -1
        
        else:
            left_height = -1
            right_height = -1

            if self.node.left:
                self.node.left.update_height()
                left_height = self.node.left.height
            if self.node.right:
                self.node.right.update_height()
                right_height = self.node.right.height
                
            self.height = max(left_height, right_height) + 1


    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        self.balance = self.node.left.height - self.node.right.height
        if self.node.left:
            self.node.left.update_balance()
        if self.node.right:
            self.node.right.update_balance()

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        parent_node = self.node
        self.node = self.node.right.node
        parent_node.right.node = self.node.left.node
        self.node.left.node = parent_node

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        parent_node = self.node
        self.node = self.node.left.node
        parent_node.left.node = self.node.right.node
        self.node.right.node = parent_node

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        pass
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        pass
