class Node:
  def __init__(self, val):  # constructor
    self.value = val  # data
    self.leftChild = None # children initialized both to None (no child yet)
    self.rightChild = None

  def insert(self, data):
    if self.value == data: # did node that called the insert() already have the insert data  
      # don't want duplicates
      return False # if data already exists (duplicate) return False => not going to add it
    elif self.value > data: # check if self.value(current node) is greater than insert data
      if self.leftChild: # if insert data is < self.value(current node) 
        return self.leftChild.insert(data) # check if there's already a leftChild
      else: 
        self.leftChild = Node(data) # if there IS a leftChild then insert data goes there
        return True # if IS NOT a leftChild create a new node with insert data and add it as leftChild to self.value(current node)
      else: 
        # if insert data is > self.value
        if self.rightChild: # check for a rightChild
          return self.rightChild.insert(data) # if there IS a  rightChild insert data there
        else:
          self.rightChild = Node(data) # if IS NOT a rightChild create a new node with insert data 
          return True # and assign it as the new rightChild for that node
  # Insert() works recursively. Continues to dig down into the tree until it finds the right place to insert it. Then creates a new node and inserts it.
  # Returns TRUE when it inserts the value.
  # Will only return FALSE if it finds the node already exists in the tree.

  def find(self, data):
    if (self.value == data): # if self.value(current node) contains data looking for return TRUE
      return True
    elif self.value > data: # if current node is > data or data < self.value
      if self.leftChild: # check the leftChild exists
        return self.leftChild.find(data) # do a recursive find on leftChild for data
      else: 
        return False # if leftChild DOES NOT EXIST, return FALSE
    else:
      if self.rightChild: # check if there's a rightChild
        return self.rightChild.find(data) # do a recursive find on rightChild until we find it
      else:
        return False # if rightChild DOES NOT EXIST, return FALSE


class Tree:
  def __init__(self): # constructor
    self.root = None  # root node

  def insert (self, data): # INSERT function
    if self.root: # does root exist? if yes, there's at least 1 node in the tree
      return self.root.insert(data)
    else:
      self.root = Node(data) # call the recursive function using root node from root class
      return True

  def find(self, data): # searching for a value in find()
    if self.root: # check for a root existing already
      return self.root.find(data) # if root node exists it calls find() passing data as arg
    else:
      return False # if there's no root node then can automatically return false
      # (no need to search an empty tree)