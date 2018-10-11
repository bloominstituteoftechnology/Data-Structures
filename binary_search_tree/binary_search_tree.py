class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.root = None

  def insert(self, value):
    if self.root == None:
      self.root = value
    else:
      self._insert(value, self.root)
      def _insert(self, value, current_node):
          if value < current_node.value:
            if current_node.left == None:
              current_node.left = value
            else:
              self._insert(value, current_node.left)
          elif value > current_node.value: 
            if current_node.right == None:
              current_node.right = value
            else:
              self._insert(value, current_node.right)
          else:
            print("Value already exists in the tree")

  def contains(self, target):
    if self.root == target:
      return True
    else:
      self._contains(target, self.root)
      def _contains(self, target, current_node):
          if target < current_node.target and current_node.left:
            if current_node.left == target:
              return True
            else:
              self._contains(target, current_node.left)
          elif target > current_node.target and current_node.right: 
            if current_node.right == target:
              return True
            else:
              self._contains(target, current_node.right)
    


  def get_max(self):
    maxNode = None
    maxed = False
    current_node = self.root
    if current_node is not None:
      maxNode = current_node.value
    while maxed is False:
      if current_node.right:
        maxNode = current_node.value
        current_node = current_node.right
      else:
        maxed = True
        return maxNode
