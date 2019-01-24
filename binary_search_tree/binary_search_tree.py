class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    currently_searching_tree = self
    is_running = True
    while is_running:
        if value > currently_searching_tree.value:
            if currently_searching_tree.right:
                currently_searching_tree = currently_searching_tree.right
            else:
                currently_searching_tree.right = BinarySearchTree(value)
                is_running = False
        elif value < currently_searching_tree.value:
            if currently_searching_tree.left:
                currently_searching_tree = currently_searching_tree.left
            else:
                currently_searching_tree.left = BinarySearchTree(value)
                is_running = False
        else:
            is_running = False

  def contains(self, target):
    currently_searching_tree = self
    is_running = True
    while is_running:
        if target == currently_searching_tree.value:
            return True
        elif target > currently_searching_tree.value:
            if currently_searching_tree.right:
                currently_searching_tree = currently_searching_tree.right
            else:
                return False
        elif target < currently_searching_tree.value:
            if currently_searching_tree.left:
                currently_searching_tree = currently_searching_tree.left
            else:
                return False
        else:
            is_running = False

  def get_max(self):
    current_max = -9999999
    currently_searching_tree = self
    is_running = True
    while is_running:
        if currently_searching_tree.value > current_max:
            if currently_searching_tree.right:
                current_max = currently_searching_tree.value
                currently_searching_tree = currently_searching_tree.right
            else:
                return currently_searching_tree.value
                is_running = False
        else:
            is_running = False
