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
        height = 0
        def traverse(node, h):
            if node == None:
                return h - 1
            traverse(node.node.left, h + 1)
            traverse(node.node.right, h + 1)
            self.height = max(self.height, h)
        traverse(self, height)
        pass

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        def find_depth(node, h):
            if node == None:
                return h - 1
            l = find_depth(node.node.left, h + 1)
            r = find_depth(node.node.right, l + 1)
            return r
        l = find_depth(self.node.left, 1)
        r = find_depth(self.node.right, 1)
        # print(self.node.key, l, r)
        self.balance = l - r
    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        p = self
        c = self.node.right
        c_l = c.node.left

        p.node.right = c_l
        p.node, c.node = c.node, p.node
        p.node.left = c
    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        p = self
        c = self.node.left
        c_r = c.node.right
        
        p.node.left = c_r
        p.node, c.node = c.node, p.node
        p.node.right = c
        
        
    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    # determine the type of rotation
    def rebalance(self):
        if self.balance >= 2:
            if self.node.left.balance < 0:
                self.node.left.left_rotate()
                self.right_rotate()
            else:
                self.right_rotate()
        elif self.balance <= -2:
            if self.node.right.balance > 0:
                self.node.right.right_rotate()
                self.left_rotate()
            else:
                self.left_rotate()
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        new_node = Node(key)
        new = AVLTree(new_node)
        prev = node
        def traverse(node, prev, new):
            if new.node.key < node.node.key:
                prev = node
                node = node.node.left
                if node == None:
                    prev.node.left = new
                    return
                traverse(node, prev, new)
                node.update_balance()
                # node.rebalance()
            else:
                prev = node
                node = node.node.right
                if node == None:
                    prev.node.right = new
                    return
                traverse(node, prev, new)
                node.update_balance()
                # node.rebalance()
        traverse(self, prev, new)
        self.update_balance()
        # self.rebalance()
        
# node = Node(8)
node = Node(5)

avl = AVLTree(node)


avl.insert(3)
avl.insert(4)
avl.insert(2)
avl.insert(1)

# print(avl.balance)


# node = avl.right_rotate(avl.node.right)
# avl.node.right = node

print(avl.display())

# print(avl.balance)
# print(avl.node.left.balance)
# print(avl.node.left.node.right.balance)
# print(avl.node.left.node.left.balance)
# print(avl.node.left.node.left.node.left.balance)


# avl.insert(3)
# avl.insert(1)
# avl.insert(6)
# avl.insert(4)
# avl.insert(7)
# avl.insert(10)
# avl.insert(14)
# avl.insert(13)
# avl.insert(12)

# avl.update_height()
# print(avl.height)
# print(avl.update_balance())
# avl.display()
