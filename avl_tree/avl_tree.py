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
        height = -1
        node = self.node
        def traverse(node, h):
            if node == None:
                return h - 1
            traverse(node.left, h + 1)
            traverse(node.right, h + 1)
            self.height = max(self.height, h)
        traverse(node, height)

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        node = self.node
        def find_depth(node):
            if not node:
                return 0
            stack = []
            stack.append(node)
            max_depth = 0
            while len(stack) > 0:
                if not node:
                    node = stack.pop()
                    node = node.right
                    if node:
                        stack.append(node)
                else:
                    max_depth = max(max_depth, len(stack) + 1)
                    node = node.left
                    if node:
                        stack.append(node)
            return max_depth
        l = find_depth(node.left)
        r = find_depth(node.right)
        return l - r
        

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self, node):
        child = node.right
        l_child = child.left
        child.left = node
        node.right = l_child
        return child

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self, node):
        child = node.left
        r_child = child.right
        child.right = node
        node.left = r_child
        return child

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    # go to the node before the swap and then swap the next node with the next next
    def rebalance(self):
        i = 0
        if self.balance >= 2:
            while i < self.balance - 1:
                print(node.key)
                

        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        new_node = Node(key)
        new = AVLTree(new_node)
        node = self
        prev = node
        def traverse(node, prev, new):
            if new.node.key < node.node.key:
                prev = node
                node = node.left
                if node == None:
                    prev.left = new
                    return
                traverse(node, prev, new)
            else:
                prev = node
                node = node.right
                if node == None:
                    prev.right = new
                    return
                traverse(node, prev, new)
        traverse(node, prev, new)


# node = Node(8)
node = Node(5)

avl = AVLTree(node)

avl.insert(3)
avl.insert(4)

# node = avl.right_rotate(avl.node.right)
# avl.node.right = node

# print(avl.node.key)
# print(avl.node.left.key)
# print(avl.node.left.right.key)


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
