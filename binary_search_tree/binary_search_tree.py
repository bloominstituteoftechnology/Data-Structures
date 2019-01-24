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
    else:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    elif target < self.value:
      if self.left is not None:
        return self.left.contains(target)
      else:
        return False
    elif target > self.value:
      if self.right is not None:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    if self.right is not None:
      return self.right.get_max()
    else:
      return self.value

  def print_tree(self):
    # import time
    if self.left is not None:
      self.left.print_tree()
    # time.sleep(.1)
    print(self.value)
    if self.right is not None:
      self.right.print_tree()

print('binary search tree ran')

def fill_tree(root, num_elems = 100, max_int = 1000):
  from random import randint
  tree = BinarySearchTree(root)
  for i in range(num_elems):
    cur_elem = randint(0, max_int)
    tree.insert(cur_elem)
  return tree

bst = fill_tree(500)
print(f'Highest: {bst.get_max()}')
print(f'Contains 500: {bst.contains(500)}\n')
print(f'Sorted:')
bst.print_tree()

# bst = BinarySearchTree(5)
# bst.insert(6)
# print(bst.contains(5))
# print(bst.contains(6))
# print(bst.contains(7))
# bst.insert(7)
# print(bst.contains(7))
# print(bst.get_max())
# bst.print_tree()

