class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    print('self.value', self.value, self.left, self.right, value)
    if self.value == None:
      self.value == value
    if value > self.value:
      if self.right is None:
        self.right = value
        print('R', self.value, self.left, self.right)
      else:
        return(self.right, value)
    elif value < self.value:
      print(value, self.value)
      if self.left is None:
        self.left = value
        print('L', self.value, self.left, self.right)
      else:
        print('L ELSE', self.value, self.left, self.right)
        return(self.left, value)
    pass

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
