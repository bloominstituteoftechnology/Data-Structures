class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, new_value):
    current = self
    while current.left or current.right:
        if new_value > current.value:
            if current.right:
                current = current.right
            else:
                current.right = current
                break
        elif new_value < current.value:
            current = current.left
    if new_value >= current.value:
        current.right = BinarySearchTree(new_value)
    elif new_value < current.value:
        current.left = BinarySearchTree(new_value)

  def contains(self, target):
    number = 0
    current = self
    if target == current.value:
        number += 1
    if self.right:
        number += self.right.contains(target)
    if self.left:
        number += self.left.contains(target)
    return number

  def get_max(self):
    max_amount = 0
    while current:
        max_amount = current.value
        current = current.right
    return max_amount

  def for_each(self, cb):
    # I need a way of keeping track of the two-way nodes that I pass down and which way I have passed down them.
        # - Make a dictionary. Each node is the key, the value is a tuple of "right, left". I can check to see if the value contains right, and then go right, or vice versa. When I go one direction I replace the value with a string signifying the remaining direction.
    # I need to go down each side of each one and pass in the value as an argument for the call-back
        # - I can use a while true loop and break only when the directions_dictionary is exhausted

    # New plan - just use recursion. It can work.
    cb(self.value)
    if self.right:
        self.right.for_each(cb)
    if self.left:
        self.left.for_each(cb)
