#https://www.tutorialspoint.com/python/python_binary_tree.htm
# Tree represents the nodes connected by edges. It is a non-linear data structure. 
# It has the following properties.
# One node is marked as Root node.
# Every node other than the root is associated with one parent node.
# Each node can have an arbiatry number of chid node.
# We designate one node as root node and then add more nodes as child nodes.


class BinarySearchTree:
  def __init__(self, value):
    # We just create a Node class and add assign a value to the node.
    # This becomes tree with only a root node.
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #compare the new value wit the parent node
    if self.value:
      if value < self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)
      elif value > self.value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
    else:
      self.value = value

  def contains(self, target):
    #Searching for a value in a tree involves comparing the incoming value 
    # with the value exiting nodes. Here also we traverse the nodes from left 
    # to right and then finally with the parent. If the searched for value does 
    # not match any of the exitign value, then we return not found message else 
    # the found message is returned.
    if target < self.value:
      if self.left is None:
        return str(target) + "Sorry Not found"
      return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return str(target) + "Sorry Not found"
      return self.right.contains(target)
    else:
      print(str(self.value) + " is found")


  def get_max(self):
    pass


  # #Print Tree
  # def PrintTree(self):
  #   if self.left:
  #     self.left.PrintTree()
  #   print(self.value),
  #   if self.right:
  #     self.right.PrintTree()

  # #use insert to add nodes
  # root = Node(12)
  # root.insert(8)
  # root.insert(13)
  # #etc