class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current_node = self

    while True: # Iterative Solution for Funsies
      if value < current_node.value:
        if current_node.left is None:
          current_node.left = BinarySearchTree(value)
          break
        else:
          current_node = current_node.left
      else:
        if current_node.right is None:
          current_node.right = BinarySearchTree(value)
          break
        else: 
          current_node = current_node.right

    # while True: ##  First Pass Solution <-- WARNING - DOES NOT WORK - ACTUAL MADNESS
      # if current_node.right == None and current_node.left == None:
      #   current_node.right = BinarySearchTree(value)
      #   break
    #   elif current_node.right == None:
    #     if value >= current_node.left.value:
    #       current_node.right = BinarySearchTree(value)
    #       break
    #     else:
    #       current_node = current_node.left
    #   elif current_node.left == None: 
    #     if value <= current_node.right.value:
    #       current_node.left = BinarySearchTree(value)
    #       break
    #     else:
    #       current_node = current_node.right
    #   elif value >= current_node.right:
    #     current_node = current_node.right
    #   else:
    #     current_node = current_node.left


        


  def contains(self, target):
    if self.value is target:
      return True
    elif target < self.value and self.left is not None:
      return self.left.contains(target)
    elif self.right is not None:
      return self.right.contains(target)
    else:
      return False

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()

