class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      """check
            -- if value is less than root.value
                 go to left
            -- if value is greater than root.value
                 go to right
      """
      #check is passed BST is empty
      root = self
      if root.value is None:
          return None
      
      # else check value_to_be_inserted is less than root value
      if value < root.value:
          #if the left child is empty insert the value_to_be_inserted as left child
          if root.left is None:
              root.left = BinarySearchTree(value)
          else:
              #if left child is present recursive call to check where to insert...
              root.left.insert(value)
      else:
          #if value_to_be_inserted is greater than root value go to right side
          #if right-child empty insert value_to_be_inserted
          if root.right is None:
              root.right = BinarySearchTree(value)
          else:
              #if right-child is there .. recursive call to check for value insertion
              root.right.insert(value)


  def contains(self, target):
      root = self
      if target == root.value:
          return True
      elif target < root.value:
          if root.left is not None:
              return root.left.contains(target)
      else :
          if self.right:
              return root.right.contains(target)
      return False

  def get_max(self):
      root = self
      #check if BST is empty
      if root.value is None:
          return None
      max_value = 0
      while root:
          if root.value > max_value:
              max_value = root.value
          root = root.right # as in BST higher values will be on right side 
                            # no need to check left-side          
      return max_value

  def display(self):
      root = self
      if root.value is None:
          return None

      if root.left:
          root.left.display()
      
      print(root.value, end = " -> ")

      if root.right:
          root.right.display()

bst = BinarySearchTree(8)
bst.insert(9)
bst.insert(12)
bst.insert(5)
bst.insert(3)
bst.insert(15)
bst.display()
       
