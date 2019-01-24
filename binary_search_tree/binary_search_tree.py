class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #recursive function to traverse tree to insert an item
    # ‎O(log n) --- provided tree is balanced

    if value < self.value:
      #as long as value is less than parent, go down the left side
      #continue until reaching a null value, then create new node/instance on tree
      if self.left != None:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
      
    elif value > self.value:
      #same as above, but right side for greater values
      if self.right != None:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
   #takes in a target value, checks tree for specified value
   #using recursion 
    if target == self.value:
      return True
  
  #if less than parent check left
    if target < self.value:
      if self.left == None:
        return False
      return self.left.contains(target)

  #if greater than parent check right 
    if target > self.value:
      if self.right == None:
        return False
      return self.right.contains(target)

  def get_max(self):
    #largest item is the right most node's value, 
    # so get right most using recursive method to traverse tree
    if self.right:
      return self.right.get_max()
      
    return self.value

