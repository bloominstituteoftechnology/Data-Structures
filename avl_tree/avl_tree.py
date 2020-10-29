"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    def __str__(self):
          return "%s" % self.key
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
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        new_node = Node(key)
        if self.node == None:
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < self.node.key: 
            self.node.left.insert(key)
        elif key > self.node.key:
            self.node.right.insert(key)
        self.rebalance()

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        self.update_height(recursive = False)
        self.update_balance(recursive = False)
    
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                 if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_height()
                    self.update_balance()
                 self.rotate_right()
                 self.update_height()
                 self.update_balance()
            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_height()
                    self.update_balance()
                self.rotate_left()
                self.update_height()
                self.update_balance()

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_height()
                if self.node.right:
                    self.node.right.update_height()
            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else: 
            self.height = -1

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self, recursive = True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balance()
                if self.node.right:
                    self.node.right.update_balance()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def rotate_right(self):
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def rotate_left(self):
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
 
    def inorder_traverse(self):
        """
        Inorder traversal of the tree
            Left subree + root + Right subtree 
        """
        result = []

        if not self.node:
            return result
        
        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.key)
        result.extend(self.node.right.inorder_traverse()) 

        return result

        
 
    
tree = AVLTree()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print ('Inserting data', data)
for key in data: 
    tree.insert(key)
print (f'lala {tree.inorder_traverse()}' )


 