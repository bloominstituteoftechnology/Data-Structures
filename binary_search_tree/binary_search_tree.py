class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
#check to see if we need to go left or right
    if value < self.value:
#if no left child just set it here
      if not self.left:
#set the left value to BST value
        self.left = BinarySearchTree(value)
#if it is, we recurse to the left and call the insert method
      else:
        self.left.insert(value)
#same thing for the right side
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
#base case
#if the value at the current node we are on matches target
#we return true
    if self.value == target:
      return True
#if target is less than value then we go left
#WHAT PART OF THE CODE MAKES IT GO LEFT????????????????
    elif target < self.value:
#if self.left exists, then we call contains target on it
      if self.left:
        return self.left.contains(target)
    else:
      if self.right:
        return self.right.contains(target)
    return False

  def get_max(self):
#if self does not exist return none
    if not self:
      return None
#or we can create a max_value variable and a current variable
    max_value = self.value
    current = self
#if current value is greater than max than current becomes the max
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value