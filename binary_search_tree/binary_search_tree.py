class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left == None:
        return False
      else:
        return self.left.contains(target)
    elif target >= self.value:
      if self.right == None:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if self.right == None: return self.value
    return self.right.get_max()

def main():
  # My Janky Test Program
  my_bst = BinarySearchTree(5)
  my_bst.insert(2)
  my_bst.insert(3)
  my_bst.insert(7)
  print('Contains 7? ',my_bst.contains(7))
  """
  This is where I found out that if you want 
  your function to give you a result, you have 
  to tell it to give it to you.
  """

if __name__ == '__main__':
  main()
