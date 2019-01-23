class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == value:
      return value
    if self.left is None:
      if value < self.value:
        print(f'{value} is less than {self.value}. inserting in left side of {self.value}')
        self.left = BinarySearchTree(value)
    if self.right is None:
      if value > self.value:
        print(f'{value} is greater than {self.value}. inserting in right side of {self.value}')
        self.right = BinarySearchTree(value)
    
    if value < self.value:
      #call insert with left node
      self.left.insert(value)
    if value > self.value:
      #call insert with right node
      self.right.insert(value)
      

  def contains(self, target):
    print(self.value)
    if self.value == target:
      print('found it!!!!!!')
      return True
    if self.left is None and self.right is None and self.value is not target:
      return False
    if target > self.value:
      self.right.contains(target)
    if target < self.value:
      self.left.contains(target)

  def get_max(self):
    pass


bst = BinarySearchTree(5)
print('created a new BST with value:', bst.value)
bst.insert(3)
print('added a new BST node:', bst.left.value)
bst.insert(1)
print('added a new BST node:', bst.left.left.value)
bst.insert(7)
bst.insert(6)
bst.insert(10)
bst.insert(8)
print(bst.contains(6))
print(bst.contains(1))
print(bst.contains(100))