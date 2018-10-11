class Node:
  def __init__(self, value=None, next_left=None, next_right=None):
    self.value = value
    self.next_left = next_left
    self.next_right = next_right
  
  def set_next_right(self, new_next_right):
    self.next_right = new_next_right 

  def set_next_left(self, new_next_left):
    self.next_left = new_next_left 


class BinarySearchTree:
  def __init__(self, root, left=None, right=None):
    self.root = Node(root)
    self.left = left
    self.right = right

  def insert(self, new_value):
    root = self.root

    while new_value > root.value:
      if root.next_right is None:
        root.set_next_right(Node(new_value))
      return
    
    while new_value < root.value:
      if root.next_left is None:
        root.set_next_left(Node(new_value))
      return

    return self.insert(root)
    
 
  def contains(self, target):
    search = self.root
    if search == target:
      return True

    while search.next_left:
      if search.next_left == target:
        return True
      search = search.next_left
    
    while search.next_right:
      if search == target:
        return True
      search = search.next_right
    
    return self.contains(target)
    

  def get_max(self):
    pass
