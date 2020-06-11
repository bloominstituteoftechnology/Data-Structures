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
        
        self.update_balance()

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        if not self.node:
            self.balance = 0
            return

        left_height = self.node.left.height if self.node.left else -1
        right_height = self.node.right.height if self.node.right else -1

        self.balance = left_height - right_height

        print(f"Balance of node with value {self.node.key} is {self.balance}")

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        parent_node = self.node # grab reference to parent node
        self.node = self.node.right.node # make self node the right node (should exist since we are rotating left)

        if self.node.left: # if self has a left child
            parent_node.right.node = self.node.left.node # move self's left child to parent's right
            self.node.left.node = parent_node # set self's left node to the parent node
        else:
            parent_node.right = None
            self.node.left = AVLTree(parent_node) # otherwise make new AVL tree with the parent node 

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        parent_node = self.node
        self.node = self.node.left.node

        if self.node.right:
            parent_node.left.node = self.node.right.node
            self.node.right.node = parent_node
        else:
            parent_node.right = None
            self.node.right = AVLTree(parent_node) 

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        self.update_height()

        if self.balance > 1: # left heavy
            print("Left heavy")
            if self.node.left.balance < 0: # left child is right heavy
                self.node.left.left_rotate()
                print("Rotating left child to the left")
            self.right_rotate()
            print("Rotating right")
            self.update_height()

        elif self.balance < -1: # right heavy
            print("Right heavy")
            if self.node.right.balance > 0: # right child is left heavy
                print("Rotating right child to the right")
                self.node.right.right_rotate()
            self.left_rotate()
            print("Rotating left")
            self.update_height()
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        # Decide where to put the key by drilling down recursively
        # If key is less than self.node.key
        # If self.left is None, self.left = new node with key
        # Otherwise insert with self.left
        # Do same for right side if equal or greater
        # Then we need to balance. This will be called as we go up the tree on each level.

        if not self.node:
            self.node = Node(key)

        elif key < self.node.key:
            if self.node.left:
                self.node.left.insert(key)
            else:
                self.node.left = AVLTree(Node(key))
        
        else:
            if self.node.right:
                self.node.right.insert(key)
            else:
                self.node.right = AVLTree(Node(key))
        
        self.rebalance()
