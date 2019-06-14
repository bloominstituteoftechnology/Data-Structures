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
from queue import Queue
tabs = None
class AVLTree:
    def __init__(self, node=None, parent=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0
        self.parent = parent

    """
  Display the whole tree. Uses recursive def.
  """
    def __str__(self):
        return f"parent: {self.parent.node.key if self.parent is not None else 'None'} height: {self.height} balance: {self.balance}  \
            node key: {self.node.key} node left key: {self.node.left.node.key} node right key: {self.node.right.node.key} "

    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print('-' * level * 2, pref, self.node.key,
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
            return 0
        else:
            # Compute the height of each subtree
            if self.node.left is not None:
                lheight = self.node.left.update_height()
            else:
                lheight = 0
            if self.node.right is not None:
                rheight = self.node.right.update_height()
            else:
                rheight = 0

            # Use the larger one
            if lheight > rheight:
                self.height = lheight
                return lheight+1
            else:
                self.height = rheight
                return rheight+1

    """
  Updates the balance factor on the AVLTree class
  """

    def bfsIterate(self, q, cv):
        # print('iterate tree.value:', tree.value)
        # icb(tree.value)

        # using parents q cv level saving nodes in child q
        # parents q = child q

        childQ = Queue()
        while not q.isEmpty:
            global tabs
            tabs += '\t'
            if len(tabs) > 5:
                return
            parent = q.dequeue()
            if parent.node is None:
                return
            if parent.node.left is not None:
                childQ.enqueue(parent.node.left)
                cv(tabs + str(parent.node.left.node.key), 1)
            if parent.node.right is not None:
                childQ.enqueue(parent.node.right)
                cv(tabs + str(parent.node.right.node.key), -1)
            if not childQ.isEmpty:
                self.bfsIterate(childQ, cv)
        return None

    def breadthFirstForEach(self):
        global tabs
        tabs = ""
        q = Queue()
        q.enqueue(self)
        if self.node is not None:
            print(f'{self.node.key},{self.balance}')
            self.bfsIterate(q, lambda key,balance: print(f'{key},{balance}'))
    

    def update_balance(self):
        if self.node is None:
            return 0
        else:
            # Compute the height of each subtree
            if self.node.left is not None:
                lheight = self.node.left.update_balance()
            else:
                lheight = 0
            if self.node.right is not None:
                rheight = self.node.right.update_balance()
            else:
                rheight = 0
            self.balance = lheight - rheight
            return self.balance

    """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """

    def left_rotate(self):
        # self.breadthFirstForEach()
        if self.node is None:
            print('None exit')
            return
#   detect left right and rotate subtree right

#   down = 5 = self
#   up = 8 = down right
#   
#   up moves up with all children except up left

#   on output
#   up left = down
#   up right no chang
#   up parent = None
#
#   down left no change
#   down right = up left
#   down parent = up
#
#   up left parent = down
#   up left left = None


        right = self.node.right
        print('right/up', right.node.key)
        print('self/down', self.node.key)
        print('self/down left key', self.node.left.node.key)

        # down left no change
        right.node.left.parent = AVLTree()
        right.node.left.parent.node = self.node
        right.node.left.parent.balance = self.balance
        right.node.left.parent.height = self.height
        right.node.left.parent.parent = self.parent
        right.node.left.node.left = None
        self.node.right = right.node.left
        right.node.left = None
        print('self/down.node.right.node.key', self.node.right.node.key)
  
        assert self.node.right.node.right == None, 'down right.node.right is not None'
        self.parent = right        

        right.node.left = AVLTree()
        right.node.left.node = self.node
        right.node.left.balance = self.balance
        right.node.left.height = self.height
        right.node.left.parent = self.parent
        # up right = no change
        right.parent = None






        # set self from down to up
        self.node = right.node
        self.balance = right.balance
        self.height = right.height
        self.parent = right.parent
        print('output root',self)
        print('self.node.left.node.key.', self.node.left.node.key)        
        print('self.node.left.node.left.node.key', self.node.left.node.left.node.key)
        print('self.node.left.node.right.node.key', self.node.left.node.right.node.key)
        self.update_balance()
        # print('exiting') 
        # right.breadthFirstForEach()

    """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """

    def right_rotate(self):
        # self.breadthFirstForEach()
        if self.node is None:
            print('None exit')
            return
#   detect right left and rotate subtree left

#   down = 5 = self
#   up = 8 = down left
#   
#   up moves up with all children except up right
#   on output
#   up right = down
#   up left no chang
#   up parent = None
#
#   down right no change
#   down left = up right
#   down parent = up
#
#   up right parent = down
#   up right right = None


        left = self.node.left
        print('left/up', left.node.key)
        print('self/down', self.node.key)
        print('self/down right key', self.node.right.node.key)

        # down right no change
        left.node.right.parent = AVLTree()
        left.node.right.parent.node = self.node
        left.node.right.parent.balance = self.balance
        left.node.right.parent.height = self.height
        left.node.right.parent.parent = self.parent
        left.node.right.node.right = None
        self.node.left = left.node.right
        left.node.right = None
        print('self/down.node.left.node.key', self.node.left.node.key)
  
        assert self.node.left.node.left == None, 'down left.node.left is not None'
        self.parent = left        

        left.node.right = AVLTree()
        left.node.right.node = self.node
        left.node.right.balance = self.balance
        left.node.right.height = self.height
        left.node.right.parent = self.parent
        # up left = no change
        left.parent = None






        # set self from down to up
        self.node = left.node
        self.balance = left.balance
        self.height = left.height
        self.parent = left.parent
        print('output root',self)
        print('self.node.right.node.key.', self.node.right.node.key)        
        print('self.node.right.node.right.node.key', self.node.right.node.right.node.key)
        print('self.node.right.node.left.node.key', self.node.right.node.left.node.key)
        self.update_balance()
        # print('exiting') 
        # left.breadthFirstForEach()     

    """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """

    def rebalance(self):
        if self.node is None:
            return
        if self.balance > 1:
            self.left_rotate()
        if self.balance < -1:
            self.right_rotate()
        if self.node.left:
            self.node.left.rebalance()
        if self.node.right:
            self.node.right.rebalance()


    """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """

    def insert(self, key):
        if self.node == None:
            self.node = Node(key)
            return
        if key < self.node.key:
            if self.node.left == None:
                self.node.left = AVLTree(Node(key), self)
            else:
                self.node.left.insert(key)
        else:
            if self.node.right == None:
                self.node.right = AVLTree(Node(key), self)
            else:
                self.node.right.insert(key)  
        self.rebalance()     
