class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):

      if value >= self.value:
        if self.right == None:
          self.right = BinarySearchTree(value)
          return
      if self.left == None:
       self.left = BinarySearchTree(value)
       return
      nodeSearch = self.left if value < self.value else self.right
      nodeSearch.insert(value)


  def contains(self, target):
   if self.value == target:
      return True

   nodeSearch = self.left if target < self.value else self.right
   if nodeSearch is None:
      return False

   return nodeSearch.contains(target)

  def get_max(self):
    left = self.value if self.left is None else self.left.get_max()
    right = self.value if self.right is None else self.right.get_max()
    return max([self.value, left, right])