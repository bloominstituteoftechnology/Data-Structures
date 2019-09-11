class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # so first see if the root has a value if not then easy peasy insert the value
    if self.value == None:
          self.value == value
    # if it doesn't then it's safe to assume that there is a tree although we don't know how far deep it goes and so we have to recursivly find and empty left or right and insert the node there
    elif self.value == value:
          return value
    else:
          # if the value is larger then the root
          if self.value < value:
                # then we check to see if the right is empty if it is the assign that value
                if self.right is None:
                      self.right = BinarySearchTree(value)
                # if not then we have to continue down the tree and recall 'insert' with the value of the right side rather then the root
                else:
                      self.right.insert(value)
          # but if the value is smaller then the root then we repeat it again but go towards the left instead
          else:
                if self.value > value:
                      if self.left is None:
                            self.left = BinarySearchTree(value)
                      else:
                            self.left.insert(value)
    # pass

  def contains(self, target):
    # pass

    # first if the tree has no branches and is empty then we return false
    if self.value is None:
          return False

    # then if target is the root value which is 'self' then we return itself
    # this is also the basecase to end the loop once the value has been found
    elif target == self.value:
          return True

    # this is another base case to check if there are no more left or right values which is to say we reached the lowest possible section on the tree so the value isn't here so we return false
    elif self.right is None and self.left is None:
        return False

    # once we meet any of the above requiremients the recurrsion will stop but until then we go to the if statements here

    # if the target is larger then the root value we must go to the right so now we...
    if self.value < target:
          return self.right.contains(target)
          # recusivily run the function again but this time we use the right side value instead of the root value

    return self.left.contains(target)
    # this is the same as before but this time we know if it is not larger then the root value it's smaller so we go toward the left and then it recusivly runs until it hits the one of the three base cases it either doesn't exist or it returns the value

  def get_max(self):
    # this is pretty straight foward we want to go as FAR right as we can and that will give us the max number

    current_max = self
    while current_max.right:
          # so we use a while loop to only break out if there is "right" after that we just return the 'current_max'
          current_max = current_max.right
    return current_max.value
    # pass

  def for_each(self, cb):
    # pass
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb) 