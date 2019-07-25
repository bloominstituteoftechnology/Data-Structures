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

      if self.node:
          return self.node.height

      else:
          return None

  """
  Updates the balance factor on the AVLTree class
  """
  def update_balance(self, recursive=True):

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
  def left_rotate(self):

        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node
        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root


  """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent.
  """
  def right_rotate(self):

        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node
        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root


  """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """
  def rebalance(self):

        self.update_height(recursive=False)
        self.update_balance(False)

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
                    self.node.right.rotate_right() # we're in case III
                    self.update_height()
                    self.update_balance()
                self.rotate_left()
                self.update_height()
                self.update_balance()

  """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """
  def insert(self, key):

        n = Node(key)

        if self.node == None:
            self.node = n
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key < self.node.key:
            self.node.left.insert(key)

        elif key > self.node.key:
            self.node.right.insert(key)

        self.rebalance()
