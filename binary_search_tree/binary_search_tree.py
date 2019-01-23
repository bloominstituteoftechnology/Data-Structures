class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # print('self.value', self.value, self.left, self.right, value)
    print('self.value', self.value)
    print('lefty', self.left)
    print('right', self.right)
    print(value)
    parent = self.value
    print(self)
    if self.value is None:
      self.value = value
      print('1****')
    else:
      if self.value < value:
        if self.right is None:
          self.right = value
          print('R', self.value, self.left, self.right)
          return BinarySearchTree.insert(self, value)
          
        else:
          print('R ELSE', self.value, self.left, self.right)
          return BinarySearchTree(self.right)
      else:
        print(value, self)
        if self.left is None:
          self.left = value
          print('L', self.value, self.left, self.right)
          return BinarySearchTree.insert(self, value)
          
        else:
          print('L ELSE', self.value, self.left, self.right)
          return BinarySearchTree(self.left)
   

  def contains(self, target):
    curr = self.value
    print('CURR', curr)
    if curr == target:
      return True
    elif target < curr:
      print(curr)
    
    #   if curr.left:
    #     print('CURR.LEFT', curr.left)
    #     # return contains(curr.left, target)
    # else: 
    #   if curr.right:
    #     print('CURR.RIGHT', curr.right.value)
    #     # return contains(curr.right, target)
    return False


  def get_max(self):
    pass
