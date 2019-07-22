class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value == self.value:
      return
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
    if target == self.value:
      return True
    elif not self.left and not self.right:
      return False
    elif self.value < target:
      if self.right:
        return self.right.contains(target)
      else:
        return False
    else:
      if self.left:
        return self.left.contains(target)
      else:
        return False

  def get_max(self):
    max_val = self.value
    next_leaf = self.right
    while(next_leaf):
      max_val = next_leaf.value
      next_leaf = next_leaf.right
    return max_val

  def for_each(self, cb):
    def inorder(root):
      if root:
        inorder(root.left)
        cb(root.value)
        inorder(root.right)
    inorder(self)
'''
bst = BinarySearchTree(8)

bst.insert(1)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.insert(4)
bst.insert(10)
bst.insert(13)
bst.insert(14)

print(bst.contains(7))
print(bst.contains(9))

print(bst.get_max())

bst.insert(30)
print(bst.get_max())

bst.insert(300)
bst.insert(3)
print(bst.get_max())
pass
'''
