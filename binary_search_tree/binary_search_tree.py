class Node:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

class BinarySearchTree:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # if self is None:
    #   self = Node(value)
    # else:
    #   curr_val = self
    #   if value < curr_val.value:
    #     while curr_val.left:
    #       curr_val = curr_val.left
    #     curr_val.left = Node(value)
    #   else:
    #     while curr_val.right:
    #       curr_val = curr_val.right
    #     curr_val.right = Node(value)
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
      

  def contains(self, target):
    # curr_val = self.value
    # if target < curr_val:
    #   curr_val = self.left
    #   if target == curr_val:
    #     return True
    # elif target > self.value:
    #   curr_val = self.right
    #   if target == curr_val:
    #     return True
    # else:
    #   return True
    # return False
    if self.value == target:
      return True
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
    else:
      if self.right:
        return self.right.contains(target)
    return False

  def get_max(self):
    # curr_val = self.value
    # while self.right is not None:
    #   if self.right > curr_val:
    #     curr_val = self.right
    # return curr_val
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
    